from django.urls import path

from . import views

urlpatterns = [

    path('', views.store, name="store"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('checkout/', views.checkout, name="checkout")

]
