from django.urls import path
from . import views

urlpatterns = [
    # Landing and Auth
    path('', views.landing_page, name='landing'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Admin URLs
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/create-user/', views.admin_create_user, name='admin_create_user'),
    
    # Brother URLs
    path('brother/profile/create/', views.brother_profile_create, name='brother_profile_create'),
    path('brother/success/', views.brother_success, name='brother_success'),
    
    # PNM URLs
    path('pnm/profile/create/', views.pnm_profile_create, name='pnm_profile_create'),
    path('pnm/results/', views.pnm_results, name='pnm_results'),
]

