from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index, name='Admin_Dashboard'),
    path('article-lists/', views.ArticlesView.as_view(), name='Admin_Articles'),
    path('article-lists/<pk>', views.ArticleEditView.as_view(), name='admin_edit_article'),
]