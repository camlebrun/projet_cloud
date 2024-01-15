from flask import Flask

app = Flask(__name__)

def before_first_request():
    print('Hello, Bravo les lesbiennes !')

before_first_request()

@app.route('/')
def hello():
    return 'Hello, Flask app!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=True)
