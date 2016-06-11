from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.views.generic.edit import FormView
from django.shortcuts import render

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/GradMaze/'

    # Called after forms.LoginForm.clean()
    def form_valid(self, form):
        user = authenticate(username=form.data['user_name'], password=form.data['password'])
        login(self.request, user) # Login User
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        # do something -- log the error, etc -- if needed
        return super(LoginView, self).form_invalid(form)


class LogoutView(TemplateView):
    template_name = "logged_out.html"

    # On GET logout
    def get(self, request):
        logout(request)
        return render(request,self.template_name)

    # On POST logout
    def post(self, request):
        logout(request)
        return render(request,self.template_name)