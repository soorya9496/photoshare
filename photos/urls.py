from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('edit-product/<str:pk>/', views.editProduct, name='edit-prod'),
    path('delete-product/<str:pk>/', views.deleteProduct, name='delete-prod')
]