from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='website_index'),
    path('get-quote/', views.get_random_quote, name='get_random_quote'),
]