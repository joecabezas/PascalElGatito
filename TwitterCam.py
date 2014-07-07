from twython import Twython
import subprocess

from twitter_data import APP_KEY
from twitter_data import APP_SECRET
from twitter_data import OAUTH_TOKEN
from twitter_data import OAUTH_TOKEN_SECRET

class TwitterCam(object):
	def __init__(self, a_animated):
		self.twitter_obj = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		self.animated = a_animated
	
	@property
	def command(self):
		command = 'sh take_picture.sh'.split()
		if self.animated:
			command.append('-a')
		return command

	@property
	def fileName(self):
		if self.animated:
			return 'output.gif'
		else:
			return 'output.jpg'
	    	
	def tweet(self):
		subprocess.check_output(self.command)
		ouputFile = open(self.fileName, 'rb')
		self.twitter_obj.update_status_with_media(status='Testing: using rPi GPIO input (animated:'+str(self.animated)+')', media=ouputFile)
		print "done uploading!"

	def test(self):
		print self.command;
		#print self.twitter_obj.verify_credentials()
		#print APP_KEY
		#self.twitter_obj.update_status(status='Test debug')