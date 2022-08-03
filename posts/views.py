from flask import Blueprint, render_template, request
from classes.posts_class import Posts
from classes.bookmarks_class import BookMarks
from classes.comments_class import Comments
from global_variables import DATA_PATH, COMMENTS_PATH, BOOKMARKS_PATH


posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts = Posts(DATA_PATH)
comments = Comments(COMMENTS_PATH)
bookmarks = BookMarks(BOOKMARKS_PATH)


@posts_blueprint.route('/')
def main_page():
    """Главная страничка с постами.
    На главной страничке они обрезаны по 30 символов
    """

    return render_template('index.html', all_posts=posts.load_data(),
                           comment=len(bookmarks.load_bookmarks()))


@posts_blueprint.route("/post/<int:post_id>/")
def show_post(post_id):
    """Страничка просмотра поста"""

    post = posts.view_post(post_id)
    return render_template('post.html', post=post,
                           posts=comments.get_some_comment(post_id),
                           count_coments=len(comments.get_some_comment(post_id)))


@posts_blueprint.route('/search/')
def search_page():
    """Поиск подслов в постах"""

    word = request.args.get('word')
    post = posts.get_post_by_keyword(word)
    return render_template('search.html', word=word, posts=post, len_post=len(post))


@posts_blueprint.route('/users/<username>/')
def show_user_post(username):
    """Реализует просмотр поста по имени пользователя"""

    post = posts.get_post_by_user_name(username)
    return render_template('user-feed.html', posts=post)


@posts_blueprint.route("/tag/<tag_name>/")
def show_tag_page(tag_name):
    """Реализует просмотр поста по тэгу"""

    post = posts.get_post_by_tagname('#' + tag_name)
    for line in post:
        if tag_name in line['content']:
            return render_template('tag.html', tag_name=posts.get_post_by_tagname(tag_name),
                                   search=tag_name)
