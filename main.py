import RPi.GPIO as GPIO
import time, sys
from TwitterCam import TwitterCam

PIEZO_SENSOR_INPUT_PIN = 17
PIEZO_BUZZER_OUTPUT_PIN = 18

class Main(object):
	def __init__(self):
		self.setupGPIO()
		pass

	def start(self, a_animated):
		self.animated = a_animated
		self.twitterCam = TwitterCam(self.animated)
		GPIO.add_event_detect(PIEZO_SENSOR_INPUT_PIN, GPIO.RISING, callback=self.callback, bouncetime=60000)

	def setupGPIO(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PIEZO_SENSOR_INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(PIEZO_BUZZER_OUTPUT_PIN, GPIO.OUT)

	def beep(self, freq):
		p = GPIO.PWM(PIEZO_BUZZER_OUTPUT_PIN, freq)

		p.start(50)
		time.sleep(0.1)
		p.stop()

		time.sleep(0.03)

		p.start(50)
		p.ChangeFrequency(freq)
		time.sleep(0.1)
		p.stop()

	def callback(self, channel):
		print("Button on channel "+str(PIEZO_SENSOR_INPUT_PIN)+" pressed")
		self.beep(700)
		self.twitterCam.tweet();
		self.beep(900)

	def test(self, channel):
		print 'test'

	def exit(self):
		GPIO.cleanup()
		print "bye! :D"
		sys.exit()

main = Main()
main.beep(600)
main.start(True)

try:
	while True:
		pass
except (KeyboardInterrupt, SystemExit):
	main.exit()