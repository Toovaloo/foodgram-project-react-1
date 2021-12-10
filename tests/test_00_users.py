from django.utils import translation
import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


class Test00Users:
    url = '/api/users/'

    @pytest.mark.django_db(transaction=True)
    def test_00_users_not_authenticated(self, client):
        response = client.get(self.url)

        assert response.status_code != 404, (
            f'Страница `{self.url}` не найдена, проверьте этот адрес в *urls.py*'
        )

        assert response.status_code == 401, (
            f'Проверьте, что при GET запросе `{self.url}` без токена авторизации возвращается статус 401'
        )

    @pytest.mark.django_db(transaction=True)
    def test_00_users_authenticated(self, auth_user_client, user):
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
    def test_00_nodata_signup(self, client):
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

    @pytest.mark.django_db(transaction=True)
    def test_00_invalid_data_signup(self, client):
        invalid_email = 'invalid_email'
        invalid_username = 'invalid username'

        invalid_data = {
            'email': invalid_email,
            'username': invalid_username
        }
        request_type = 'POST'
        response = client.post(self.url, data=invalid_data)

        assert response.status_code != 404, (
            f'Страница `{self.url}` не найдена, проверьте этот адрес в *urls.py*'
        )
        code = 400
        assert response.status_code == code, (
            f'Проверьте, что при {request_type} запросе `{self.url}` с невалидными данными '
            f'не создается пользователь и возвращается статус {code}'
        )

        response_json = response.json()
        invalid_fields = ['email', 'username']
        for field in invalid_fields:
            assert (field in response_json.keys()
                    and isinstance(response_json[field], list)), (
                f'Проверьте, что при {request_type} запросе `{self.url}` с невалидными параметрами, '
                f'в ответе есть сообщение о том, какие поля заполенены неправильно'
            )

        valid_email = 'validemail@yamdb.fake'
        invalid_data = {
            'email': valid_email,
        }
        response = client.post(self.url, data=invalid_data)
        assert response.status_code == code, (
            f'Проверьте, что при {request_type} запросе `{self.url}` без username '
            f'нельзя создать пользователя и возвращается статус {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_00_valid_data_user_signup(self, client):

        valid_email = 'valid@yamdb.fake'
        valid_username = 'valid_username'
        valid_first_name = 'Ivan'
        valid_last_name = 'Ivanov'
        valid_password = 'sECretPaSSw0rd'

        valid_data = {
            'email': valid_email,
            'username': valid_username,
            'first_name': valid_first_name,
            'last_name': valid_last_name,
            'password': valid_password,
        }
        request_type = 'POST'
        response = client.post(self.url, data=valid_data)

        assert response.status_code != 404, (
            f'Страница `{self.url}` не найдена, проверьте этот адрес в *urls.py*'
        )

        code = 201
        assert response.status_code == code, (
            f'Проверьте, что при {request_type} запросе `{self.url}` с валидными данными '
            f'создается пользователь и возвращается статус {code}'
        )
        data = response.json()
        assert (
            data.get('username') == valid_username
            and data.get('email') == valid_email
            and data.get('first_name') == valid_first_name
            and data.get('last_name') == valid_last_name
        ), (
            f'Проверьте, что при {request_type} запросе `{self.url}` с валидными данными '
            f'создается пользователь и возвращается статус {code}'
        )

        hidden_fields = ['password', ]
        for field in hidden_fields:
            assert field not in data.keys(), (
                f'Проверьте, что при {request_type} запросе `{self.url}`'
                f'возвращяются только предусмотренные спецификацией поля.'
            )

        new_user = User.objects.filter(email=valid_email)
        assert new_user.exists(), (
            f'Проверьте, что при {request_type} запросе `{self.url}` с валидными данными '
            f'создается пользователь и возвращается статус {code}'
        )

        new_user.delete()
