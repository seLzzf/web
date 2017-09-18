from django.db import models
from django.contrib.auth.models import User

class To_Message(models.Model):
	owner=models.OneToOneField(User)
	to_message=models.TextField(default='留言板')
	设为私密=models.BooleanField(default=False)
	def __str__(self):
		return self.to_message
class Message(models.Model):
	t_m=models.ForeignKey(To_Message)
	giver=models.ForeignKey(User)
	message=models.TextField('写留言:')
	date_added=models.DateTimeField(auto_now_add=True)
	私密留言=models.BooleanField(default=False)
	def __str__(self):
		return self.message

