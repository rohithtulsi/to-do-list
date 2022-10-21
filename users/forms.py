from logging import PlaceHolder
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class NewUserForm(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control'}))	
	class Meta:
		model = User
		fields = ("username", "password1", "password2")
		required_fields = ["username", "password1", "password2"]

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user

	def clean(self):	
		cleaned_data = self.cleaned_data
		username = cleaned_data.get('username')

		if username:
			if len(username)<4:
				self.add_error('username', 'Username is too short')
            # You can use ValidationError as well
            # self.add_error('end_date', form.ValidationError('Event end date should not occur before start date.'))  
		return cleaned_data
