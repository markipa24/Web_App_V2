from flask import Flask, render_template

app = Flask(__name__)



JOBS = [
    {
      'id':1,
      'title': 'Structural Engineer',
      'location': 'Philippines',
      'salary': 'P30,000'
    },
    {
      'id':2,
      'title': 'Computational Engineer',
      'location': 'HongKong',
      'salary': 'P50,000'
    },
    {
      'id':3,
      'title': 'Project Manager',
      'location': 'Australia',
      'salary': 'P150,000'
    }
]

@app.route("/")

def hello_world():
    return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
  
