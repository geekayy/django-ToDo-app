from django.contrib import admin
from django.urls import path, include
from TodoList import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TodoList, name='TodoList')
]