from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from beyondwords!'

@app.route('/test')
def test():
    return 'Test from beyondwords!'

@app.route('/health')
@app.route('/ready')
def check():
    return 'Health and Ready from beyondwords!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
