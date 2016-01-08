from config import APP_ID, APP_SECRET, SCOPE, COOKIES, REQ_PARAMS

from facepy import GraphAPI
from flask import Flask
import subprocess
import urllib
import urlparse
import warnings

app = Flask(__name__)

@app.route('/getAccessToken', methods=['GET'])
def getAccessToken():
    oauth_args = dict(client_id     = APP_ID,
                      client_secret = APP_SECRET,
                      grant_type    = 'client_credentials')
    oauth_curl_cmd = ['curl',
                      'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
    oauth_response = subprocess.Popen(oauth_curl_cmd,
                                      stdout = subprocess.PIPE,
                                      stderr = subprocess.PIPE).communicate()[0]

    try:
        oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
        return oauth_access_token
    except KeyError:
        return 'Unable to grab an access token!'

@app.route('/recognize', methods=['POST'])
def recognize():
    pass

if __name__ == '__main__':
    app.run(debug=True)