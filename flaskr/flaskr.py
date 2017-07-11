import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='key',
    USERNAME='liliang',
    PASSWORD='rock'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

entries = [
    {
        'title': 1,
        'text': 'liliang1',
        'img': 'static/img/Koala.jpg'
    },
    {
        'title': 2,
        'text': 'liliang2',
        'img': 'static/img/Koala.jpg'
    },
    {
        'title': 3,
        'text': 'liliang3',
        'img': 'static/img/Koala.jpg'
    }
]


@app.route('/')
def show_entries():
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    entries.append(request.form)
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run(debug=True)