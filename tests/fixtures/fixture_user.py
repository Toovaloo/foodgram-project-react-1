import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser',
        email='testuser@foodgram.fake',
        password='1234567',
        first_name='TestFirstName',
        last_name='TestLastName',
    )


@pytest.fixture
def access_token(user):
    from rest_framework_simplejwt.tokens import AccessToken
    token = AccessToken.for_user(user)

    return {
        'access': str(token),
    }


@pytest.fixture
def auth_user_client(access_token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token["access"]}')
    return client
