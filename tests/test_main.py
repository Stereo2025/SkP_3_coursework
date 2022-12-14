from app import app

data_keys = {'poster_name', 'poster_avatar', 'pic', 'content',
             'views_count', 'likes_count', 'pk'}


class TestMain:

    def test_main_page(self):
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_post_page(self):
        response = app.test_client().get('/post/1/')
        assert response.status_code == 200

    def test_search_page(self):
        result = {'word': "Смотрите"}
        response = app.test_client().get('/search/', query_string=result)
        assert response.status_code == 200

    def test_users_page(self):
        response = app.test_client().get('/users/leo/')
        assert response.status_code == 200

    # ************************************************************************* #

    # На show_tag_page из post/views.py, не смог написать тесты, поиск по тэгу
    # почему-то не работает... хотя ссылка с тэгом отображается корректно.

    # ************************************************************************* #
