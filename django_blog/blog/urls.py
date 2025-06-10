from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.signup,name='signup'),
   path('login/',views.login,name='login'),
    path('newpost/', views.new_post, name='newpost'),
    path('mypost/', views.my_posts, name='mypost'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'), 
   
]
