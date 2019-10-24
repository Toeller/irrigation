from datetime import date, time, datetime
from modus import Modus

class Timer:
	name="leer"
	start_date=date.today()
	start_time=datetime.now().time()
	modus=Modus()
    #intervall=0
	#duration=0


	def __init__(self, name, start_date, start_time, intervall_mode, intervall, duration_mintes):
		self.name = name
		self.start_date = start_date
		self.start_time = start_time
		self.modus.set(intervall_mode)
		self.intervall=intervall
		self.duration_minutes=duration_mintes