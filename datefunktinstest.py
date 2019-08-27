from datetime import date, time, datetime, timedelta as delta
from Timer import Timer

tim1=datetime.now().time()
#print(tim1)

tim1=tim1.replace(minute=59)
tim1=tim1.replace(hour=23)
#print(tim1)

da1=date.today()-delta(days=0)
#print(da1)

dates=[]
#if dates !=None:
#	for d in dates:
	#	print(d)
#else:
	#print("Kein Datum in der Liste")
	
dates.append(da1)

#if dates !=None:
	#for d in dates:
	#	print("Nach append")
	#	print(d)
#else:
	#print("Kein Datum in der Liste")

#dates=[]
#if dates !=None:
#	for d in dates:
	#	print(d)
#else:
	#print("Kein Datum in der Liste")
print(datetime.now())

t=Timer("Ventilx", date.today()-delta(days=2), tim1, 1, 1, 5)
t.start_date=da1
t.intervall=2
print("Timer")
print("Datum:"+str(t.start_date))
print("Zeit: "+str(t.start_time))
print("Intervall: "+str(t.intervall))
print("Dauer: "+str(t.duration_minutes))



#print((date.today()-t.start_date).days)
#print((date.today()-t.start_date).days%t.intervall)
#print((t.start_time+delta(minutes=t.duration_minutes)).strftime('%H:%M'))
#print("Startzeit: "+str(t.start_time))
#print("Bewaesserungsdauer: "+str(t.duration_minutes))
#t.start_time=(datetime(2000,1,1,t.start_time.hour,t.start_time.minute,t.start_time.second)+delta(minutes=t.duration_minutes)).time()

print("Bewaesserungsdauer in Minuten: 60")
t.start_time=(datetime(2000,1,1,t.start_time.hour,t.start_time.minute,t.start_time.second)+delta(minutes=60)).time()


print ("Neue Stopzeit:"+str(t.start_time))
#print((t.start_time-delta(minutes=t.duration_minutes)))
print("Stopdatum"+str(t.start_date+delta(minutes=t.duration_minutes)))
if (date.today()-(t.start_date+delta(minutes=t.duration_minutes))).days%t.intervall==0: 
	print("Heute stoppen")
else:
	print("Stopdatum:" +str((date.today()-(t.start_date+delta(minutes=t.duration_minutes)))))
