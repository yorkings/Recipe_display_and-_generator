from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name="home"),
    path('dashboard/',dashboard,name="dashboard"),
    path('login/',login_user,name="login"),
    path('register/',register,name='sign-up'),
    path('logout/',logout_user,name='logout'),
    path("profile/",user_profile,name="profile"),
    path("post/",Create_post,name='create_post')
    
]