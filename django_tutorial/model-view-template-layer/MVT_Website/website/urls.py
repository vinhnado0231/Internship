from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_view'),
    path('logout/', views.logout_page, name='logout_view'),
    path('register/', views.register_page, name='register_page'),
    path('register/new_user/', views.register, name='register'),
]