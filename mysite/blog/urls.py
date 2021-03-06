from django.urls import path
from . import views
from .feeds import LatestPostsFeed


app_name = 'blog'

urlpatterns = [
    # Обработчики приложения блога
    # path('', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail, name='post_detail'),
    path('about/', views.about_post_list, name='about_post_list'),
    path('post/', views.post),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
