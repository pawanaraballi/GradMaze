from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^accounts/register/$', views.RegisterView.as_view(), name='register'),
    url(r'^accounts/manage/$', views.AccountManageView.as_view(), name='manage'),
    url(r'^accounts/delete/$', views.DeleteAccountView.as_view(), name='delete'),
    url(r'^accounts/apps/delete/$', views.DeleteApplicationView.as_view(), name='delete-app'),
    url(r'^accounts/apps/modify/$', views.ModifyApplicationView.as_view(), name='modify-app'),
    url(r'^accounts/grescore/delete/$', views.DeleteGREScoreView.as_view(), name='delete-gre'),
    url(r'^accounts/toeflscore/delete/$', views.DeleteTOEFLScoreView.as_view(), name='delete-toefl'),
    url(r'^accounts/prevprogram/delete/$', views.DeletePrevProgramView.as_view(), name='delete-pprog'),
    url(r'^accounts/currprogram/delete/$', views.DeleteCurrProgramView.as_view(), name='delete-cprog'),
    url(r'^accounts/experience/delete/$', views.DeleteIndustExprView.as_view(), name='delete-indust'),
    url(r'^accounts/subscription/cancel/$', views.CancelSubView.as_view(), name='cancel-sub'),
    url(r'^accounts/subscription/subscribe/$', views.SubscribeView.as_view(), name='subscibe'),

    url(r'^schools/$', views.SchoolListView.as_view(), name='school-list'),
    url(r'^programs/$', views.ProgramListView.as_view(), name='program-list'),
    url(r'^schoolprogram/$', views.SchoolProgramListView.as_view(), name='school-program-list'),

    url(r'^programs/(?P<pk>\d+)$', views.DetailProgramFromSP.as_view(), name='program-ancher-list'),
    url(r'^schools/(?P<pk>\d+)$', views.DetailSchoolFromSP.as_view(), name='school-ancher-list'),
    url(r'^schoolprogram/(?P<pk>\d+)$', views.DetailSchoolProgramFromSP.as_view(), name='school-ancher-list'),



    url(r'^search/$', views.SearchResultView.as_view(), name='search-results'),





    url(r'^detailschool/$', views.DetailSchoolListView.as_view(), name='detail-school-list'),
    url(r'^detailprogram/$', views.DetailProgramListView.as_view(), name='detail-program-list'),
]