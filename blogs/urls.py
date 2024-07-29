from django.urls import path
from blogs.views import BlogListView, BlogDetailView, BlogTagView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('', BlogTagView.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),

]
