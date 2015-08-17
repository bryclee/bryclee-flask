"""I wanted to create a very basic proxy"""
from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urlencode

from flask import make_response

images = {}

#Gets the image at the requested path from imgur, cache result in a dict
def imgurRequest(path):
	if path in images:
		return images[path]

	req = Request('https://i.imgur.com/' + path, None, {}, None, None, 'GET')

	try:
		response = urlopen(req)
	except URLError as e:
		return e.code

	images[path] = response.read()
	return images[path]
