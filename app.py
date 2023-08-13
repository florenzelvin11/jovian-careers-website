from flask import Flask, render_template

APP = Flask(__name__)

@APP.route("/")
def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
    APP.run(host='0.0.0.0', debug=True) # Do not edit this port
 