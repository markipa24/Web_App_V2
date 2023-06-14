from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs_list = load_jobs_from_db()
  return render_template('home.html', jobs=jobs_list)


@app.route("/api/jobs")
def list_jobs():
  jobs_list = load_jobs_from_db()
  return jsonify(jobs_list)


@app.route("/job/<id>")
def show_jobs(id):
  jobs_list = load_job_from_db(id)
  if not jobs_list:
    return "Not Found", 404
  #return jsonify(jobs_list)
  return render_template('jobpage.html', jobs=jobs_list)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  #Store this in the DB
  #Display an acknowledgement
  #Send an email
  ##return jsonify(data)
  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
