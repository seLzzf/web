from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

urlpatterns=[
	url(r'^$',login,{'template_name':'users/login.html'},name='login'),
	url(r'^index/$',views.index,name='index'),
	# url(r'^index/$',login_required(views.IndexView.as_view()),name='index'),
	url(r'^themes/(?P<user_id>\d+)/$',views.themes,name='themes'),
	# url(r'^themes/(?P<user_id>\d+)/$',views.ThemesView.as_view(),name='themes'),
	url(r'^themes/(?P<user_id>\d+)/(?P<theme_id>\d+)/$',views.theme,name='theme'),
	url(r'^new_theme/$',views.new_theme,name='new_theme'),
	url(r'^new_note/(?P<theme_id>\d+)/$',views.new_note,name='new_note'),
	url(r'^delete_theme/(?P<theme_id>\d+)/$',views.delete_theme,name='delete_theme'),
	url(r'^delete_note/(?P<theme_id>\d+)/(?P<note_id>\d+)/$',views.delete_note,name='delete_note'),
	url(r'^(?P<theme_id>\d+)/privacy/$',views.privacy,name='privacy'),
	url(r'^search/$',views.search,name='search'),
	url(r'^themes/(?P<user_id>\d+)/(?P<theme_id>\d+)/give_praise/$',views.give_praise,name='give_praise'),
	url(r'^themes/(?P<user_id>\d+)/(?P<theme_id>\d+)/get_favorite/$',views.get_favorite,name='get_favorite'),
	url(r'^test/$',views.test,name='test'),
]