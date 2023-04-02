from django.contrib import admin
from django.urls import path
from User import views as userViews

urlpatterns = [
    path('', userViews.indexViews),
    path('newLog/', userViews.newLog),
    path('admin/', admin.site.urls)
]
