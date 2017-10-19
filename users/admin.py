from django.contrib import admin
from users.models import Userinfo,YZM,Follower,News,Favorites

class UserinfoAdmin(admin.ModelAdmin):
	list_display=('user','sex','birthday')
	search_fields=('user',)
admin.site.register(Userinfo,UserinfoAdmin)

class YZMAdmin(admin.ModelAdmin):
	list_display=('email','yzm')
	search_fields=('email',)
admin.site.register(YZM,YZMAdmin)

class FollowerAdmin(admin.ModelAdmin):
	list_display=('focus','follower')
	search_fields=('focus','follower',)
admin.site.register(Follower,FollowerAdmin)

class NewsAdmin(admin.ModelAdmin):
	list_display=('user','status')
	search_fields=('user','status',)
admin.site.register(News,NewsAdmin)

class FavoriteAdmin(admin.ModelAdmin):
	list_display=('user','theme')
	search_fields=('user','theme',)
admin.site.register(Favorites,FavoriteAdmin)