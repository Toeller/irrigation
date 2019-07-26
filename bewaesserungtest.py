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


GPIO.setmode(GPIO.BCM)

RIN1=23
RIN2=24
RIN3=25
RIN4=12
RIN5=16
RIN6=20
RIN7=21
RIN8=26


ventil1=RIN8
ventil2=RIN7
ventil3=RIN5
ventil4=RIN4
pumpe=RIN1

GPIO.setup(RIN8, GPIO.OUT)
GPIO.setup(RIN1, GPIO.OUT)
GPIO.setup(RIN2, GPIO.OUT)
GPIO.setup(RIN3, GPIO.OUT)
GPIO.setup(RIN4, GPIO.OUT)
GPIO.setup(RIN5, GPIO.OUT)
GPIO.setup(RIN6, GPIO.OUT)
GPIO.setup(RIN7, GPIO.OUT)

GPIO.output(pumpe, GPIO.HIGH)
GPIO.output(ventil1,GPIO.HIGH)
GPIO.output(ventil2, GPIO.HIGH)
GPIO.output(ventil3, GPIO.HIGH)
GPIO.output(ventil4, GPIO.HIGH)

#
# Timer
#

t=datetime.now()
startDateTime=datetime(onJahr,onMonat,onTag,onStunde,onMinute,0)
stopDateTime=datetime(offJahr,offMonat,offTag,offStunde,offMinute,0)
print("Aktuell:")
print(t)
#print(t.tzinfo)
print("Start:")
print(startDateTime)
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
