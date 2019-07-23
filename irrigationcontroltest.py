#!/usr/bin/env python2
import RPi.GPIO as GPIO
import time
from datetime import datetime
import time

#Start
onJahr=2019
onMonat=07
onTag= 22
onStunde=18
onMinute=25

#Stop
offJahr=2019
offMonat=07
offTag=22
offStunde=18
offMinute=40


#
# Setup
#

GPIO.setmode(GPIO.BCM)

#GPIO raspberry pi 3b rev1.2
#PIN1:  3v3 Power       #PIN2:  5v Power -> Power Relais
#PIN3:  GPIO2(SDA)   	#PIN4:  5v Power
#PIN5:  GPIO3(SCL)   	#PIN6:  GND		 -> GND Relais
#PIN7:  GPIO4(GPCLK0)   #PIN8:  GPIO14(TXD)
#PIN9:  GND             #PIN10: GPIO15(RXD)
#PIN11: GPIO17          #PIN12: GPIO18 (PCM_CLK)
#PIN13: GPIO27      	#PIN14: GND
#PIN15: GPIO22          #PIN16: GPIO23
#PIN17: 3v3 Power       #PIN18: GPIO24
#PIN19: GPIO10(MOSI)    #PIN20: GND
#PIN20: GPIO9 (MISO)    #PIN22: GPIO25
#PIN23: GPIO11       	#PIN24: GPIO8 (CE0)
#PIN25: GND			   	#PIN26: GPIO7 (CE1)
#PIN27: GPIO0 (ID_SD)	#PIN28: GPIO1 (ID_SC)
#PIN29: GPIO5		    #PIN30: GND
#PIN31: GPIO6           #PIN32: GPIO12
#PIN33: GPIO13          #PIN34: GND
#PIN35: GPIO19      	#PIN36: GPIO16
#PIN37: GPIO22          #PIN38: GPIO20
#PIN39: GND       		#PIN40: GPIO21


RIN0 = 23
RIN1 = 24
RIN2 = 25
RIN3 = 12
RIN4 = 16
RIN5 = 20
RIN6 = 21
RIN7 = 26

pumpe   = RIN0
#ventil1 = RIN1
#ventil2 = RIN2
#ventil3 = RIN3
ventil4 = RIN4
ventil3 = RIN5
ventil2 = RIN6
ventil1 = RIN7

GPIO.setup(RIN0, GPIO.OUT)
GPIO.setup(RIN1, GPIO.OUT)
GPIO.setup(RIN2, GPIO.OUT)
GPIO.setup(RIN3, GPIO.OUT)
GPIO.setup(RIN4, GPIO.OUT)
GPIO.setup(RIN5, GPIO.OUT)
GPIO.setup(RIN6, GPIO.OUT)
GPIO.setup(RIN7, GPIO.OUT)

GPIO.output(ventil1, GPIO.HIGH)
GPIO.output(ventil2, GPIO.HIGH)
GPIO.output(ventil3, GPIO.HIGH)
GPIO.output(ventil4, GPIO.HIGH)
GPIO.output(ventil5, GPIO.HIGH)
GPIO.output(ventil5, GPIO.HIGH)
GPIO.output(ventil6, GPIO.HIGH)
GPIO.output(ventil7, GPIO.HIGH)

#
# Timer
#

t=datetime.now()
startDateTime=datetime(onJahr,onMonat,onTag,onStunde,onMinute,0)
stopDateTime=datetime(offJahr,offMonat,offTag,offStunde,offMinute,0)
print("Aktuell:)
print(t)
#print(t.tzinfo)
print("Start:")
print (startDateTime)
print("Stop:")
print(stopDateTime)
#print(t.tzinfo,t.tzinfo.utcoffset(t))

while(True):
	while datetime.now().strftime('%H:%M')!=startDateTime.strftime('%H:%M'):
		print (datetime.now())
        time.sleep(10)
		
	print("AN")
	GPIO.output(pumpe, GPIO.LOW)
	time.sleep(30)
	GPIO.output(ventil1, GPIO.LOW)

	while datetime.now().strftime('%H:%M')!=stopDateTime.strftime('%H:%M'):
        print(datetime.now())
        time.sleep(10)
	
	GPIO.output(ventil1, GPIO.HIGH)
	time.sleep(60)
	GPIO.output(pumpe, GPIO.HIGH)
	print("Aus")


GPIO.cleanup()
print("Bye!")
