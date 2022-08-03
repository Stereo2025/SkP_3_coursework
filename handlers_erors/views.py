from flask import Blueprint, render_template


handlers_blueprint = Blueprint('handlers_blueprint', __name__, template_folder='templates')


@handlers_blueprint.errorhandler(404)
def page_404_error(error):
    """ Обработчик запросов к несуществующим страницам"""

    return render_template('page_404_error.html', title="Страница не найдена", error=error)


@handlers_blueprint.errorhandler(500)
def page_500_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return render_template('page_500_error.html', title="Сервер не отвечает", error=error)
