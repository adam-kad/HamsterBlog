from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # Обработчики приложения блога
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail, name='post_detail'),
    path('about/', views.about_post_list, name='about_post_list'),
    path('post/', views.post),
    path('contact/', views.contact),
]
