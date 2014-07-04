from twython import Twython

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#print twitter.verify_credentials()
#print twitter.get_home_timeline()[0]['text']
#twitter.update_status(status='first tweet from python')

photo = open('image3.jpg', 'rb')
twitter.update_status_with_media(status='Probando tweets con fotos! :3 miau', media=photo)