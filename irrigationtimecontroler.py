import time
from datetime import datetime, date, timedelta as delta
from datetime import date
from irrigationmodel import irrigationmodel

irrigationmodel1=irrigationmodel()


a=1
while (True):
	for n in range(1,8):
		#print("Ueberpruefe Ventil:"+str(n))
		if(irrigationmodel1.gettimer(a) !=None):
			for t in irrigationmodel1.gettimer(a):
				print("Timer vorhanden fuer Ventil"+str(a)+".")
				print(t.start_date)
				print("Startzeit:")
				print(t.start_time)
				if t.modus.daily:
					print("Modus daily")
					if (date.today()-t.start_date).days%t.intervall==0:
						if datetime.now().strftime('%H:%M')==t.start_time.strftime('%H:%M'):
							irrigationmodel1.setstate(n,True)
					#if (date.today()-t.start_date#plusBewaesserungszeit#).days%t.intervall==0: 
					#Problem: Bewaesserung startet um 23:59 für 5Min... -> Neues Datum, wird nicht ausgeschaltet...
						stoptime=(datetime(2000,1,1,t.start_time.hour,t.start_time.minute,t.start_time.second)+delta(minutes=t.duration_minutes)).time()
						if datetime.now().strftime('%H:%M')==stoptime.strftime('%H:%M'):
							irrigationmodel1.setstate(n,False)
		a=a+1
	a=1
	time.sleep(10)
	
			#elif timer.modus.weekly:
				
			#elif timer.modus.monthly:
				
			#elif timer.modus.weekdaily:
				
			#elif timer.modus.hourly:
			#	time.now()
				
			#==datetime.now().strftime('%d.%m.%Y %H:%M')
			#	irrigationmodel.changestate(n,1)
				#print(datetime.now())
				#print(n)
				#print("An")
					

