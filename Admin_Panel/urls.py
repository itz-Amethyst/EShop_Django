from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.Index, name='Admin_Dashboard'),
    path('article-lists/', views.ArticlesView.as_view(), name='Admin_Articles'),
]