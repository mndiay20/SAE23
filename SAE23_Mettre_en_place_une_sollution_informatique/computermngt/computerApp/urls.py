from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machines/', views.machine_list_view, name='machines'),
    path('personnes/', views.personnel_list_view, name='personnes'),
    path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
    path('personne/<pk>', views.personne_detail_view, name='personne-detail'),
    path('add-machine', views.machine_add_form, name='add-machine'),
    path('add-personne', views.personne_add_form, name='add-personne'),
    path('machine/<int:pk>/delete/', views.machine_delete_view, name='machine-delete'),
    path('personne/<int:pk>/delete/', views.personne_delete_view, name='personne-delete'),
    path('login/', views.login_view, name='login'),
]
