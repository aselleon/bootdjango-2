from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 


# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('course_info', views.course_info, name='course_info'),
    path('dev_contact/', views.dev_contacts, name='dev_contact'),
    path('team_members/', views.team_members, name='team_members'),
    path('', views.main_page, name='main_page'),
    path('login_page', views.login_page, name='login_page'),
    path('create_product', views.create_prod, name='create_product'),
    path('<int:pk>', views.ProductsDetailed.as_view(), name='detail_prod'),
]