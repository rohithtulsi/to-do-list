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


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect('lists')
		messages.error(request, "Unsuccessful registration. User already exists.")
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
