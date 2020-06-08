from django.urls import path

from . import views

app_name = 'article1'

urlpatterns = [

    path('article-list/', views.article_list, name='article_list'),
      # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
]