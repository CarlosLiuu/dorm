from django import forms  

class UserForm(forms.Form):  
    username = forms.IntegerField()
	number = forms.IntegerField()
	password = forms.CharField()