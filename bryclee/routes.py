from bryclee import app
from flask import request, render_template

@app.route('/')
def hello():
	print('Cookies:', request.cookies)
	return render_template('hello.html', name='visitor')
