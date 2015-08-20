import os, sys
from bryclee import app
from flask import request, render_template, jsonify

from bryclee.imgur import get_imgur_image, get_imgur_data

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
	imgurData = get_imgur_data(path)
	return render_template('image.html', data=imgurData)

#Could remove having two paths if I can set the content type of the images properly
@app.route('/image/<path>', methods=['GET'])
def imgur(path):
	return get_imgur_image(path)
