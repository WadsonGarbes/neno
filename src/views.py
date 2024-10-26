from flask import current_app as app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Neno'}
    return render_template('index.html', title='Home', user=user)
