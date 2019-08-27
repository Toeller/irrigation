

#
# Setup
#
def setup():

	GPIO.setmode(GPIO.BCM)

	RIN0 = 23
	RIN1 = 24
	RIN2 = 25
	RIN3 = 12
	RIN4 = 16
	RIN5 = 20
	RIN6 = 21
	RIN7 = 22

	pumpe   = RIN0
	ventil1 = RIN1
	ventil2 = RIN2
	ventil3 = RIN3
	ventil4 = RIN4
	ventil5 = RIN5
	ventil6 = RIN6
	ventil7 = RIN7

	GPIO.setup(RIN0, GPIO.OUT)
	GPIO.setup(RIN1, GPIO.OUT)
	GPIO.setup(RIN2, GPIO.OUT)
	GPIO.setup(RIN3, GPIO.OUT)
	GPIO.setup(RIN4, GPIO.OUT)
	GPIO.setup(RIN5, GPIO.OUT)
	GPIO.setup(RIN6, GPIO.OUT)
	GPIO.setup(RIN7, GPIO.OUT)
