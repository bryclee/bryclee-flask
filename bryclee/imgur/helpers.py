import os
from flask import make_response
from imgurpython import ImgurClient
from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urlencode


#Initialize Imgur API for fetching image data
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

#Imgur client
client = ImgurClient(client_id, client_secret)

#Retrieve data about the image
def get_imgur_data(id):
	imageData = client.get_image(id)
	images[id] = {
		'link': getattr(imageData, 'link'),
		'mimetype': getattr(imageData, 'type')
	}

	return {
		'title': getattr(imageData, 'title'),
		'description': getattr(imageData, 'description'),
		'id': getattr(imageData, 'id')
	}

images = {}

#Gets the image at the requested path from imgur, cache result in a dict
def get_imgur_image(id):
	try:
		imageData = images.pop(id)
		link = imageData['link']
		mimetype = imageData['mimetype']
	except KeyError:
		imageData = client.get_image(id)
		link = getattr(imageData, 'link')
		mimetype = getattr(imageData, 'type')

	req = Request(link, None, {}, None, None, 'GET')

	try:
		image = urlopen(req)
	except URLError as e:
		return e.code

	response = make_response(image.read())
	response.headers['Content-type'] = mimetype
	return response

