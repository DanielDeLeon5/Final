from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'nueva', views.asignacion_nueva, name='asignacion_nueva'),
    ]
