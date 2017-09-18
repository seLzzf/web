from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from users.models import Follower
from blogs.models import Theme
from django.contrib.auth.models import User

@login_required
def action(request,user_id):
	page_user=request.user
	Followers=Follower.objects.filter(follower=page_user)#一个查询集内，N个元素
	themes=[]
	n=0
	for people in Followers:
		owner=people.focus
		if n==0:
			themes.append(Theme.objects.filter(owner=owner))
		else:
			themes.append(Theme.objects.filter(owner=owner))
			themes[n]=themes[n]|themes[n-1]
		n+=1
	try:
		themes=themes[n-1].order_by('date_added')
	except:
		return HttpResponse('no focus')
		
	context={'page_user':page_user,'themes':themes}
	return render(request,'action/action.html',context)