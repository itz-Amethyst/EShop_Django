from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles_list_page'),
    path('cat/<str:category>' , views.ArticlesView.as_view(), name = 'articles_by_category_list'),
    path('<pk>/<title>', views.ArticleDetailView.as_view(), name = 'article_detail_page'),

]