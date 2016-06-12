from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.views.generic import View

from django.contrib.auth.models import User

from .models import Application, Student

from .forms import ApplicationForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/GradMaze/'

    # Called after forms.RegisterForm.clean()
    def form_valid(self, form):

        # Create User
        User.objects.create_user(form.data['user_name'],form.data['email'],form.data['password'])

        # Login User
        user = authenticate(username=form.data['user_name'], password=form.data['password'])
        login(self.request, user) # Login User
        return super(RegisterView, self).form_valid(form)


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


class AccountManageView(View):
    template_name = "account_manage.html"

    def get(self, request, *args, **kwargs):

        apps_form = ApplicationForm()

        # Applications For Logged In User
        applications = Application.objects.filter(student__id=request.user.id)
        return render(request, self.template_name, {'apps': applications,'apps_form': apps_form})



    def post(self, request, *args, **kwargs):

        apps_form = ApplicationForm(request.POST)

        # Applications For Logged In User
        applications = Application.objects.filter(student__id=request.user.id)
        return render(request, self.template_name, {'apps': applications,'apps_form': apps_form})




from django.http import HttpResponse
from django.views.generic import View

class DeleteAccountView(View):
    def post(self, request):
        user = User.objects.get(id=self.request.user.id)
        user.delete()
        return HttpResponse('result')