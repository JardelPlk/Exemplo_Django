from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
    path('author/<pk>/', views.author_perfil, name='author_perfil'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]#Lista de urls
