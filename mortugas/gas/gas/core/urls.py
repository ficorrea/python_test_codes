from django.conf.urls import url
from gas.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
