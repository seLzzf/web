from django import forms
from .models import Theme,Note

class ThemeForm(forms.ModelForm):
	class Meta:
		model=Theme
		fields=['title','设为私密']
		lables={}


class NoteForm(forms.ModelForm):
	class Meta:
		model=Note
		fields=['text']
		lables={'text':''}
		widgets={'text':forms.Textarea(attrs={'cols':80})}