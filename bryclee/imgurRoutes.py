from bryclee import app
from flask import render_template
from bryclee.imgur import get_imgur_data, get_imgur_image
from imgurpython.helpers.error import ImgurClientError

#Add routes to the app
@app.route('/mirror/<path>', methods=['GET'])
def mirrors(path):
  try:
    imgurData = get_imgur_data(path)
  except ImgurClientError as e:
    error = {'statusCode': e.status_code, 'message': e.error_message}
    return render_template('error.html', error=error)

  return render_template('mirror.html', data=imgurData)

@app.route('/image/<path>', methods=['GET'])
def image(path):
  return get_imgur_image(path)
