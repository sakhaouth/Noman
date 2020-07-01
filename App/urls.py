from django.urls import path
from django.contrib import admin

admin.autodiscover()
from . import views

urlpatterns = {
    path('signin', views.signIn),
    path('set', views.setToDatabase, name='ddd'),
    path('signUp', views.signup, name='nn'),
    path('new', views.checkSignIn, name='ccc'),
    path('1st', views.eventName, name='ss'),
    path('',views.index,name='index'),
    path('logout',views.logout),
    path('add',views.add),
    path('pra',views.function),
    path('remove',views.remove)

}
