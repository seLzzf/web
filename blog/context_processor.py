from users.models import Userinfo

def request_userinfo(request):
	user=request.user
	try:
		request_userinfo=Userinfo.objects.get(user=user)
		return {'request_userinfo':request_userinfo}
	except:
		return {'request_userinfo':'请登录.'}