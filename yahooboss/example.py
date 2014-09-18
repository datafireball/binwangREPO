# I am using the anaconda Python with comes with oauth2 I guess?

OAUTH_CONSUMER_KEY = ""
OAUTH_CONSUMER_SECRET = ""
import urllib2
import oauth2 as oauth
import time
import httplib
# Set HTTP to 1.0 protocol so it can avoid the server side error incomplete read
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'


def oauth_request(url, params, method="GET"):
    # Removed trailing commas here - they make a difference.
    params['oauth_version'] = "1.0" #,
    params['oauth_nonce'] = oauth.generate_nonce() #,
    params['oauth_timestamp'] = int(time.time())
    consumer = oauth.Consumer(key=OAUTH_CONSUMER_KEY,
                              secret=OAUTH_CONSUMER_SECRET)
    params['oauth_consumer_key'] = consumer.key
    req = oauth.Request(method=method, url=url, parameters=params)
    req.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, None)
    return req


if __name__ == "__main__":
    url = "http://yboss.yahooapis.com/ysearch/web"

    req = oauth_request(url, params={"q": "cats dogs"})
    req['q'] = req['q'].encode('utf8')
    req_url = req.to_url().replace('+', '%20')
    print req_url
    result = urllib2.urlopen(req_url)
    print result
    print result.read()
    
#     try:
#         page = urllib2.urlopen(urls).read()
#     except httplib.IncompleteRead, e:
#         page = e.partial
