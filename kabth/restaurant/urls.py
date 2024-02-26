from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('menu/',views.menu, name="menu"),
    path('about/',views.about, name="about"),
    path('booking/', views.booking, name="booking"),
    path('menu_item/<int:pk>/', views.menu_item, name= "menu_item"),
]
