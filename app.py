import sqlite3
##from sqlalchemy.pool import SingletonThreadPool
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    db = sqlite3.connect('lecture.db')
    rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html", rows=rows)
