from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "5765d60537dee0d98783a4c3a327c852"


# routes must be imported at the bottom
from flaskapp import routes