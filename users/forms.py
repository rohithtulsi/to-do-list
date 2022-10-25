from logging import PlaceHolder
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'This already exists!'})
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control'}))	
	
	class Meta:
		model = User
		fields = ("username",'email', "password1", "password2")
		required_fields = ["username", "password1", "password2"]

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

	def clean_email(self):
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError(self.fields['email'].error_messages['exists'])
		return self.cleaned_data['email']