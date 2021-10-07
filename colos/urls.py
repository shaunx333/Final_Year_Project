from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doNic/', views.doNic, name='doNic')
]
