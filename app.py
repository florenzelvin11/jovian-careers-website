from flask import Flask, render_template

APP = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Sydney, Australia',
        'salary': 'AUD 100,0000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Melbourne, Australia',
        'salary': 'AUD 80,0000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'AUD 100,0000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Sydney, Australia',
        'salary': 'AUD 120,0000'
    }
]

@APP.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Google")

if __name__ == "__main__":
    APP.run(host='0.0.0.0', debug=True) # Do not edit this port
 