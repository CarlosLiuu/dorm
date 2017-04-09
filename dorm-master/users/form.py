from django import forms  

class LoginForm(forms.Form):
	username=forms.IntegerField(label='username')
	password=forms.CharField(label='password',widget=forms.PasswordInput())
	num=forms.IntegerField(label='number')