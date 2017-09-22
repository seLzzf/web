from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
	owner=models.ForeignKey(User)
	title=models.CharField('标题',max_length=15)
	date_added=models.DateTimeField(auto_now_add=True)
	设为私密=models.BooleanField(default=False)
	views=models.PositiveIntegerField(default=0)
	praises=models.PositiveIntegerField(default=0)
	
	def increase_praises(self):
		self.praises+=1
		self.save(update_fields=['praises'])
	def increase_views(self):
		self.views+=1
		self.save(update_fields=['views'])
	def __str__(self):
		return self.title
		
class Note(models.Model):
	title=models.ForeignKey(Theme)#"Note.title" must be a "Theme" instance.
	text=models.TextField('你想说的话...')
	date_added=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title.title
	
