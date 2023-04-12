# define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # token-based authentication to secure the Table booking API
    path('api-token-auth/', obtain_auth_token),
    
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('about/', views.about, name="about"),
    # path('book/', views.book, name="book"),
    # path('reservations/', views.reservations, name="reservations"),
    # path('menu/', views.menu, name="menu"),
    # path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    # path('bookings', views.bookings, name='bookings'), 
]
