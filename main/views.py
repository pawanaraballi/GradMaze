from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.views.generic import View

from django.contrib.auth.models import User

from .models import *

from .forms import *

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
        curr_prog_form = CurrentProgramForm()
        prev_prog_form = PreviousProgramForm()
        gre_form = GREScoreForm()
        toefl_form = TOEFLScoreForm()
        indust_form = IndustryExperienceForm()

        # Applications For Logged In User
        applications = Application.objects.filter(student__id=request.user.id)

        #GREScores
        gre = GREScore.objects.filter(student__id=request.user.id)
        #TOEFLScores
        toefl = TOEFLScore.objects.filter(student__id=request.user.id)
        #Current Program
        student = Student.objects.get(id=request.user.id)

        indust = IndustryExperience.objects.filter(student__id=request.user.id)


        params = {'apps': applications,
                  'apps_form': apps_form,
                  'gre':gre,
                  'toefl':toefl,
                  'student':student,
                  'curr_prog_form': curr_prog_form,
                  'prev_prog_form':prev_prog_form,
                  'gre_form':gre_form,
                  'toefl_form':toefl_form,
                  'indust_form':indust_form,
                  'indust':indust}
        return render(request, self.template_name,params )



    def post(self, request, *args, **kwargs):



        #########################################
        # Catching Which Form Button Is Pressed #
        #########################################

        # Application Form Button Pressed
        if('app' in request.POST):
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
        else:
            apps_form = ApplicationForm()

        # Current Program Form Button Pressed
        if('cprog' in request.POST):
            curr_prog_form = CurrentProgramForm(request.POST)
            if curr_prog_form.is_valid():
                student = Student.objects.filter(id=request.user.id)
                student.update(current_program=curr_prog_form.cleaned_data['curr_school_program'],
                               current_gpa=curr_prog_form.cleaned_data['curr_gpa'],
                               current_credit_hours=curr_prog_form.cleaned_data['curr_credit_hours'],
                               current_start_date=curr_prog_form.cleaned_data['curr_start_date'],
                               current_end_date =curr_prog_form.cleaned_data['curr_end_date'])
                return HttpResponseRedirect("/GradMaze/accounts/manage/")
        else:
            curr_prog_form = CurrentProgramForm()


        # Previous Program Form Button Pressed
        if('pprog' in request.POST):
            prev_prog_form = PreviousProgramForm(request.POST)
            if prev_prog_form.is_valid():
                student = Student.objects.filter(id=request.user.id)
                student.update(prev_program=prev_prog_form.cleaned_data['prev_school_program'],
                               prev_gpa=prev_prog_form.cleaned_data['prev_gpa'],
                               prev_credit_hours=prev_prog_form.cleaned_data['prev_credit_hours'],
                               prev_start_date=prev_prog_form.cleaned_data['prev_start_date'],
                               prev_end_date =prev_prog_form.cleaned_data['prev_end_date'])
                return HttpResponseRedirect("/GradMaze/accounts/manage/")
        else:
            prev_prog_form = PreviousProgramForm()


        # GRE Form Button Pressed
        if('gre' in request.POST):
            gre_form = GREScoreForm(request.POST)
            if gre_form.is_valid():
                student = Student.objects.get(id=request.user.id)
                gre = GREScore.objects.create(student=student,
                                                  verb=gre_form.cleaned_data['verb'],
                                                  quant=gre_form.cleaned_data['quant'],
                                                  write=gre_form.cleaned_data['write'])
                gre.save()
        else:
            gre_form = GREScoreForm()



        # TOEFL Form Button Pressed
        if('toefl' in request.POST):
            toefl_form = TOEFLScoreForm(request.POST)
            if toefl_form.is_valid():
                student = Student.objects.get(id=request.user.id)
                toefl = TOEFLScore.objects.create(student=student,
                                                  reading=toefl_form.cleaned_data['reading'],
                                                  listening=toefl_form.cleaned_data['listening'],
                                                  writing=toefl_form.cleaned_data['writing'],
                                                  speaking=toefl_form.cleaned_data['speaking'])
                toefl.save()
                return HttpResponseRedirect("/GradMaze/accounts/manage/")
        else:
            toefl_form = TOEFLScoreForm()


        if('indust' in request.POST):
            indust_form = IndustryExperienceForm(request.POST)
            if indust_form.is_valid():
                student = Student.objects.get(id=request.user.id)
                expr = IndustryExperience.objects.create(student=student,
                                                  company=indust_form.cleaned_data['company'],
                                                  position=indust_form.cleaned_data['position'],
                                                  start_date=indust_form.cleaned_data['start_date'],
                                                  end_date=indust_form.cleaned_data['end_date'])
                expr.save()
                return HttpResponseRedirect("/GradMaze/accounts/manage/")
        else:
            indust_form = IndustryExperienceForm()



        # Applications For Logged In User
        applications = Application.objects.filter(student__id=request.user.id)
        gre = GREScore.objects.filter(student__id=request.user.id)
        toefl = TOEFLScore.objects.filter(student__id=request.user.id)
        student = Student.objects.get(id=request.user.id)
        indust = IndustryExperience.objects.filter(student__id=request.user.id)


        params = {'apps': applications,
                  'apps_form': apps_form,
                  'gre':gre,
                  'toefl':toefl,
                  'student':student,
                  'curr_prog_form': curr_prog_form,
                  'prev_prog_form':prev_prog_form,
                  'gre_form':gre_form,
                  'toefl_form':toefl_form,
                  'indust_form':indust_form,
                  'indust':indust}

        return render(request, self.template_name, params)




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

class DeleteIndustExprView(View):
    def post(self, request):
        expr_pk = request.POST.get('row_id')[7:]
        print(expr_pk)
        expr = IndustryExperience.objects.get(id=expr_pk)
        expr.delete()
        return HttpResponse('result')

from django.views.generic.list import ListView
class SchoolListView(ListView):
    model = School
    template_name = 'school_list.html'


class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'


class SchoolProgramListView(ListView):
    model = SchoolProgram
    template_name = 'school_program_list.html'


class DetailSchoolListView(ListView):
    model = School
    template_name = 'detail_school_list.html'


class DetailProgramListView(ListView):
    model = Program
    template_name = 'detail_program_list.html'

from django.views.generic import DetailView
class DetailSchoolFromSP(DetailView):
    model = School
    template_name = 'school_ancher_list.html'


class DetailProgramFromSP(DetailView):
    model = Program
    template_name = 'program_ancher_list.html'
