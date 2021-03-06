import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # creates Flask instance
    app = Flask(__name__, instance_relative_config=True)
    # override SECRET_KEY with random
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import generate
    app.register_blueprint(generate.bp)
    app.add_url_rule('/', endpoint='empty')

    return app


app = create_app()
