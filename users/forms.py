from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class NewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user

	def validate(self, password, user=None):
		if len(password) < self.min_length:
			raise ValidationError(
                _("This password must contain at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )
