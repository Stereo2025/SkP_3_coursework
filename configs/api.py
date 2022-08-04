import os
import logging
from flask import Blueprint, jsonify, abort
from classes.posts_class import Posts
from global_variables import DATA_PATH, PATH_LOGS_CONFIG


posts = Posts(DATA_PATH)

path = os.path.join(PATH_LOGS_CONFIG)

# создание логера
logger_api = logging.getLogger("config")
# FileHandler == запись в файл
file_handler = logging.FileHandler(path)
# уровень логера - INFO.
logger_api.setLevel("INFO")
# Формат записи логов.
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# форматирование
file_handler.setFormatter(formatter_api)
# запись в файл логов
logger_api.addHandler(file_handler)

config_blueprint = Blueprint('config_blueprint', __name__)


@config_blueprint.route("/api/posts/", methods=["GET"])
def page_post_form():
    """Возвращает полный список постов в виде списка json"""

    logger_api.info("запрос всех постов")
    post = posts.load_data()
    if not post:
        abort(404)
    return jsonify(post)


@config_blueprint.route("/api/posts/<int:post_id>", methods=["GET"])
def page_post_pk(post_id):
    """Возвращает один пост в виде словаря json."""

    logger_api.info(f"запрос постов по {post_id}")
    post = posts.get_post_by_pk(post_id)
    if not post:
        abort(404)
    return jsonify(post)


@config_blueprint.route("/api/posts/<username>", methods=["GET"])
def page_post_name(username):
    """Возвращает пост по имени пользователя в словаре json"""

    logger_api.info(f"запрос постов по {username}")
    post = posts.get_post_by_user_name(username)
    if not post:
        abort(404)
    return jsonify(post)


@config_blueprint.errorhandler(404)
def page_400_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return jsonify({"Error": 'Information Not Found'}), 404
