from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)


app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_page"),
    path("blog_post/<int:pk>/", BlogDetailView.as_view(), name="blog_post"),
    path("create/", BlogCreateView.as_view(), name="post_create"),
    path("update/<int:pk>/", BlogUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="post_delete"),
]
