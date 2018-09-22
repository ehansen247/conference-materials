from flask import Flask
import socket
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route("/host")
def index():
    return "Hello from FLASK. My Hostname is: %s \n" % (socket.gethostname())

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)