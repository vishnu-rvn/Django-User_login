from django import forms
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'text','placeholder':'Password'}), label='')
    username = forms.CharField(widget = forms.TextInput(attrs = {'class':'text','placeholder':'Username'}), label='')
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'class':'text','placeholder':'First Name'}), label='')
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'class':'text','placeholder':'Last Name'}), label='')
    email = forms.CharField(widget = forms.EmailInput(attrs = {'class':'text','placeholder':'E-mail'}), label='')
    class Meta():
        model = User
        fields = ('username','password','first_name','last_name','email')
