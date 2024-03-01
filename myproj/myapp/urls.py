from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('login',views.index,name='index'),
    path('signin',views.sign,name='sign')
    
    
   
    
    
]
