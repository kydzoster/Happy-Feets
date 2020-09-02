from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animal/<int:animal_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
