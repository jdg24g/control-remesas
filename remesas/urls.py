from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.home, name='home'),
    path('home/main_cards',views.main_cards, name='main_cards'),
    path('home/login', views.login, name='home_login')
]
