from django.shortcuts import render
from .models import To_Message,Message
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import MessageForm

def message(request,user_id):
	page_user=User.objects.get(id=user_id)
	request_user=request.user
	try:
		T_M=To_Message.objects.get(owner=page_user)
	except:
		T_M=To_Message(owner=page_user,to_message='留言板',设为私密='False')
		T_M.save()
	if request.method=='POST':
		form=MessageForm(data=request.POST)
		if form.is_valid():
			new_message=form.save(commit=False)
			new_message.t_m=T_M
			new_message.giver=request_user
			new_message.save()
			return HttpResponseRedirect(reverse('message:message',args=[page_user.id]))
	else:
		if request_user==page_user:
			messages=Message.objects.filter(t_m=T_M)
		elif T_M.设为私密==True:
			return HttpResponse('你没有访问权限')
		else:
			message1=Message.objects.filter(t_m=T_M,私密留言=False)
			message2=Message.objects.filter(t_m=T_M,私密留言=True,giver=request_user)
			messages=message1|message2
		message_form=MessageForm
		context={'request_user':request_user,'page_user':page_user,'T_M':T_M,'messages':messages,'message_form':message_form}
		return render(request,'message/message.html',context)
		
def message_privacy(request,):
	user=request.user
	T_M=To_Message.objects.get(owner=user)
	if T_M.设为私密:
		T_M.设为私密=False
		T_M.save()
	else:
		T_M.设为私密=True
		T_M.save()
	context={'page_user':user,}
	return render(request,'blogs/privacysuc.html',context)