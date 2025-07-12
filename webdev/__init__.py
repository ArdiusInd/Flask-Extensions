from flask import Flask, redirect, url_for
from .expenses import expenses_bp
from .home import home_bp

app = Flask(__name__)
#app.config["EXPLAIN_TEMPLATE_LOADING"] = True

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(expenses_bp, url_prefix='/expenses')

# redirct the beginning home page to the home blueprint
@app.route('/')
def index():
    return redirect(url_for('home.index'))

