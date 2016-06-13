from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.views.generic import View

from django.contrib.auth.models import User

from .models import *

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

        #GREScores
        gre = GREScore.objects.filter(student__id=request.user.id)
        #TOEFLScores
        toefl = TOEFLScore.objects.filter(student__id=request.user.id)
        #Current Program
        student = Student.objects.get(id=request.user.id)
        return render(request, self.template_name, {'apps': applications,'apps_form': apps_form,'gre':gre,'toefl':toefl,'student':student})



    def post(self, request, *args, **kwargs):

        apps_form = ApplicationForm(request.POST)


        if apps_form.is_valid():
            # Add Application to DB
            student = Student.objects.get(id=request.user.id)
            new_app = Application.objects.create(student=student,
                                                 school_program=apps_form.cleaned_data['school_program'],
                                                 date_submitted=apps_form.cleaned_data['date_submitted'],
                                                 date_updated=apps_form.cleaned_data['date_updated'],
                                                 status=apps_form.cleaned_data['status'])
            new_app.save()
            return HttpResponseRedirect("/GradMaze/accounts/manage/")


        # Applications For Logged In User
        applications = Application.objects.filter(student__id=request.user.id)
        gre = GREScore.objects.filter(student__id=request.user.id)
        toefl = TOEFLScore.objects.filter(student__id=request.user.id)

        return render(request, self.template_name, {'apps': applications,'apps_form': apps_form,'gre':gre,'toefl':toefl})




from django.http import HttpResponse
from django.views.generic import View

class DeleteAccountView(View):
    def post(self, request):
        user = User.objects.get(id=self.request.user.id)
        user.delete()
        return HttpResponse('result')


class DeleteApplicationView(View):
    def post(self, request):
        application_pk = request.POST.get('row_id')[4:]
        application = Application.objects.get(id=application_pk)
        application.delete()
        return HttpResponse('result')

import datetime

class ModifyApplicationView(View):
    def post(self, request):
        application_pk = request.POST.get('row_id')[4:]
        status = request.POST.get('status')
        application = Application.objects.filter(id=application_pk)
        application.update(status=status,date_updated=datetime.datetime.today())
        return HttpResponse('result')

class DeleteGREScoreView(View):
    def post(self, request):
        gre = GREScore.objects.filter(student__id=request.user.id)
        gre.delete()
        return HttpResponse('result')

class DeleteTOEFLScoreView(View):
    def post(self, request):
        toefl = TOEFLScore.objects.filter(student__id=request.user.id)
        toefl.delete()
        return HttpResponse('result')

class DeletePrevProgramView(View):
    def post(self, request):
        student = Student.objects.filter(id=request.user.id)
        student.update(prev_program=None,prev_gpa=None,prev_credit_hours=None,prev_start_date=None,prev_end_date=None)
        return HttpResponse('result')

class DeleteCurrProgramView(View):
    def post(self, request):
        student = Student.objects.filter(id=request.user.id)
        student.update(current_program=None,current_gpa=None,current_credit_hours=None,current_start_date=None,current_end_date=None)
        return HttpResponse('result')