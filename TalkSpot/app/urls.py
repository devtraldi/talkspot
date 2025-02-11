from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('login/', views.app_login, name='app_login'),
    path('logout/', views.app_logout, name='app_logout'),
    path('post/<int:post_id>/', views.post_list, name='post_list'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/comment/create/', views.create_comment, name='create_comment'),
    path('post/<int:post_id>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
]