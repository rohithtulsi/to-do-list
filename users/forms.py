from logging import PlaceHolder
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class NewUserForm(UserCreationForm):
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation','class':'form-control'}))	
	
	class Meta:
		model = User
		fields = ('username','email', 'password1', 'password2')
		required_fields = ['username','email', 'password1', 'password2']

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

	def clean_email(self):
        # Get the email
		email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
		try:
			match = User.objects.get(email=email)
		except User.DoesNotExist:
            # Unable to find a user, this is fine
			return email

        # A user was found with this as a username, raise an error.
		raise forms.ValidationError('This email address is already in use.')


	def clean(self):
			
		cleaned_data = self.cleaned_data
		username = cleaned_data.get('username')


		if username:
			if len(username)<4:
				self.add_error('username', 'Username is too short')
            # You can use ValidationError as well
            # self.add_error('end_date', form.ValidationError('Event end date should not occur before start date.'))  
	

		return 