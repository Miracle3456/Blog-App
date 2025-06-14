from django.urls import path ,include
from .views import BlogPostView , PostDetailView , BlogCreateView , BlogUpdateView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('logout/' , auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/' , auth_views.LoginView.as_view(template_name = 'registration/login.html' ), name = 'login'),
    path('post/<int:pk>/update' , BlogUpdateView.as_view (), name = 'post_update'),
    path('post/new/' , BlogCreateView.as_view() , name = 'post_new' ),
    path('post/<int:pk>/' , PostDetailView.as_view() , name = 'post_detail'),
    path('' ,BlogPostView.as_view() , name = 'blog_post_view' ),
     
]