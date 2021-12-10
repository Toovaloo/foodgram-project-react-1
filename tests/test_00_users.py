import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


class Test00Users:

    @pytest.mark.django_db(transaction=True)
    def test_01_users_not_authenticated(self, client):
        response = client.get('/api/users/')

        assert response.status_code != 404, (
            'Страница `/api/users/` не найдена, проверьте этот адрес в *urls.py*'
        )

        assert response.status_code == 401, (
            'Проверьте, что при GET запросе `/api/users/` без токена авторизации возвращается статус 401'
        )

    @pytest.mark.django_db(transaction=True)
    def test_02_users_authenticated(self, auth_user_client, user):
        response = auth_user_client.get('/api/users/')

        assert response.status_code != 404, (
            'Страница `/api/users/` не найдена, проверьте этот адрес в *urls.py*'
        )

        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/users/` с токеном авторизации возвращается статус 200'
        )
        data = response.json()
        assert 'count' in data, (
            'Проверьте, что при GET запросе `/api/users/` возвращаете данные с пагинацией. '
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
            'Проверьте, что при GET запросе `/api/v1/users/` возвращаете данные с пагинацией. '
            'Значение параметра `results` не правильное'
        )
