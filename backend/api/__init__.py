from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    # This configuration allows all origins (*) to access endpoints under /api
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config[config_name])

    from api.bp_template import bp as bp_template

    app.register_blueprint(bp_template, url_prefix="/api/test")

    with app.app_context():

        db.init_app(app)
        migrate.init_app(app, db=db)

    return app


from api import models  # noqa: F401 E402
