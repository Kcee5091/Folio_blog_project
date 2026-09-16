from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('login/', auth_views.LoginView.as_view(template_name='myblog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('blogs/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blogs/<int:post_id>/edit/', views.edit_blog, name='edit_blog'),
    path('blogs/<int:post_id>/delete/', views.delete_blog, name='delete_blog'),
    path('search/', views.search_blogs, name='search_blogs'),  
]   
