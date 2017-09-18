from django.shortcuts import render
from blogs.models import Theme
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,Http404,HttpResponse
from .forms import CommentForm
from django.core.urlresolvers import reverse

def handle_comment(request,theme_id):
	if request.method=='POST':
		form=CommentForm(data=request.POST)
		if form.is_valid():
			theme=Theme.objects.get(id=theme_id)
			page_user=theme.owner
			page_user_id=page_user.id
			
			comment=form.save(commit=False)
			comment.belong=theme
			comment.publisher=request.user
			comment.save()
			return HttpResponseRedirect(reverse('blogs:theme',args=[page_user_id,theme_id]))
		else:
			return HttpResponse('请输入有效评论')
	else:
		return HttpResponse('你在干什么')