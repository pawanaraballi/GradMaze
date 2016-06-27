from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.views.generic import View

from django.contrib.auth.models import User


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import numpy as np

from .models import *

from .forms import *

from utilities import SimilarityMetrics

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

#
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/GradMaze/'

    # Called after forms.RegisterForm.clean()
    def form_valid(self, form):

        # Create User
        new_user = User.objects.create_user(form.data['user_name'],form.data['email'],form.data['password'])
        Student.objects.create(user=new_user,subscribed=False)

        #TODO Create Student object for user

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
        applications = Application.objects.filter(student__user_id=request.user.id)

        #GREScores
        gre = GREScore.objects.filter(student__user_id=request.user.id)
        #TOEFLScores
        toefl = TOEFLScore.objects.filter(student__user_id=request.user.id)
        #Current Program
        id = request.user.id
        student = Student.objects.get(user_id=request.user.id)

        indust = IndustryExperience.objects.filter(student__user_id=request.user.id)

        credit_card = CreditCard.objects.filter(user_id=request.user.id)
        if not credit_card:
            credit_card_form = CreditCardForm()
        else:
            credit_card = CreditCard.objects.get(user_id=request.user.id)
            credit_card_form =CreditCardForm(initial={'city':credit_card.city,
                                                      'card_type':credit_card.card_type,
                                                      'first_name':credit_card.first_name,
                                                      'last_name':credit_card.last_name,
                                                      'number':credit_card.number,
                                                      'secuirty':credit_card.security_code,
                                                      'expr_year':credit_card.expiration,
                                                      'line1':credit_card.addr_line1,
                                                      'line2':credit_card.addr_line2,
                                                      'state':credit_card.state,
                                                      'zip':credit_card.zip,
                                                      'phone_number':credit_card.phone_number,})

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
                  'indust':indust,
                  'credit_card_form':credit_card_form,}
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
                student = Student.objects.get(user_id=request.user.id)
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
                student = Student.objects.filter(user_id=request.user.id)
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
                student = Student.objects.filter(user_id=request.user.id)
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
                student = Student.objects.get(user_id=request.user.id)
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
                student = Student.objects.get(user_id=request.user.id)
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
                student = Student.objects.get(user_id=request.user.id)
                expr = IndustryExperience.objects.create(student=student,
                                                  company=indust_form.cleaned_data['company'],
                                                  position=indust_form.cleaned_data['position'],
                                                  start_date=indust_form.cleaned_data['start_date'],
                                                  end_date=indust_form.cleaned_data['end_date'])
                expr.save()
                return HttpResponseRedirect("/GradMaze/accounts/manage/")
        else:
            indust_form = IndustryExperienceForm()



        # Credit Card Form Button Pressed
        if('ccinfo' in request.POST):
            credit_card_form =CreditCardForm(request.POST)
            if credit_card_form.is_valid():

                credit_card = CreditCard.objects.filter(user_id=request.user.id)

                if not credit_card:

                    credit_card = CreditCard.objects.create(user_id=request.user.id,
                                                            card_type = credit_card_form.cleaned_data['card_type'],
                                                            first_name = credit_card_form.cleaned_data['first_name'] ,
                                                            last_name = credit_card_form.cleaned_data['last_name'],
                                                            number = credit_card_form.cleaned_data['number'],
                                                            security_code = credit_card_form.cleaned_data['secuirty'],
                                                            expiration = credit_card_form.cleaned_data['expr_year'],
                                                            addr_line1 = credit_card_form.cleaned_data['line1'],
                                                            addr_line2 = credit_card_form.cleaned_data['line2'],
                                                            state = credit_card_form.cleaned_data['state'],
                                                            city = credit_card_form.cleaned_data['city'],
                                                            zip = credit_card_form.cleaned_data['zip'],
                                                            phone_number=credit_card_form.cleaned_data['phone_number'])
                    credit_card.save()

                    student = Student.objects.filter(user__id=request.user.id)
                    student.update(subscribed=True)
                else:
                    credit_card.update(card_type = credit_card_form.cleaned_data['card_type'],
                                                            first_name = credit_card_form.cleaned_data['first_name'] ,
                                                            last_name = credit_card_form.cleaned_data['last_name'],
                                                            number = credit_card_form.cleaned_data['number'],
                                                            security_code = credit_card_form.cleaned_data['secuirty'],
                                                            expiration = credit_card_form.cleaned_data['expr_year'],
                                                            addr_line1 = credit_card_form.cleaned_data['line1'],
                                                            addr_line2 = credit_card_form.cleaned_data['line2'],
                                                            state = credit_card_form.cleaned_data['state'],
                                                            city = credit_card_form.cleaned_data['city'],
                                                            zip = credit_card_form.cleaned_data['zip'],
                                                            phone_number=credit_card_form.cleaned_data['phone_number'])

                return HttpResponseRedirect("/GradMaze/accounts/manage/")
        else:
            credit_card = CreditCard.objects.get(user_id=request.user.id)
            if not credit_card:
                credit_card_form = CreditCardForm()
            else:
                credit_card_form =CreditCardForm(initial={'city':credit_card.city,
                                                          'card_type':credit_card.card_type,
                                                          'first_name':credit_card.first_name,
                                                          'last_name':credit_card.last_name,
                                                          'number':credit_card.number,
                                                          'secuirty':credit_card.security_code,
                                                          'expr_year':credit_card.expiration,
                                                          'line1':credit_card.addr_line1,
                                                          'line2':credit_card.addr_line2,
                                                          'state':credit_card.state,
                                                          'zip':credit_card.zip,
                                                          'phone_number':credit_card.phone_number,})



        # Applications For Logged In User
        applications = Application.objects.filter(student__user_id=request.user.id)
        gre = GREScore.objects.filter(student__user_id=request.user.id)
        toefl = TOEFLScore.objects.filter(student__user_id=request.user.id)
        student = Student.objects.get(user_id=request.user.id)
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
                  'indust':indust,
                  'credit_card_form':credit_card_form,}

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

class DetailSchoolProgramFromSP(DetailView):
    model = SchoolProgram
    template_name = 'school_program_ancher_list.html'

class UserListView(ListView):
    model = Student
    template_name = 'students_list.html'
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        self.extra_context["student"]=Student.objects.get(user_id=self.request.user.id)

        context.update(self.extra_context)
        return context







class DetailStudentListView(ListView):
    template_name = 'details_student_list.html'



    def get(self, request, *args, **kwargs):
        try:
            application_details = Application.objects.filter(student__user_id=self.kwargs['pk'])
        except Application.DoesNotExist:
            application_details=[]

        try:
            student=Student.objects.get(user_id=self.kwargs['pk'])
        except Student.DoesNotExist:
            student=[]

        try:
            gre_scores=GREScore.objects.get(student__user_id=self.kwargs['pk'])
        except GREScore.DoesNotExist:
            gre_scores=[]

        try:
            toelf_scores=TOEFLScore.objects.get(student__user_id=self.kwargs['pk'])
        except TOEFLScore.DoesNotExist:
            toelf_scores=[]






        params = {
            'application_details':application_details,
            'student': student,
            'toelf_scores': toelf_scores,
            'gre_scores': gre_scores
        }

        return render(request,self.template_name,params)



class SearchResultView(View):
    template_name = 'search_results.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SearchResultView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        results = []

        if(request.POST.get('field') == 'School'):
            from django.db.models import Q
            results = School.objects.filter(Q(name__icontains=request.POST.get('query_string'))|Q(abbr__icontains=request.POST.get('query_string')))


        if(request.POST.get('field') == 'Program'):
            from django.db.models import Q
            results = Program.objects.filter(Q(name__icontains=request.POST.get('query_string'))|Q(level__icontains=request.POST.get('query_string')))

        if(request.POST.get('field') == 'School Program'):
            from django.db.models import Q
            results = SchoolProgram.objects.filter(Q(school__name__icontains=request.POST.get('query_string'))|Q(school__abbr__icontains=request.POST.get('query_string'))|
                                                   Q(program__name__icontains=request.POST.get('query_string'))|Q(program__level__icontains=request.POST.get('query_string')))


        params = {'results':results,
                  'field':request.POST.get('field'),
                  'query_string':request.POST.get('query_string')}

        return render(request, self.template_name,params )



class CancelSubView(View):

    def post(self, request, *args, **kwargs):

        student = Student.objects.filter(user__id=request.user.id)
        student.update(subscribed=False)

        CreditCard.objects.get(user_id=request.user.id).delete()

        return HttpResponse('result')



class SimilarStudentsView(View):
    template_name = 'similar_students.html'

    def get(self, request, *args, **kwargs):
        metrics = SimilarityMetrics()
        similar_thres = .75


        target_student = Student.objects.get(user_id=request.user.id)

        try:
            target_gre = GREScore.objects.get(student__user_id=request.user.id)
        except GREScore.DoesNotExist:
            target_gre = []

        try:
            target_toefl = TOEFLScore.objects.get(student__user_id=request.user.id)
        except TOEFLScore.DoesNotExist:
            target_toefl = []


        target_vect = [target_student.current_gpa]
        fake_mean_gpa = [3.0]
        gre_required = False
        toefl_required = False

        if target_gre:
            fake_mean_gre = [150,150,3]
            gre_required = True
            target_vect = target_vect + [target_gre.verb,target_gre.quant,target_gre.write]
        else:
            fake_mean_gre = []


        if target_toefl:
            fake_mean_toefl = [20,20,20,20]
            toefl_required = True
            target_vect = target_vect + [target_toefl.reading,target_toefl.listening,target_toefl.speaking,target_toefl.writing]
        else:
            fake_mean_toefl = []



        fake_mean = np.asarray(fake_mean_gpa+fake_mean_gre+fake_mean_toefl)


        target_vect = np.asarray(target_vect)-fake_mean


        all_students = Student.objects.all()
        scores = []
        for student in all_students:

            vect = [student.current_gpa]

            if gre_required:
                try:
                    gre = GREScore.objects.get(student__user_id=student.user_id)
                    vect = vect + [gre.verb,gre.quant,gre.write]
                except GREScore.DoesNotExist:
                    scores.append(0)
                    continue

            if toefl_required:
                try:
                    toefl = TOEFLScore.objects.get(student__user_id=student.user_id)
                    vect = vect + [toefl.reading,toefl.listening,toefl.speaking,toefl.writing]
                except TOEFLScore.DoesNotExist:
                    scores.append(0)
                    continue


            vect = np.asarray(vect)-fake_mean

            # In this context this is actually pearson correlation and not cosine similarity
            scores.append(np.abs(metrics.cosine_similarity(vect,target_vect)))


        similar_students = []
        similar_students_gre = []
        similar_students_toefl = []
        for i, score in enumerate(scores):
            if score >= similar_thres:

                try:
                    similar_students.append(all_students[i])
                    if toefl_required:
                        similar_students_toefl.append(TOEFLScore.objects.get(student=all_students[i].id))
                    if gre_required:
                        similar_students_gre.append(GREScore.objects.get(student=all_students[i].id))

                except (GREScore.DoesNotExist,TOEFLScore.DoesNotExist):
                    continue



        if(gre_required and toefl_required):
            similar_students = zip(similar_students,similar_students_gre,similar_students_toefl)
        elif(gre_required):
            similar_students = zip(similar_students,similar_students_gre)
        elif(toefl_required):
            similar_students = zip(similar_students,similar_students_toefl)





        params = {"similar_students":similar_students,
                  "toefl_required":toefl_required,
                  "gre_required":gre_required}

        return render(request, self.template_name,params )
