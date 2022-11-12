import os

from flask import Flask

from views import main_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    return app


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")




if __name__ == '__main__':
    app = create_app()
    app.run(port=25000)
