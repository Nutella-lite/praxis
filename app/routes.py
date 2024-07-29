from flask import render_template, request, redirect, url_for
from app import app

posts = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post = {
            'name': request.form['name'],
            'email': request.form['email'],
            'town': request.form['town'],
            'age': request.form['age'],
            'hobby': request.form['hobby']
        }
        posts.append(post)
        return redirect(url_for('index'))
    return render_template('anketa.html', posts=posts)