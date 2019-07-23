import RPi.GPIO as GPIO
import time
from datetime import datetime
import time

#Start
onJahr=2019
onMonat=07
onTag=03
onStunde=07
onMinute=45

#Stop
offJahr=2019
offMonat=07
offTag=03
offStunde=07
offMinute=50


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

#
# Timer
#

t=datetime.now()
startDateTime=datetime(onJahr,onMonat,onTag,onStunde,onMinute,0)
stopDateTime=datetime(offJahr,offMonat,offTag,offStunde,offMinute,0)
print(t)
#print(t.tzinfo)
print(startDateTime)
print(stopDateTime)
#print(t.tzinfo,t.tzinfo.utcoffset(t))
while datetime.now().strftime('%d.%m.%Y %H:%M')!=startDateTime.strftime('%d.%m.%$
        print (datetime.now())
        time.sleep(1)
print("AN")
GPIO.output(pumpe, GPIO.LOW)

while datetime.now().strftime('%d.%m.%Y %H:%M')!=stopDateTime.strftime('%d.%m.%Y$
        print(datetime.now())
        time.sleep(1)

print("Aus")
GPIO.output(pumpe, GPIO.HIGH)



#GPIO.setup(ventil1, GPIO.OUT)
#GPIO.setup(ventil2, GPIO.OUT)
#GPIO.setup(ventil3, GPIO.OUT)
#GPIO.setup(ventil4, GPIO.OUT)
#GPIO.setup(ventil5, GPIO.OUT)
#GPIO.setup(ventil6, GPIO.OUT)
#GPIO.setup(ventil7,  GPIO.OUT)

#LOW=EIN!!
#GPIO.output(ventil1, GPIO.LOW)
#GPIO.output(ventil2, GPIO.LOW)
#GPIO.output(ventil3, GPIO.LOW)
#GPIO.output(ventil4, GPIO.LOW)
#GPIO.output(ventil5, GPIO.LOW)
#GPIO.output(ventil5, GPIO.LOW)
#GPIO.output(ventil6, GPIO.LOW)
#GPIO.output(ventil7, GPIO.LOW)

#time.sleep(1)

#GPIO.output(pumpe, GPIO.HIGH)
#time.sleep(1)
GPIO.cleanup()
print("Bye!")
