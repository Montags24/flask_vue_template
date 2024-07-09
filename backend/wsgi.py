import os
from dotenv import load_dotenv

from api import create_app

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

# Set the environment type eg. development, production
config_name = os.environ.get("INSTANCE_TYPE")
app = create_app(config_name)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
