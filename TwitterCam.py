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

	def start(self):

		#excecute command
		outputFileName = subprocess.check_output(self.command)
		outputFileName = outputFileName.strip()

		#tweet
		ouputFile = open(outputFileName, 'rb')
		twitter.update_status_with_media(status='Testing '+str(animated), media=ouputFile)

		print "done!"

	def test(self):
		print self.command;
		#twitter.update_status(status='Test debug')