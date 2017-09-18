from django.db import models
from blogs.models import Theme
from django.contrib.auth.models import User

class Comment(models.Model):
	belong=models.ForeignKey(Theme)
	message=models.TextField('')
	publisher=models.ForeignKey(User)
	date_added=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.message[:10]