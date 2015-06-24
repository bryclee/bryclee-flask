import os
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
	print('Cookies:', request.cookies)
	return render_template('hello.html', name='visitor')
