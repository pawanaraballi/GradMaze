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
    url(r'^accounts/apps/modify/$', views.ModifyApplicationView.as_view(), name='modify-app')
]