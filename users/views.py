from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lists')


from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect


class RegisterPage(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('lists')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('lists')
        return super(RegisterPage, self).get(args, **kwargs)
