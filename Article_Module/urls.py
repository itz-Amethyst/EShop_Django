from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles_list_page'),
    path('cat/<str:category>' , views.ArticlesView.as_view(), name = 'articles_by_category_list'),
    path('<pk>/<slug:slug>', views.ArticleDetailView.as_view(), name = 'article_detail_page'),
    path('add-article-comment', views.add_article_comment, name='add_article_comment')

]