from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urlencode

from flask import make_response

def imgurRequest(path):
	req = Request('https://i.imgur.com/' + path, None, {}, None, None, 'GET')

	try:
		response = urlopen(req)
	except URLError as e:
		return e.code

	return response.read()
