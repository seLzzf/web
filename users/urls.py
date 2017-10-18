from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns=[
	url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
	url(r'^logout/$',views.logout_views,name='logout'),
	url(r'^register/$',views.register,name='register'),
	url(r'^some_works/$',views.some_works,name='some_works'),
	url(r'^register_confirm/$',views.register_confirm,name='register_confirm'),
	url(r'^userinfo/(?P<user_id>\d+)/$',views.userinfo,name='userinfo'),
	url(r'^news/$',views.news,name='news'),
	url(r'^user_ff_list/(?P<user_id>\d+)/',views.ff_list,name='ff_list'),
	url(r'^alterinfo/$',views.alterinfo,name='alterinfo'),
	url(r'^regsuc/$',views.regsuc,name='regsuc'),
	url(r'^follow/(?P<user_id>\d+)/$',views.follow,name='follow'),
	url(r'^favorite_list/(?P<user_id>\d+)/$',views.favorite_list,name='favorite_list'),
	
]