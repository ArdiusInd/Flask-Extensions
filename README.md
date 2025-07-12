# Flask-Extensions
Flask Web App using Flask extensions

## Flask Blueprints
Flask Blueprints allow one to build completely independent modules with a catch.   The 'static' and 'templates' folders can be tricky to create.   Note:  That flask blueprint registration adds the templates and static path to a search list.   When the flask application goes to render the web page, it can get the wrong one if the name is the same when searching for the html file.

Example:
   If you have two blueprints a and b where the folder is like:

   a/
     templates/
        index.html
      views.py
   b/
      templates/
         index.html
      views.py
   main.py

  In a/views.py:
      bp_a = Blueprint('a', __name__, template_folder='templates')

      @a.route('/')
      def a():
          return render_template('a/index.html')

  In b/views.py:
      bp_b = Blueprint('b', __name__, template_folder='templates')

      @a.route('/')
      def a():
          return render_template('b/index.html')

and in the main.py:
   from a import bp_a
   from b import bp_b
   app = Flask(__name__)
   app.register_blueprint(bp_a, url_prefix='/a')
   app.register_blueprint(bp_b, url_prefix='/b')

Then the /b/index.html file in b/templates will never be used since it will find index.html in the /a/index.html path first.  This is why they recommend adding the blueprint directory as 'a/templates/a' and 'b/templates/b' to ensure uniqueness along all paths.