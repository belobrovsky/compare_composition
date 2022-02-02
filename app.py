import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import bs


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/', methods=['GET', 'POST'])
def index():
    # conn = get_db_connection()
    # posts = conn.execute('SELECT * FROM posts').fetchall()
    # conn.close()
    # return render_template('index.html', posts=posts)
    rows = []
    info = {}
    if request.method == 'POST':
        # pass
        if request.form:
            number = request.form['number']
            bs.pars_znp(number)
            rows.clear()
            rows, info = bs.getElements()
        # else:
        #     element = []
        # bs.pars_znp('0')
    # else:
    #     bs.pars_znp('294156002')

    return render_template('index.html', rows=rows, info=info)
    # return elements[5]


@app.route('/delete', methods=['POST'])
def delete():
    # if request.method == 'POST':
    bs.delete()
    # element = []
    return redirect(url_for('index'))

# @app.route('/', methods=['POST'])
# def search():
#     # if request.method == 'POST':
#     number = request.form['number']
#     return number



@app.route('/78')
def post():
    pass


@app.route('/89')
def create():
    pass


@app.route('/5665')
def edit():
    pass


# @app.route('/566+')
# def delete():
#     pass

# # @app.route('/<int:post_id>')
# @app.route('/<int:post_id>')
# def post(post_id):
#     pass
#     # post = get_post(post_id)
#     # return render_template('post.html', post=post)
# #
# #
# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#
#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
#                          (title, content))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#
#     return render_template('create.html')
#
#
# @app.route('/<int:id>/edit', methods=['GET', 'POST'])
# def edit(id):
#     post = get_post(id)
#
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#
#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('UPDATE posts SET title = ?, content = ?'
#                          ' WHERE id = ?',
#                          (title, content, id))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#
#     return render_template('edit.html', post=post)
#
#
# @app.route('/<int:id>/delete', methods=['POST', ])
# def delete(id):
#     post = get_post(id)
#     conn = get_db_connection()
#     conn.execute('DELETE FROM posts WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     flash('"{}" was successfully deleted!'.format(post['title']))
#     return redirect(url_for('index'))
