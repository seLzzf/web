from django.forms import ModelForm,Textarea,IntegerField,Form,TextInput
from .models import Userinfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model=User
		fields=['username','email']
		
class UserProfileForm(ModelForm):
	class Meta:
		model=Userinfo
		fields=['birthday','sex','school','autograph','pic']
		widgets={
			'school':Textarea(attrs={'rows':3}),
			'autograph':Textarea(attrs={'rows':3}),
		}

class UserProfileForm_read(ModelForm):
	class Meta:
		model=Userinfo
		fields=['birthday','sex','school','autograph']
		widgets={
			'birthday':TextInput(attrs={'readonly':'readonly'}),
			'sex':TextInput(attrs={'readonly':'readonly'}),
			'school':TextInput(attrs={'readonly':'readonly'}),
			'autograph':TextInput(attrs={'readonly':'readonly'}),
		}

class EmailConfirmForm(Form):
	emailnum_input=IntegerField(label='验证码:',min_value=100000,max_value=999999)