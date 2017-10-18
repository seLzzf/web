from django.db import models
from django.contrib.auth.models import User
from blogs.models import Theme

class Userinfo(models.Model):
	user=models.OneToOneField(User)
	pic=models.ImageField(upload_to='images',default='images/default.jpg',verbose_name='头像',blank=True)
	sex=models.CharField('性别',max_length=2,choices=(
	('男','♂'),('女','♀')),blank=True)
	birthday=models.DateField('生日',default='2000-01-01',blank=True)
	school=models.TextField('学校',max_length=50,default='暂未设置所在学校')
	autograph=models.TextField('个性签名',max_length=50,default='暂未设置个性签名')
	
	def __str__(self):
		return self.user.username

class YZM(models.Model):
	user=models.OneToOneField(User)
	yzm=models.IntegerField(blank=True,default=123456)
	
	def __str__(self):
		return str(self.yzm)
		
class Follower(models.Model):
	focus=models.ForeignKey(User,related_name='focus')
	follower=models.ForeignKey(User,related_name='follower',blank=True)
		
class News(models.Model):
	user=models.ForeignKey(User)
	news=models.TextField('消息',blank=True)
	status=models.BooleanField(default=True)
	date_added=models.DateTimeField(auto_now_add=True,blank=True)

class Favorites(models.Model):
	user=models.ForeignKey(User)
	theme=models.ForeignKey(Theme)