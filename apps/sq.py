import sqlite3
from flask import g,Flask 
app = Flask(__name__)

DATABASE = './test.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



if __name__ == '__main__':
	#app.run('0.0.0.0',10000,debug=True)
	with app.app_context():
		user = query_db('select * from WEBSHELL',one=False)
		if user is None:
			print 'No such user'
		else:
			print user[0][1]