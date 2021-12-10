from django.utils import translation
import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


class Test00Users:
    url = '/api/users/'

    @pytest.mark.django_db(transaction=True)
    def test_01_users_not_authenticated(self, client):
        response = client.get(self.url)

        assert response.status_code != 404, (
            f'Страница `{self.url}` не найдена, проверьте этот адрес в *urls.py*'
        )

        assert response.status_code == 401, (
            f'Проверьте, что при GET запросе `{self.url}` без токена авторизации возвращается статус 401'
        )

    @pytest.mark.django_db(transaction=True)
    def test_02_users_authenticated(self, auth_user_client, user):
        response = auth_user_client.get(self.url)

        assert response.status_code != 404, (
            f'Страница `{self.url}` не найдена, проверьте этот адрес в *urls.py*'
        )

        assert response.status_code == 200, (
            f'Проверьте, что при GET запросе `{self.url}` с токеном авторизации возвращается статус 200'
        )
        data = response.json()
        assert 'count' in data, (
            f'Проверьте, что при GET запросе `{self.url}` возвращаете данные с пагинацией. '
            'Не найден параметр `count`'
        )
        assert (
            len(data['results']) == 1
            and data['results'][0].get('id') == user.id
            and data['results'][0].get('username') == user.username
            and data['results'][0].get('email') == user.email
            and data['results'][0].get('first_name') == user.first_name
            and data['results'][0].get('last_name') == user.last_name
            and data['results'][0].get('is_subscribed') == False
        ), (
            f'Проверьте, что при GET запросе `{self.url}` возвращаете данные с пагинацией. '
            'Значение параметра `results` не правильное'
        )

    @pytest.mark.django_db(transaction=True)
    def test_03_nodata_signup(self, client):
        response = client.post(self.url)

        assert response.status_code != 404, (
            f'Страница `{self.url}` не найдена, проверьте этот адрес в *urls.py*'
        )
        request_type = 'POST'
        code = 400
        assert response.status_code == code, (
            f'Проверьте, что при {request_type} запросе `{self.url}` без параметров '
            f'не создается пользователь и возвращается статус {code}'
        )
        response_json = response.json()
        empty_fields = ['username', 'email',
                        'password', 'first_name', 'last_name']
        for field in empty_fields:
            assert (field in response_json.keys()
                    and isinstance(response_json[field], list)), (
                f'Проверьте, что при {request_type} запросе `{self.url}` без параметров '
                f'в ответе есть сообщение о том, какие поля заполенены неправильно'
            )
