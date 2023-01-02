
"""
url paths for rendering views to the browser
"""

from . import views
from django.urls import path
from .views import UpdatePost, DeletePost, AddPost


urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('add_post/new', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/edit/', views.UpdatePost.as_view(), name='update_post'),
    path('<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'),
]


