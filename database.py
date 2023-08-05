from sqlalchemy import create_engine, text


db_conn = os.environ['DB_CONN']


engine = create_engine(
  db_conn ,
connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })
  


def load_all():
  with engine.connect() as conn:
     s = text("select * FROM job_list")
     

     return conn.execute(s).fetchall()


def find_job(id):
  with engine.connect() as conn:
     s = text("select * FROM job_list WHERE job_id = "+str(id))
     s=conn.execute(s).fetchall()
     rows = s
     if len(rows) == 0:
      return None
     else:
      return rows
      





def pagination(id):
  off = (id-1)*5
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM job_list LIMIT "+str(off)+",5"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows
                                                  
                                                                                          
def apply(data):
  with engine.connect() as conn:
    result = conn.execute(text("INSERT INTO User (name,email,job_id,linkdin_url,resume,password) VALUES ('"+data['fullname']+"','"  +data['email']+ "',"+data['job_id']+ ",'"+data['linkdin_url']+  "','"+data['resume_url']+  "','" +data['password']+"')") )         
