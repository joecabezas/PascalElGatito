#!/bin/sh

while getopts "a" opt; do
	case $opt in
		a)
			ANIMATED=true
			;;
	esac
done

#VALORES POR DEFECTO
if [ -z "$ANIMATED" ]; then ANIMATED=false; fi

###########
#EXECUTION#
###########

OUTPUT_FILE_ANIMATED="output.gif"
OUTPUT_FILE="output.jpg"

take_animated()
{
	#take screenshots
	ffmpeg \
		-r 10 \
		-f video4linux2 \
		-i /dev/video0 \
		-vf scale=320:-1 \
		-t 3 \
		-vcodec gif \
		video%03d.jpg

	#converto screenshots to gif
	convert \
		-delay 10 \
		-loop 0 \
		video*.jpg \
		$OUTPUT_FILE_ANIMATED

	#remove screenshots
	rm -r video*.jpg
}

take_photo()
{
	fswebcam \
		-r 640x480 \
		--jpeg 80 \
		--no-banner \
		$OUTPUT_FILE
}

#make target dir
if "$ANIMATED"; then
	take_animated
else
	take_photo
fi