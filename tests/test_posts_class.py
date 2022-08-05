import pytest
from classes.posts_class import Posts
from global_variables import DATA_PATH


data_keys = {'poster_name', 'poster_avatar', 'pic', 'content',
             'views_count', 'likes_count', 'pk'}

search_for_posts_exceptions = [(322, TypeError), (3.22, TypeError), (True, TypeError)]


class TestPosts:

    def test_load_data(self):
        post = Posts(DATA_PATH)
        assert type(post.load_data()) == list, 'Возвращается не list[dict]'
        assert len(post.load_data()) > 0, "Возвращается пустой list[dict]"
        assert set(post.load_data()[0].keys()) == data_keys, 'Ошибочный список ключей'

    def test_get_post_by_user_name(self):
        post = Posts(DATA_PATH)
        assert type(post.get_post_by_user_name("Leo")) == list, 'Возвращается не list[dict]'
        assert len(post.get_post_by_user_name("Leo")) > 0, "Возвращается пустой list[dict]"

    def test_get_post_by_user_name_type_error(self):
        post = Posts(DATA_PATH)
        with pytest.raises(TypeError):
            post.get_post_by_user_name(1)

    def test_get_post_by_user_name_value_error(self):
        post = Posts(DATA_PATH)
        with pytest.raises(ValueError):
            post.get_post_by_user_name('1')

    def test_get_post_by_keyword(self):
        post = Posts(DATA_PATH)
        assert type(post.get_post_by_keyword('Вот')) == list, 'Возвращается не list[dict]'
        assert len(post.get_post_by_keyword('Вот')) > 0, "Возвращается пустой list[dict]"

    # @pytest.mark.parametrize('input_str, exceptions', search_for_posts_exceptions)
    # def test_search_for_posts_exceptions(self, input_str, exceptions):
    #     post = Posts(DATA_PATH)
    #     with pytest.raises(exceptions):
    #         post.get_post_by_keyword(self, input_str)

    # def test_get_post_by_keyword_type_error(self):
    #     post = Posts(DATA_PATH)
    #     with pytest.raises(TypeError):
    #         post.get_post_by_user_name(1)
    #
    # def test_get_post_by_keyword_value_error(self):
    #     post = Posts(DATA_PATH)
    #     with pytest.raises(ValueError):
    #         post.get_post_by_user_name('1')

    def test_get_post_by_pk(self):
        post = Posts(DATA_PATH)
        assert type(post.get_post_by_pk(1)) == dict, 'Возвращается не list[dict]'
        assert len(post.get_post_by_pk(1)) > 0, "Возвращается пустой list[dict]"

    # def test_get_post_by_pk_type_error(self):
    #     post = Posts(DATA_PATH)
    #     with pytest.raises(TypeError):
    #         post.get_post_by_pk(1.1)
    #
    # def test_get_post_by_pk_value_error(self):
    #     post = Posts(DATA_PATH)
    #     with pytest.raises(ValueError):
    #         post.get_post_by_pk(-1)

    def test_get_post_by_tagname(self):
        post = Posts(DATA_PATH)
        assert type(post.get_post_by_tagname("#Кот")) == list, 'Возвращается не list[dict]'
        assert len(post.get_post_by_tagname("#инста")) > 0, "Возвращается пустой list[dict]"

    # def test_test_get_post_by_tagnametype_error(self):
    #     post = Posts(DATA_PATH)
    #     with pytest.raises(TypeError):
    #         post.get_post_by_tagname(1)
    #
    # def test_test_get_post_by_tagname_value_error(self):
    #     post = Posts(DATA_PATH)
    #     with pytest.raises(ValueError):
    #         post.get_post_by_tagname('1')

    def test_view_post(self):
        post = Posts(DATA_PATH)
        assert type(post.view_post(1)) == dict, 'Возвращается не list[dict]'
        assert len(post.view_post(1)) > 0, "Возвращается пустой list[dict]"

    def test_view_post_type_error(self):
        post = Posts(DATA_PATH)
        with pytest.raises(TypeError):
            post.view_post(1.1)

    def test_view_post_value_error(self):
        post = Posts(DATA_PATH)
        with pytest.raises(ValueError):
            post.view_post(-1)
