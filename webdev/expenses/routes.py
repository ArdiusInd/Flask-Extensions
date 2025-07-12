from flask import  render_template, redirect, url_for
from . import expenses_bp


@expenses_bp.route('/')
@expenses_bp.route('/home')
def index():
    return render_template('expenses/dashboard.html')