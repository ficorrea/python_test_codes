from django.conf.urls import url
from django.contrib.auth import views
# from gas.contas import views

'''urlpatterns = [
    url(r'^entrar/$', views.login, {'template_name': 'contas/login.html'},
        name='login'),
]'''

urlpatterns = [
    url(r'^entrar/$', views.login, {'template_name': 'contas/login.html'}, name='login'),
]