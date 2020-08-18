import sqlite3
##from sqlalchemy.pool import SingletonThreadPool
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    db = sqlite3.connect('lecture.db')
    cu = db.cursor()
    rows = cu.execute("SELECT * FROM registrants")
    cu.close() # Use cu.commit() before close() if you inserted any data
    return render_template("index.html", rows=rows)
