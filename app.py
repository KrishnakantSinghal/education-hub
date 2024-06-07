from flask import Flask
from flask_admin import Admin

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"


admin = Admin(app, name="MyApp", template_mode="bootstrap3")
