from flask import Flask
from flask import render_template, send_from_directory
import webscrape
app = Flask(__name__)


class Config():
    APP_NAME = 'FarmBuild'

    # Enable debug mode
    DEBUG = True
    ALLOWED_HEADERS = ['Origin', 'Accept', 'Content-Type', 'X-Requested-With', 'X-CSRF-Token']
    ALLOWED_ORIGINS = '*'
    ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']

    # TODO
    # This is where frontend should go, create a route for all UI files
    # Setup template folder for webpages
    TEMPLATE_FOLDER = "templates"


app = Flask(
    Config.APP_NAME, 
    template_folder=Config.TEMPLATE_FOLDER, 
    static_folder=Config.TEMPLATE_FOLDER
)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/earthquake.html')
def scrape_page():
    return render_template('earthquake.html')

@app.route('/')
def run_script():
    file = open(r'real_time/webscrape.py', 'r').read()
    return exec(file)

@app.route('/js/<path:path>')
def send_js(path):
    print(path)
    return send_from_directory('templates/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('templates/img', path)

@app.route('/json/<path:path>')
def send_json(path):
    return send_from_directory('templates/json', path)

@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('templates/assets', path)

    
if __name__ == "__main__":
	app.run(debug= True)
