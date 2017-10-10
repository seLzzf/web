from django.db import models

class Notes(models.Model):
	title=models.CharField('标题',max_length=30)
	text=models.TextField('正文')
	date_setup=models.DateTimeField(auto_now_add=True)
	views=models.PositiveIntegerField(default=0)

	def increase_views(self):
		self.views+=1
		self.save(update_fields=['views'])
	def __str__(self):
		return self.title
