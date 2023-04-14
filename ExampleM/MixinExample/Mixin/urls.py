"""MixinExample URL Configuration

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
from django.urls import path
from Mixin.views import  TeacherListView, TeacherDetailView , CourseView,CourseListView # , StndList, StudentDetailapiView

urlpatterns = [
    path('course/', CourseView.as_view(), name='CourseView'),
    path('course/<int:pk>/',CourseListView.as_view()),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_list'),
    #path(r'students/', StndList.as_view()),
    #path(r'students/<int:pk>/', StudentDetailapiView.as_view()),
]