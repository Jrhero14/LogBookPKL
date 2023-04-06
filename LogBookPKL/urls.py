from django.contrib import admin
from django.urls import path
from User import views as userViews

urlpatterns = [
    path('', userViews.indexViews),
    path('newLog/', userViews.newLog),
    path('editLog/', userViews.editLog),
    path('delLog/', userViews.deleteLogBook),
    path('admin/', admin.site.urls)
]
