from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns=[
	url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
	url(r'^logout/$',views.logout_views,name='logout'),
	url(r'^register/$',views.register,name='register'),
	url(r'^register_confirm/$',views.register_confirm,name='register_confirm'),
	#url(r'^userpage/(?P<user_id>\d+)/$',views.userpage,name='userpage'),
	url(r'^userinfo/(?P<user_id>\d+)/$',views.userinfo,name='userinfo'),
	url(r'^alterinfo/(?P<user_id>\d+)/$',views.alterinfo,name='alterinfo'),
	url(r'^regsuc/$',views.regsuc,name='regsuc'),
	url(r'^follow/(?P<user_id>\d+)/$',views.follow,name='follow'),
]