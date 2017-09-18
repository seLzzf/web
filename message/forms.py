from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
	class Meta:
		model=Message
		fields=['message','私密留言']
		lables={''}