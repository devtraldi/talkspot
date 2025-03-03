from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('relevance/', views.relevance, name='app_relevance'),  # Posts ordenados por curtidas
    path('trending/', views.trending, name='app_trending'), # Posts ordenados por trending
    path('login/', views.app_login, name='app_login'),
    path('logout/', views.app_logout, name='app_logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_list, name='post_list'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/comment/create/', views.create_comment, name='create_comment'),
    path('post/<int:post_id>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('post/<int:post_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path("post/<int:post_id>/comment/<int:comment_id>/like/", views.like_comment, name="like_comment"),
    path("bookmark_post/<int:post_id>/", views.bookmark_post, name="bookmark_post"),
    path('bookmarks/', views.bookmarked_posts, name='bookmarked_posts'),
    path('user/<str:username>/', views.user_posts, name='user_posts'),
    path('editar-perfil/', views.edit_profile, name='edit_profile'),
]
