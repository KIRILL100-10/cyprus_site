from django.urls import path
from . import views

app_name = 'history'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('article/detail/<slug:article_slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('category/articles/<slug:category_slug>/', views.ArticleCategory.as_view(), name='article_category'),
]
