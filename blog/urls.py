from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.sign_up,name='signup'),
    path('logout/',views.log_out,name='logout'),
    path('login/',views.log_in,name='login'),
    path('changepwd/',views.chg_pwd,name='chgpwd'),
    path('addpost/',views.add_post,name='addpost'),
    path('updatepost/<int:id>/',views.update_post,name='updatepost'),
    path('deletepost/<int:id>/',views.delete_post,name='deletepost'),
]