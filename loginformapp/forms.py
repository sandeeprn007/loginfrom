from django import forms
from django.contrib.auth.models import User
from loginformapp.models import userprofile,Userpost

class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password')

class user_profileform(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = ('user_img','user_url')

class userpostform(forms.ModelForm):
    class Meta:
        model = Userpost
        fields = '__all__'
         