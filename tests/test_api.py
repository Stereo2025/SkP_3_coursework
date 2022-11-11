from app import app

data_keys = {'poster_name', 'poster_avatar', 'pic', 'content',
             'views_count', 'likes_count', 'pk'}


class TestApi:

    def test_page_post_form(self):
        response = app.test_client().get('/api/posts/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список!'

    def test_element_key(self):
        response = app.test_client().get('/api/posts/')
        assert len(response.json[0]) == len(data_keys), "Ошибка в количестве ключей"
        assert set(response.json[0]) == data_keys, "Ошибка в названии ключей"

    def test_page_post_pk(self):
        response = app.test_client().get('/api/posts/1')
        assert response.status_code == 200
        assert type(response.json) == dict, "Это не словарь!"

    def test_page_post_name(self):
        response = app.test_client().get('/api/posts/leo')
        assert response.status_code == 200
        assert type(response.json) == list

    def test_page_not_found_name(self):
        response = app.test_client().get('/api/post/George')
        assert response.status_code == 404

    def test_page_not_found_id(self):
        response = app.test_client().get('/api/post/1000')
        assert response.status_code == 404

    def test_page_not_found(self):
        response = app.test_client().get('/api/post/')
        assert response.status_code == 404
