from django.contrib import admin
from .models import Notes

class NotesAdmin(admin.ModelAdmin):
	list_display=('title','date_setup')
	search_fields=('title','date_setup',)

admin.site.register(Notes,NotesAdmin)