from bryclee import app
from flask import request, render_template

@app.route('/')
def hello():
	return render_template('index.html', name='visitor')
