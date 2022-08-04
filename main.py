from flask import Flask, render_template
import logging
from configs.api import config_blueprint
from bookmarks.views import bookmarks_blueprint
from posts.views import posts_blueprint
from global_variables import PATH_MAIN_LOGS


FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(filename=PATH_MAIN_LOGS, level=logging.INFO, format=FORMAT)


app = Flask(__name__)
app.register_blueprint(config_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(posts_blueprint)
app.config['JSON_AS_ASCII'] = False


@app.errorhandler(404)
def page_404_error(error):
    """ Обработчик запросов к несуществующим страницам"""

    return render_template('page_404_error.html',
                           title="Страница не найдена", error=404), 404


@app.errorhandler(500)
def page_500_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return render_template('page_500_error.html',
                           title="Сервер не отвечает", error=500), 500


if __name__ == "__main__":
    app.run(debug=True)
