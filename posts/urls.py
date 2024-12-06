from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_list, name='list'),
    path('new-post/', views.post_new, name='new-post'),
    path('<slug:slug>', views.post_page, name='page'),
]

# let slug url stay at the bottom so that i dont catch new-post url