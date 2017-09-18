from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^(?P<user_id>\d+)/$',views.message,name='message'),
	url(r'^message_privacy/$',views.message_privacy,name='message_privacy'),
]