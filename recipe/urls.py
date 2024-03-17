from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name="home"),
    path('dashboard/',dashboard,name="dashboard"),
    path('login/',login_user,name="login"),
    path('register/',register,name='sign-up'),
    path('logout/',logout_user,name='logout'),
    path("profile/",user_profile,name="profile"),
    #post
    path("post/",Create_post,name='create_post'),
    path('post/lists/',post_list,name='post_list'),
    path('post/delete/<int:id>',delete_post,name="delete_post"),
    path('post/edit/<int:id>',edit_post,name='edit_post'),
    path('post/detail/<int:id>',post_detail,name='post_detail'),
    #cosmetics
    path('cosm/create/',cosmetics_create,name='create_cosmetics'),
    path('cosm/list/',cosmetics_display,name='cosmetics_list'),
    path('cosm/edit/<int:id>',cosmetics_edit,name='edit_cosmetics'),
    path('cosm/delete/<int:id>',delete_cosmetics,name='delete_cosmetics'),
    #learn
    path('learn/list/',learning_list, name='learning_list'),
    path('learn/detail/<int:pk>/',learning_detail, name='learning_detail'),
    path('learn/create/',learning_create, name='learning_create'),
    path('learn/<int:pk>/edit/',learning_edit, name='learning_edit'),
    path('learn/<int:pk>/delete/',learning_delete, name='learning_delete'),  
]