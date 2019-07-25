#!/usr/bin/env python2
import Adafruit_DHT
import MySQLdb
import time
time.sleep(60)
sensor = Adafruit_DHT.DHT22
pin=9
db=MySQLdb.connect("localhost", "root", "Notre_jardin_est_le_paradis.","bewaesserung")
curs=db.cursor()
while (True):
	try:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		curs.execute("INSERT INTO humidity (id,timestamp,value) VALUES(NULL,NOW() , %.2f);" %humidity)
		db.commit()
		curs.execute("INSERT INTO temperature (id,timestamp,value) VALUES (NULL,NOW(),%.2f);" %temperature)
		db.commit()
		#print("Done")
	except Exception as e:
		#print("Error. Rolling back. "+str(e))
		db.rollback()
	time.sleep(60*60)

