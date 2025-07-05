from django.urls import path
from . import views


urlpatterns = [
    path('ads/new/', views.create_ad, name='create_ad'),
    path('ads/<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),
]