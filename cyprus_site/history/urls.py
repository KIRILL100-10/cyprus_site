from django.urls import path
from . import views

app_name = 'history'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('search/', views.ArticleSearch.as_view(), name='article_search'),
    path('article/detail/<slug:article_slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('category/articles/<slug:category_slug>/', views.ArticleCategory.as_view(), name='article_category'),
    path('article/comment/detail/<int:comment_id>/', views.CommentDetail.as_view(), name='comment_detail'),
    path('article/<slug:article_slug>/comment/create/', views.CreateComment.as_view(), name='create_comment'),
    path('comment/edit/<int:comment_id>/', views.EditComment.as_view(), name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.DeleteComment.as_view(), name='comment_delete'),
]
