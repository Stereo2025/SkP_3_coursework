import pytest
from classes.comments_class import Comments
from global_variables import COMMENTS_PATH


data_keys = {'post_id', 'commenter_name', 'comment', 'pk'}


class TestComments:

    def test_load_data(self):
        comments = Comments(COMMENTS_PATH)
        assert type(comments.load_comments()) == list, 'Возвращается не list[dict]'
        assert len(comments.load_comments()) > 0, "Возвращается пустой list[dict]"
        assert set(comments.load_comments()[0].keys()) == data_keys, 'Ошибочный список ключей'

    def test_get_some_comment(self):
        post = Comments(COMMENTS_PATH)
        assert type(post.get_some_comment(1)) == list, 'Возвращается не list[dict]'
        assert len(post.get_some_comment(1)) > 0, "Возвращается пустой list[dict]"

    def test_get_some_comment_type_error(self):
        post = Comments(COMMENTS_PATH)
        with pytest.raises(TypeError):
            post.get_some_comment(1.1)

    def test_get_some_comment_value_error(self):
        post = Comments(COMMENTS_PATH)
        with pytest.raises(ValueError):
            post.get_some_comment(-1)
