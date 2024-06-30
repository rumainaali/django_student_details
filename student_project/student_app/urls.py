from django.urls import path
from .views import student_detail_view, student_list_view

urlpatterns = [
    path('student/<int:id>/', student_detail_view, name='student_detail'),
    path('', student_list_view, name='student_list'),
]
