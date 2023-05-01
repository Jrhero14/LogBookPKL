from django.contrib import admin
from django.urls import path
from User import views as userViews

urlpatterns = [
    path('', userViews.indexViews),
    path('splash/', userViews.splashviews),
    path('auth/', userViews.loginViews),
    path('registrasi/', userViews.register),
    path('login/', userViews.logincekViews),
    path('logout/', userViews.logoutViews),
    path('newLog/', userViews.newLog),
    path('editLog/', userViews.editLog),
    path('delLog/', userViews.deleteLogBook),
    path('admin/', admin.site.urls)
]
