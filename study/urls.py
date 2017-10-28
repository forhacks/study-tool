from django.conf.urls import url

from . import views

app_name = 'study'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard')
]
