#!/usr/bin/env python
from flask import Flask,request,render_template
import Adafruit_DHT
import MySQLdb

app = Flask(__name__)

@app.route('/')

def index():
	humidity,temperatur=Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,9)
	result='Salut jardiniers et jardinieres <br>'
	result+='humidite relative:'+str(humidity)+'<br>'
	result+='temperature Celsius:'+str(temperatur)+'<br>'
	return result

@app.route('/pilotage')
def pilotage():
	result='Les programmes:<br>'
	db=MySQLdb.connect("localhost","root","Notre_jardin_est_le_paradis.","bewaesserung")
	curs=db.cursor()
	curs.execute("SELECT * from schedule;");
	for entry in curs.fetchall():
		result+="nom:{0}<br> demarage:{1}<br> l tous les {2} jours<br> duree: {3}".format(entry[1], entry[2], entry[3],entry[4])
		result+="<br>"
	return result

@app.route('/programmes')
def programmes():
	templateData={
		'v1_start':'2019-07-25',
		'v1_frequency':'2',
		'v1_time':'19:15',
		'v1_duration':'15'
	}
	return render_template('programmes.html',**templateData)

if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0',port=80)
