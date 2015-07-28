import os
from bryclee import app
from flask import request, render_template, jsonify

@app.route('/')
def index():
	return render_template('index.html', name='visitor')

@app.route('/posts/<id>', methods=['GET'])
def get_post(id):
	return jsonify(tag="intro",
					id=id,
					text="Hello, this is a normal post.")
