import os, sys
from bryclee import app
from flask import request, render_template, jsonify

from bryclee.imgur import imgurRequest

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

@app.route('/mirror/<path>', methods=['GET'])
def imgur_mirror(path):
	return render_template('imgur.html', url='/imgur/' + path)

#Could remove having two paths if I can set the content type of the images properly
@app.route('/imgur/<path>', methods=['GET'])
def imgur(path):
	return imgurRequest(path)
