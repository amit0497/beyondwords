from flask import Flask
import logging



logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)

@app.route('/')
def index():
    logging.info("Default Route")
    return 'Hello from beyondwords!'

@app.route('/test')
def test():
    logging.info("Test Route")
    return 'Test from beyondwords!'

@app.route('/health')
@app.route('/ready')
def check():
    logging.info("Health and Ready Route")
    return 'Health and Ready from beyondwords!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
