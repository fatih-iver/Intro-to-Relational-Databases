# "Database code" for the DB Forum.
import psycopg2
import bleach

DNAME = "forum"


#POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DNAME)
  c = db.cursor()  
  c.execute("select content, time from posts order by time desc")
  rows = c.fetchall()
  db.close()
  return rows


#def get_posts():
  #"""Return all posts from the 'database', most recent first."""
  #return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DNAME)
  c = db.cursor() 
  c.execute("INSERT INTO posts values (%s) ", (bleach.clean(content),))
  db.commit()
  db.close()

#def add_post(content):
  #"""Add a post to the 'database' with the current timestamp."""
  #POSTS.append((content, datetime.datetime.now()))


