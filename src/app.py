from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to the Open-Source Ticket Info Project'

if __name__ == '__main__':
    app.run(host='0.0.0.0')