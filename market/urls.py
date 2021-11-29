from django.urls import path
from . import views


urlpatterns = [
    path('course_info', views.course_info, name='course_info'),
    path('dev_contact/', views.dev_contacts, name='dev_contact'),
    path('team_members/', views.team_members, name='team_members'),
    path('', views.main_page, name='main_page'),
    path('login_page', views.login_page, name='login_page'),
]