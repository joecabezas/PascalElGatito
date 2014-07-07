from twython import Twython
import subprocess

from twitter_data import APP_KEY
from twitter_data import APP_SECRET
from twitter_data import OAUTH_TOKEN
from twitter_data import OAUTH_TOKEN_SECRET

#create twython object
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#is this take will be animated? (gif)
animated = False

#create command
command = 'sh take_picture.sh'.split()
if animated:
	command.append('-a')
#print command

#excecute command
outputFileName = subprocess.check_output(command)
outputFileName = outputFileName.strip()

#tweet
ouputFile = open(outputFileName, 'rb')
twitter.update_status_with_media(status='Testing '+str(animated), media=ouputFile)

print "done!"
