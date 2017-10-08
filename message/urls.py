from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^(?P<user_id>\d+)/$',views.message,name='message'),
	url(r'^message_privacy/$',views.message_privacy,name='message_privacy'),
	url(r'^delete/(?P<user_id>\d+)/(?P<message_id>\d+)/$',views.message_delete,name='message_delete'),
]