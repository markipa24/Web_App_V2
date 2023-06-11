from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})

#with engine.connect() as conn:
#result = conn.execute(text("select * from mmi.jobs01"))

#print("type(result):", type(result))
#result_all = result.all()
#print("type(result.all():", type(result_all))
#first_result = result_all[0]
#print("type(first_result):", type(first_result))
#first_result_dict = result_all[0]._asdict()
#print(first_result_dict)
#for row in result_all:
#print(row)

#result_dicts = []
#for row in range(0, len(result_all)):
#result_dicts.append(result_all[row]._asdict())
#print(result_dicts)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from mmi.jobs01"))
    jobs = []
    result_all = result.all()
    for row in range(0, len(result_all)):
      jobs.append(result_all[row]._asdict())
    return jobs