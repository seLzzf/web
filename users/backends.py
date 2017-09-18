from django.contrib.auth.models import User

class EmailBackend(object):
	def authenticate(self,request,**credentials):
		email=credentials.get('email',credentials.get('username'))
		try:
			user=User.objects.get(email=email)
		except:
			pass
		else:
			if user.check_password(credentials['password']):
				return user

	def get_user(self,user_id):
		try:
			return User.objects.get(pk=user_id)
		except:
			return None
		