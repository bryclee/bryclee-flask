import os
from imgurpython import ImgurClient
from bryclee import app
from flask import request, make_response

def getClientId():
	try:
		return os.environ['IMGUR_ID']
	except KeyError:
		from bryclee.secret import client_id
		return client_id

def getClientSecret():
	try:
		return os.environ['IMGUR_SECRET']
	except KeyError:
		from bryclee.secret import client_secret
		return client_secret

client_id = getClientId()
client_secret = getClientSecret()

client = ImgurClient(client_id, client_secret)

@app.route('/mirror/<id>', methods=['GET'])
def imgur_mirror(id):
	image = client.get_image(id)
	print(image)
	return '1'
