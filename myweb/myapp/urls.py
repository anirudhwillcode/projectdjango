from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('delete_contact/<ID>', views.delete_contact, name="Delete Contact"),
    path('update_contact/<ID>', views.update_contact, name="Update Contact"),
    path('regs',views.regs,name="regs"),
    path('login_user', views.login_user , name="login_user"),
    path('logout_user',views.logout_user,name="logout_user"),
]