from users.models import Userinfo

def request_userinfo(request):
	user=request.user
	request_userinfo=Userinfo.objects.get(user=user)
	return {'request_userinfo':request_userinfo}