from flask import Flask

from board import pages


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506"
    app.register_blueprint(pages.bp)
    return app
