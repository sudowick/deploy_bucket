from django.urls import path
from . import views
from .views import PostListView
urlpatterns = [
    path('', PostListView.as_view(), name='gallery-home'),
    path('myposts/', views.myposts, name = 'gallery-myposts'),
    path('post/new', views.upload, name = 'post-create'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='photo-detail'),
]
