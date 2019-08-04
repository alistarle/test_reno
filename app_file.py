import os

from flask import Flask
from dynaconf import FlaskDynaconf

def generate_vault_path():
    app_name = os.environ.get('FLASK_APP_NAME', '')
    region = os.environ.get('FLASK_REGION', 'eu-fr-paris')
    environment = os.environ.get('FLASK_ENV', 'DEV')
    return 'secret/data/%s/%s/%s/' % (app_name, environment, region)

app = Flask(__name__)
FlaskDynaconf(app,
              VAULT_PATH_FOR_DYNACONF=generate_vault_path())


@app.route("/")
def hello():
    print(app.config['VAULT_PATH_FOR_DYNACONF'])
    return "<h1 style='color:blue'>Hello There ! %s, %s</h1>" % (app.config['HELLO'], app.config['DB_ADDR'])

if __name__ == "__main__":
    app.run(host='0.0.0.0')