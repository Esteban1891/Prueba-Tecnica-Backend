from django.urls import path 
from apps.student.api.api import admin_api_view, student_detail_api_view, admin_detail_api_view, admin_list_api_view

urlpatterns = [
    path('students/', admin_api_view, name = 'student'),
    path('students/<pk>/', student_detail_api_view, name = 'student'),
    path('students/note/<pk>/', admin_detail_api_view, name = 'student'),
    path('students/list/average/', admin_list_api_view, name = 'student'),
]