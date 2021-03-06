from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Theme,Note
from users.models import Userinfo,Favorites
from comments.models import Comment
from .forms import NoteForm,ThemeForm
from comments.forms import CommentForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView

@login_required
def index(request):
	try:
		sort=request.GET['sort']
		themes=Theme.objects.filter(设为私密=False).order_by('-'+sort)
	except:
		themes=Theme.objects.filter(设为私密=False).order_by('-date_added')
	page_user=request.user
	context={'themes':themes,'page_user':page_user}
	return render(request,'blogs/index.html',context)

# class IndexView(ListView): #基于类的视图
	# model=Theme
	# template_name='blogs/index.html'
	# context_object_name='themes'
	# def get_queryset(self):
		# try:
			# sort=self.request.GET['sort']
			# return super().get_queryset().filter(设为私密=False).order_by('-'+sort)
		# except:
			# return super().get_queryset().filter(设为私密=False).order_by('-date_added')
	# def get_context_data(self,**kwargs):
		# context=super().get_context_data(**kwargs)
		# page_user=self.request.user
		# context.update({'page_user':page_user})
		# return context

@login_required
def themes(request,user_id):
	request_user=request.user
	page_user=get_object_or_404(User,id=user_id)
	if page_user==request_user:
		themes=Theme.objects.filter(owner=request.user).order_by('date_added')
	else:
		themes=Theme.objects.filter(owner=page_user,设为私密=False).order_by('date_added')
	context={'themes':themes,'page_user':page_user,'request_user':request_user}
	return render(request,'blogs/themes.html',context)
	
# class ThemesView(ListView):    #基于类
	# model=Theme
	# template_name='blogs/themes.html'
	# context_object_name='themes'
	# def get_context_data(self,**kwargs):
		# context=super().get_context_data(**kwargs)
		# request_user=self.request.user
		# page_user=get_object_or_404(User,id=self.kwargs.get('user_id'))
		# if page_user==request_user:
			# themes=Theme.objects.filter(owner=request_user).order_by('date_added') 
		# else:
			# themes=Theme.objects.filter(owner=page_user,设为私密=False).order_by('date_added')
		# context.update({'request_user':request_user,'themes':themes,'page_user':page_user})
		# return context
	
@login_required
def theme(request,user_id,theme_id):
	request_user=request.user
	page_user=get_object_or_404(User,id=user_id)
	theme=get_object_or_404(Theme,id=theme_id)
	theme.increase_views()
	
	if theme.设为私密==True:
		if theme.owner!=request_user:
			return Http404
	notes=Note.objects.filter(title=theme).order_by('date_added')
	
	comment_form=CommentForm()
	comments=theme.comment_set.order_by('date_added')
	#分页:
	    #note
	notes_pages=Paginator(notes,5)
	page_num_notes=request.GET.get('page_n')
	try:
		notes_page=notes_pages.page(page_num_notes)
	except PageNotAnInteger:
		notes_page=notes_pages.page(1)
	except EmptyPage:
		notes_page=notes_pages.page(notes_pages.num_pages)
	    #comment
	comments_pages=Paginator(comments,5)
	page_num_comments=request.GET.get('page_c')
	
	try:
		favorite=Favorites.objects.get(user=request_user,theme=theme)
		is_favo=True
	except:
		is_favo=False
	
	context={'theme':theme,'page_user':page_user,'request_user':request_user,'comments':comments,'notes_page':notes_page,'notes_pages':notes_pages,'comment_form':comment_form,'is_favo':is_favo}
	return render(request,'blogs/theme.html',context)
@login_required
def new_theme(request):
	if request.method!='POST':
		form=ThemeForm()
	else:
		form=ThemeForm(data=request.POST)
		user_id=request.user.id
		if form.is_valid():
			new_theme=form.save(commit=False)
			new_theme.owner=request.user
			new_theme.save()
			return HttpResponseRedirect(reverse('blogs:themes',args=[user_id]))
	page_user=request.user
	context={'form':form,'page_user':page_user}
	return render(request,'blogs/new_theme.html',context)
@login_required
def new_note(request,theme_id):
	theme=Theme.objects.get(id=theme_id)
	if request.method!='POST':
		form=NoteForm()
	else:
		user_id=request.user.id
		form=NoteForm(data=request.POST)
		if form.is_valid():
			new_note=form.save(commit=False)
			new_note.title=theme
			new_note.save()
			return HttpResponseRedirect(reverse('blogs:theme',args=[user_id,theme_id]))
	page_user=request.user
	context={'theme':theme,'form':form,'page_user':page_user}
	return render(request,'blogs/new_note.html',context)
@login_required
def delete_theme(request,theme_id):
	Theme.objects.get(id=theme_id).delete()
	user_id=request.user.id
	return HttpResponseRedirect(reverse('blogs:themes',args=[user_id]))
@login_required
def delete_note(request,theme_id,note_id):
	theme=Theme.objects.get(id=theme_id)
	theme.note_set.get(id=note_id).delete()
	user_id=request.user.id
	return HttpResponseRedirect(reverse('blogs:theme',args=[user_id,theme_id]))
@login_required
def privacy(request,theme_id):
	theme=Theme.objects.get(id=theme_id)
	if theme.设为私密:
		theme.设为私密=False
		theme.save()
	else:
		theme.设为私密=True
		theme.save()
	page_user=request.user
	context={'page_user':page_user}
	return render(request,'blogs/privacysuc.html',context)
@login_required
def search(request):
	page_user=request.user
	search=request.POST.get('search')
	if not search:
		error_msg='请输入关键词'
		return render(request,'blogs/index.html',{'error_msg':error_msg,'page_user':page_user})
	theme_list=Theme.objects.filter(Q(title__icontains=search)).filter(设为私密=False)
	user_list=User.objects.filter(Q(username__icontains=search))
	user_id_list=User.objects.filter(Q(id__icontains=search))
	context={'theme_list':theme_list,'user_list':user_list,'page_user':page_user,'user_id_list':user_id_list}
	return render(request,'blogs/search.html',context)
def give_praise(request,user_id,theme_id):
	if request.is_ajax():
		try:
			theme=Theme.objects.get(id=theme_id)
			theme.increase_praises()
			praises=theme.praises
			return HttpResponse(praises)
		except:
			return HttpResponse('主题不存在')
def get_favorite(request,user_id,theme_id):
	if request.is_ajax():
		user=request.user
		theme=Theme.objects.get(id=theme_id)
		try:
			favorite=Favorites.objects.get(user=user,theme=theme)
			favorite.delete()
			return HttpResponse('取消收藏!')
		except:
			Favorites.objects.create(user=user,theme=theme)
			return HttpResponse('收藏成功!')
	
def test(request):
	user=request.user
	userinfo=Userinfo.objects.get(user=user)
	years=range(1980,2020)
	colors=request.GET.getlist('colors')
	color=request.GET.get('color')
	try:
		user_id=request.GET['user_id']
		user_pass=request.GET['user_pass']
	except:
		user_id=None
	if user_id!=None and user_pass=='123':
		verified=True
	else:
		verified=False
	page_user=request.user
	return render(request,'blogs/test.html',locals())