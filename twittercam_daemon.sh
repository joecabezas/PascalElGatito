#!/bin/sh

#create a symbolic link to this file in /etc/init.d/
#more info at:
#http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html

DAEMON_NAME="TwitterCam"

case "$1" in
	start)
		echo "Starting $DAEMON_NAME"
		# run application you want to start
		/usr/bin/python /home/pi/git/PascalElGatito/main.py
		;;
	stop)
		echo "Stopping $DAEMON_NAME"
		# kill application you want to stop
		killall noip2
		;;
	*)
		echo "Usage: $0 {start|stop}"
		exit 1
		;;
esac

exit 0