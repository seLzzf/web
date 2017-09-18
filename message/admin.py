from django.contrib import admin
from message.models import Message,To_Message

class To_MessageAdmin(admin.ModelAdmin):
	list_display=('owner','设为私密')
	search_fields=('owner',)
	
admin.site.register(To_Message,To_MessageAdmin)

class MessageAdmin(admin.ModelAdmin):
	list_display=('giver','date_added')
	search_fields=('giver',)
	
admin.site.register(Message,MessageAdmin)