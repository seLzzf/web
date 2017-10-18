from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate 
from .models import Userinfo,YZM,Follower,News,Favorites
from blogs.models import Theme
from django.contrib.auth.models import User
from .forms import UserForm,UserProfileForm,EmailConfirmForm,UserProfileForm_read
from PIL import Image
import random,sys,io
from django.core.mail import send_mail
#coding=utf-8

def Storage_pic(request):
	name=request.user.id+'.jpg'
	with open(name,'wb') as pic:
		pic.write(request.FILES['picture'].content)
		pic.close
		return pic
		
def logout_views(request):
	logout(request)
	return HttpResponseRedirect(reverse('blogs:login'))
def register(request):
	if request.method!='POST':
		user_form=UserForm()
		profile_form=UserProfileForm()
	else:
		user_form=UserForm(data=request.POST)
		if user_form.is_valid():
			user=user_form.save()
			user.is_active=False
			user.save()
			
			email=request.POST.get('email')
			email_num=random.randint(100000,999999)
			Userinfo.objects.create(user=user)
			user_id=user.id
			try:
				send_mail('欢迎注册zz的网站','欢迎注册zz的网站,您的注册验证码是: '+str(email_num)+' .','271938333@qq.com',[email],fail_silently=False)
			except:
				user.delete()
				return HttpResponse('some errors')
			YZM.objects.create(user=user,yzm=email_num)
			form=EmailConfirmForm()
			context={'user_id':user_id,'form':form}
			return render(request,'users/register_confirm.html',context)
		else:
			print('some errors')
	context={'user_form':user_form}
	return render(request,'users/register.html',context)
def register_confirm(request):
	if request.method=='POST':
		yzm=request.POST.get('emailnum_input')
		user_id=request.POST.get('user_id')
		user=User.objects.get(id=user_id)
		YZM_obj=YZM.objects.get(user=user)
		email_num=YZM_obj.yzm
		if yzm==str(email_num):
			user.is_active=True
			user.save()
			YZM_obj.delete()
			return HttpResponseRedirect(reverse('users:regsuc'))
		else:
			user.delete()
			return HttpResponse('验证码有误，请检查输入，或重新发送。')
def some_works(request):
	root=sys.path[0]+'/users/map_list.txt'
	lists=[]
	with open(root,'r',encoding='utf-8') as f:
		str_all=f.readlines()
		f.close()
	for str in str_all:
		list=str.split(',')
		lists.append(list)
	context={'lists':lists}
	return render(request,'users/some_works.html',context)
def userinfo(request,user_id):
	page_user=User.objects.get(id=user_id)
	themes=Theme.objects.filter(owner=page_user)
	page_userinfo=Userinfo.objects.get(user=page_user)
	info_read_form=UserProfileForm_read(instance=page_userinfo)
	followers=Follower.objects.filter(focus=page_user)
	focusers=Follower.objects.filter(follower=page_user)
	favorites=Favorites.objects.filter(user=page_user)
	try:
		the_follower=Follower.objects.get(focus=page_user,follower=request.user)
	except:
		the_follower=False
	context={'page_user':page_user,'themes':themes,'page_userinfo':page_userinfo,'info_read_form':info_read_form,'followers':followers,'the_follower':the_follower,'focusers':focusers,'favorites':favorites}
	return render(request,'users/userinfo.html',context)
def ff_list(request,user_id):
	page_user=User.objects.get(id=user_id)
	if request.GET['f'] == 'focusers':
		focusers=Follower.objects.filter(follower=page_user)
		context={'focusers':focusers,'page_user':page_user}
	elif request.GET['f'] == 'followers':
		followers=Follower.objects.filter(focus=page_user)
		context={'followers':followers,'page_user':page_user}
	else:
		return HttpResponse('some errors')
	return render(request,'users/ff_list.html',context)
def alterinfo(request):
	page_user=request.user
	if request.method!='POST':
		userinfo=Userinfo.objects.get(user=page_user)
		infoform=UserProfileForm(instance=userinfo)
		context={'infoform':infoform,'page_user':page_user}
		return render(request,'users/alterinfo.html',context)
	else:
		userinfo=Userinfo.objects.get(user=page_user)
		form=UserProfileForm(request.POST,request.FILES,instance=userinfo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('blogs:index'))
def news(request):
	page_user=request.user
	news=News.objects.filter(user=page_user)
	news_unread=News.objects.filter(user=page_user,status=True)
	if news_unread:
		for new_unread in news_unread:
			new_unread.status=False
			new_unread.save()
	context={'page_user':page_user,'news':news}
	return render(request,'users/news.html',context)
def regsuc(request):
	return render(request,'users/regsuc.html')
def follow(request,user_id):
	user=request.user
	page_user=User.objects.get(id=user_id)
	try:
		the_follower=Follower.objects.get(focus=page_user,follower=user)
		the_follower.delete()
	except:
		Follower.objects.create(focus=page_user,follower=user)
	return HttpResponseRedirect(reverse('users:userinfo',args=[page_user.id]))
def favorite_list(request,user_id):
	page_user=User.objects.get(id=user_id)
	favorites=Favorites.objects.filter(user=page_user)
	context={'favorites':favorites,'page_user':page_user}
	return render(request,'users/favorite_list.html',context)