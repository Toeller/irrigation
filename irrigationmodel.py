from Timer import Timer
from datetime import date, time, datetime, timedelta as delta
class irrigationmodel:

	
	tim1=datetime.now().time()
	tim1=tim1.replace(minute=36)
	tim2=datetime.now().time()
	tim2=tim2.replace(minute=37)

	timer1=Timer("Ventil1", date.today()-delta(days=2), tim1, 1, 1, 2)
	timer2=Timer("Ventil2", date.today()-delta(days=3), tim2, 1, 3, 3)
	timers=[]
	def gettimer(self,n):
		#get starttimes for n from database
		# db: bewaesserung (->irrigation)
		#	schedule
		#		schedule_id (int), name (str),start_date (date), start_time(time), intervall_mode(int), interavall(int), duration_minutes(int)
		#	=>select * from bewaesserung wherer name="Ventil"+n
	
		#	
		#add each time to an array
		
		#timers.append(timer1)
		#timers.append(timer2)
		if n==1:
			self.timers=[]
			self.timers.append(self.timer1)
		elif n==2:
			self.timers=[]
			self.timers.append(self.timer2)
		else:
			self.timers=None
			
		#if self.timers != None:
			#print("Versandkontrolle")
			#for t in self.timers:
			#	print("tim")
			#	print(self.tim1)
			#	print(t.start_date)
			#	print(t.start_time)
			#print("Ende der Versandkontrolle")
		return self.timers
	
	def setstate(self,number,state):
		#set state of number  to state
		print("Set State")
		print(datetime.now())
		print("Ventil:")
		print(number)
		print(state)

