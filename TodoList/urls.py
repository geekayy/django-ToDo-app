from django.contrib import admin
from django.urls import path, include
from TodoList import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('AddTask/', views.AddTask, name='AddTask'),
    path('logout/', views.signout, name='signout'),
]