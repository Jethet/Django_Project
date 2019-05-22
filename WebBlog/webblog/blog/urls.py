from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # '' specifies homepage for path
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]


# With class-based views, the server looks for the following pattern:
#  <app>/<model>_<viewtype>.html
# For example:  blog/post_list.html
