from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('about/', views.AboutListView.as_view(), name='about'),
    path('contact/', views.ContactListView.as_view(), name='contact'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('services/', views.ServicesListView.as_view(), name='services'),

]