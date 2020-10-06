from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('studentregister',views.studentreg,name='studentregister'),
    path('staffregister',views.staffreg,name='staffregister')
]
