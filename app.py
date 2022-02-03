import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import bs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    rows = []
    info = {}
    if request.method == 'POST':
        if request.form:
            number = request.form['number']
            bs.pars_znp(number)
            rows.clear()
            rows, info = bs.getElements()
        return render_template('index.html', rows=rows, info=info)

@app.route('/delete', methods=['POST'])
def delete():
    bs.delete()
    return redirect(url_for('index'))
