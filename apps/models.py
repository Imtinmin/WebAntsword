import sqlite3
from flask import g
from apps import app
DATABASE = 'C:\\Users\\Imtinmin\\Desktop\\shellsite\\apps\\test.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def gethistory():
	with app.app_context():
		success = query_db('select * from WEBSHELL',one=False)
		if success:
			return success