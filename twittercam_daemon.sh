#!/bin/sh
### BEGIN INIT INFO
# Provides:          TwitterCam
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
# Description:       A simple script from www.stuffaboutcode.com which will start / stop a program a boot / shutdown.
### END INIT INFO

#create a symbolic link to this file in /etc/init.d/
#more info at:
#http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html

DAEMON_NAME="TwitterCam"

case "$1" in
	start)
		echo "Starting $DAEMON_NAME"
		# run application you want to start
		cd /home/pi/git/PascalElGatito/
		/usr/bin/python /home/pi/git/PascalElGatito/main.py &
		;;
	stop)
		echo "Stopping $DAEMON_NAME"
		#stop application
		#TODO
		;;
	*)
		echo "Usage: $0 {start|stop}"
		exit 1
		;;
esac

exit 0