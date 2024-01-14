import pytest

from app.profiles.auth import get_jwt_strategy


@pytest.fixture
async def test_token(create_user_in_database):
    user_data = {
        'username': 'testuser',
        'email': "test@test.com",
        'password': 'PASSWORD'
    }
    user = await create_user_in_database(**user_data)
    strategy = get_jwt_strategy()
    return await strategy.write_token(user)


async def test_get_image_info(app, client, event_loop, test_token):
    response = await client.post(
        '/image/',
        files={"file": ("filename", b'some', "image/png")},
        data={'title': 'title'},
        headers={"Authorization": f"Bearer {test_token}"}
    )
    assert response.json()['title'] == 'title'
    assert response.status_code == 200
