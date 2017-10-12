from django.shortcuts import render
from .models import Notes

def notes(request):
	notes=Notes.objects.all().order_by('-date_setup')
	try:
		note_id=request.GET['note']
		note=Notes.objects.get(id=note_id)
	except:
		note=Notes.objects.get(id=1)
	import markdown
	note.text=markdown.markdown(note.text,extensions=[
						'markdown.extensions.extra',
						'markdown.extensions.codehilite',
						'markdown.extensions.toc',
					])
	context={'notes':notes,'note':note}
	return render(request,'notes/notes.html',context)