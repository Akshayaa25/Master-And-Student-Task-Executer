"""Task_Executer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TaskApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('masterLogin',views.masterLogin,name='masterLogin'),
    path('studentLogin',views.studentLogin,name='studentLogin'),
    path('studentSignup',views.studentSignup,name='masterSignup'),
    path('masterSignup',views.masterSignup,name='masterSignup'),
    path('logout',views.logout,name='logout'),
    path('masterDashboard',views.masterDashboard,name='masterDashboard'),
    path('createTask',views.createTask,name='createTask'),
    path('taskList',views.taskList,name='taskList'),
    path('studentAnswer',views.studentAnswer,name='studentAnswer'),
    path('studentDashboard',views.studentDashboard,name='studentDashboard'),
    path('viewTask/<int:id>',views.viewTask,name='viewTask'),
    path('taskSolve',views.taskSolve,name='taskSolve'),
    path('solveTask/<int:id>',views.solveTask,name='solveTask'),
    path('listoftask',views.listoftask,name='listoftask'),
    path('activity',views.activity,name='activity'),
]