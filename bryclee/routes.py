import os, sys
from bryclee import app
from flask import request, render_template, jsonify

#Sample data
from bryclee.database.fakeData import jsonData

#Routes
@app.route('/')
def index():
	return render_template('index.html', posts=jsonData)

@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
	if id < len(jsonData) and id >= 0:
		return jsonify(post=jsonData[id])
	else:
		return jsonify(error="Out of range")

@app.route('/posts', methods=['GET'])
def get_posts():
	return 'a bunch of posts'

@app.route('/test')
def test():
	return render_template('post.html', posts=jsonData)
