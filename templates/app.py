from flask import Flask
from flask import render_template, send_from_directory
import webscrape
app = Flask(__name__)


# Loads the needed config in the configuration file
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', app.config['ALLOWED_ORIGINS'])
    response.headers.add('Access-Control-Allow-Headers', ','.join(app.config['ALLOWED_HEADERS']))
    response.headers.add('Access-Control-Allow-Methods', ','.join(app.config['ALLOWED_METHODS']))
    return response

@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html',)

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

@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('templates/assets', path)

    
if __name__ == "__main__":
	app.run(host='0.0.0.0', use_reloader=True, threaded=True)
