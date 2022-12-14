from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, ArticleCreate, ArticleUpdate, ArticleDelete

urlpatterns = [
   path('', PostList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view(), name='news_detail'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]

