import RPi.GPIO as GPIO
import time
from datetime import datetime
import irrigationsetup
import time


irrigationsetup.setup()
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
while datetime.now().strftime('%d.%m.%Y %H:%M')!=startDateTime.strftime('%d.%m.%Y %H:%M'):
        print (datetime.now())
        time.sleep(1)
print("AN")
GPIO.output(pumpe, GPIO.LOW)

while datetime.now().strftime('%d.%m.%Y %H:%M')!=stopDateTime.strftime('%d.%m.%Y %H:%M'):
        print(datetime.now())
        time.sleep(1)

print("Aus")
GPIO.output(pumpe, GPIO.HIGH)




GPIO.cleanup()
print("Bye!")
