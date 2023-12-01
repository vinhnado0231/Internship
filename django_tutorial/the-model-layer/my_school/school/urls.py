from django.urls import path

from . import views

app_name = 'school'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student_detail'),
    path('class/<int:pk>', views.ClassDetailView.as_view(), name='class_detail'),
]