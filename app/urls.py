

from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # STUDENTS
    path('students/', getStudents),

    path('add/', addStudent),

    path('update/<int:pk>/', updateStudent),

    path('delete/<int:pk>/', deleteStudent),

    # REGISTER
    path('register/', registerUser),

    # LOGIN
    path('login/', TokenObtainPairView.as_view()),

    # REFRESH TOKEN
    path('refresh/', TokenRefreshView.as_view()),

]