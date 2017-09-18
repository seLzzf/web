from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^comment/(?P<theme_id>\d+)$',views.handle_comment,name='handle_comment'),
]