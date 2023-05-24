from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index,name='home'),
   path("settle/<int:id>",views.settle,name='settle'),
   path("table",views.table,name='table')
]