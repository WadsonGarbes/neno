from flask import current_app as app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"
