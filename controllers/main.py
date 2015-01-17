from flask import *

main = Blueprint('main', __name__, template_folder='views')

@main.route('/')
def main_route():
    options = {}
    return render_template("index.html", **options)

@app.route('/issues')
def issues():
	options = {}
	return render_template("issues.html", **options)