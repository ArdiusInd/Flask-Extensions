from flask import Blueprint

expenses_bp = Blueprint('expenses', __name__, 
                        template_folder='templates', 
                        static_folder='static')

from . import routes
