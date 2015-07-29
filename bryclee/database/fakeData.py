#For sample json object
import json, os

with open(os.path.join(os.path.dirname(__file__), 'fakePosts.json')) as f:
	jsonData = json.load(f)
