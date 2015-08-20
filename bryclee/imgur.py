import os
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
	image = client.get_image(id)
	return {
				'title': getattr(image, 'title'),
				'description': getattr(image, 'description'),
				'link': getattr(image, 'link')
			}


images = {}

#Gets the image at the requested path from imgur, cache result in a dict
def get_imgur_image(link):
	if link in images:
		return images[link]

	req = Request(link, None, {}, None, None, 'GET')

	try:
		response = urlopen(req)
	except URLError as e:
		return e.code

	images[link] = response.read()
	return images[link]
