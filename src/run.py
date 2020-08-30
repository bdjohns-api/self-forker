from flask import Flask

from app.api.core import api as core_blueprint


def run_app(debug=False):
    """
    Run App

    Register all blueprints with a flask instance and start the app.
    :param: debug indicates if the app should be started in debug mode.
    """
    app = Flask(__name__)
    app.register_blueprint(core_blueprint, url_prefix="/")
    app.run(host="0.0.0.0", port=8080, debug=debug)


if __name__ == "__main__":
    run_app(debug=True)

