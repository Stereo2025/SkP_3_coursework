from flask import Flask
from configs.config import config_blueprint
from handlers_erors.views import handlers_blueprint
from bookmarks.views import bookmarks_blueprint
from posts.views import posts_blueprint


app = Flask(__name__)
app.register_blueprint(config_blueprint)
app.register_blueprint(handlers_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(posts_blueprint)
app.config['JSON_AS_ASCII'] = False


if __name__ == "__main__":
    app.run(debug=True)
