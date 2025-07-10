from flask import Flask, render_template
from .expenses import expenses_bp

app = Flask(__name__)

app.register_blueprint(expenses_bp, url_prefix='/expenses')

