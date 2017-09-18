from django.contrib import admin
from comments.models import Comment

class CommentAdmin(admin.ModelAdmin):
	list_display=('belong','publisher','date_added')
	search_fields=('belong',)
	
admin.site.register(Comment,CommentAdmin)