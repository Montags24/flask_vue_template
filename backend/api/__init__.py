from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from api.bp_template import bp as bp_template
    app.register_blueprint(bp_template, url_prefix="/api/test")

    with app.app_context():

        db.init_app(app)
        migrate.init_app(app, db=db)

    return app
