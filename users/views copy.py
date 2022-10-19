from distutils import errors
from tkinter import Widget
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import  render, redirect
from users.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.core.exceptions import ValidationError

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			
			return redirect('lists')
		messages.error(request, "Unsuccessful registration. User already exists or check details.")
	form = NewUserForm()

    
	return render(request=request, template_name="users/register.html", context={"register_form": form})



class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lists')


class RegisterPage(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('lists')
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('lists')
        return super(RegisterPage, self).get(args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        messages.error(self.request, "Unsuccessful registration. Invalid information.")
        return super(RegisterPage, self).form_valid(form)

    def form_invalid(self, form):
        for field in form:
            if field.errors :
                print(field , field.errors)
                field.field.widget.attrs['class'] += ' is-invalid' 
        return super().form_invalid(form)

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("This password must contain at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class MinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("This password must contain at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_length)d characters."
            % {'min_length': self.min_length}
        )
