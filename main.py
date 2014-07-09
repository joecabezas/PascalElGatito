import RPi.GPIO as GPIO
import time, sys
from TwitterCam import TwitterCam

PIEZO_SENSOR_INPUT_PIN = 17
PIEZO_BUZZER_OUTPUT_PIN = 18

class Main(object):
	def __init__(self, a_animated):
		self.animated = a_animated
		self.twitterCam = TwitterCam(self.animated)
		self.setupGPIO()
		
	def setupGPIO(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PIEZO_SENSOR_INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(PIEZO_BUZZER_OUTPUT_PIN, GPIO.OUT)
		GPIO.add_event_detect(PIEZO_SENSOR_INPUT_PIN, GPIO.RISING, callback=self.callback, bouncetime=10000)

	def beep(self):
		p = GPIO.PWM(PIEZO_BUZZER_OUTPUT_PIN, 440)  # channel=12 frequency=50Hz
		p.start(0)
		p.ChangeDutyCycle(50)
		time.sleep(0.2)
		p.stop()

	def callback(self, channel):
		print("Button on channel "+str(PIEZO_SENSOR_INPUT_PIN)+" pressed")
		self.beep()
		self.twitterCam.tweet();

	def test(self, channel):
		print 'test'

try:
	main = Main(True)
	while True:
		pass
except (KeyboardInterrupt, SystemExit):
	GPIO.cleanup()
	print "bye! :D"
	sys.exit()