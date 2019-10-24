
class Modus:
	daily=False
	weekly=False
	monthly=False
	weekdaily=False
	hourly=False
	
	def __init__(self):
			self.daily=False
	
	def set(self, intervall_mode):
		if intervall_mode==1:
			self.daily=True
		elif intervall_mode==2:
			self.weekly=True
		elif interavall_mode==3:
			self.monthly=True
		elif interavall_mode==4:
			self.weekdaily=True
		elif interavall_mode==5:
			self.hourly=True