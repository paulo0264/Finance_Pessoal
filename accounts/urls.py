from django import views
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    # path('sair/$', views.logout, name='logout'),
    # path('dashboard/$', views.dashboard, name='dashboard'),
    # path('cadastre-se/$', views.register, name='register'),
    
]