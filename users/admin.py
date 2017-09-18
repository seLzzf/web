from django.contrib import admin
from users.models import Userinfo,YZM,Follower

class UserinfoAdmin(admin.ModelAdmin):
	list_display=('user','sex','birthday')
	search_fields=('user',)
admin.site.register(Userinfo,UserinfoAdmin)

class YZMAdmin(admin.ModelAdmin):
	list_display=('user','yzm')
	search_fields=('user',)
admin.site.register(YZM,YZMAdmin)

class FollowerAdmin(admin.ModelAdmin):
	list_display=('focus','follower')
	search_fields=('focus','follower',)
admin.site.register(Follower,FollowerAdmin)