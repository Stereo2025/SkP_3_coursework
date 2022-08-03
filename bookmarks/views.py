from flask import Blueprint, render_template, redirect
from classes.posts_class import Posts
from classes.bookmarks_class import BookMarks
from global_variables import DATA_PATH, BOOKMARKS_PATH

posts = Posts(DATA_PATH)
bookmarks = BookMarks(BOOKMARKS_PATH)


bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@bookmarks_blueprint.route("/bookmarks/add/<post_id>/")
def bookmarks_add_post(post_id):
    """ Добавляет посты в закладки."""

    add_bookmark = posts.get_post_by_pk(post_id)
    bookmarks.add_bookmarks(add_bookmark)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks/delete/<int:post_id>')
def page_bookmarks_delete(post_id):
    """  Удаляет посты из закладок"""

    post = posts.get_post_by_pk(post_id)
    bookmarks.delete_bookmarks(post)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/")
def all_bookmark():
    """Выводит все закладки"""

    bookmark = bookmarks.load_bookmarks()
    return render_template("bookmarks.html", bookmark=bookmark)
