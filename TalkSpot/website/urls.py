from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='website_index'),
    path('get-quote/', views.get_random_quote, name='get_random_quote'),
    path('bart-game/', views.bart_game, name='bart_game'),
    path('em_construcao/', views.em_construcao, name='em_construcao'),
]
