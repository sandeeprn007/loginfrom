from django.urls import path
from loginformapp import views

app_name='loginformapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('newpost/',views.newpost,name='newpost'),
    path('home/',views.home,name='home'),
    path('user_login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('user_logout/',views.user_logout,name='logout')
]