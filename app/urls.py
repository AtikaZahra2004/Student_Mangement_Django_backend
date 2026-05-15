from django.urls import path
from .views import *

urlpatterns = [
    path('students/', getStudents),
    path('add/', addStudent),
    path('update/<int:pk>/', updateStudent),
    path('delete/<int:pk>/', deleteStudent),
    path(
    'register/',
    registerUser
),

]