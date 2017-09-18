from django.contrib import admin
from blogs.models import Theme,Note

class ThemeAdmin(admin.ModelAdmin):
	list_display=('title','date_added','owner')
	search_fields=('title',)
class NoteAdmin(admin.ModelAdmin):
	list_display=('title','date_added')
	search_fields=('title',)
	
admin.site.register(Theme,ThemeAdmin)
admin.site.register(Note,NoteAdmin)
