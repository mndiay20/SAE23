from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('machines/', views.machine_list_view, name='machines'),
    path('personnes/', views.personnel_list_view, name='personnes'),
    path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
    path('personne/<pk>', views.personne_detail_view, name='personne-detail'),
    path('add-machine', views.machine_add_form, name='add-machine'),
    path('add-personne', views.personne_add_form, name='add-personne'),
]
