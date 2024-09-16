from django.urls import path

from . import views

# Template Tag
app_name = 'booking_site'

urlpatterns = [
    path("booking/", views.booking, name="booking"),
    path("register/", views.register, name="register"),
    path('login/', views.user_login, name='user_login'),
]