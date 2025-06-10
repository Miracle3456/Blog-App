from django.urls import path 
from .views import BlogPostView , PostDetailView , BlogCreateView , BlogUpdateView

urlpatterns = [
    path('post/<int:pk>/update' , BlogUpdateView.as_view (), name = 'post_update'),
    path('post/new/' , BlogCreateView.as_view() , name = 'post_new' ),
    path('post/<int:pk>/' , PostDetailView.as_view() , name = 'post_detail'),
    path('' ,BlogPostView.as_view() , name = 'blog_post_view' ),
     
]