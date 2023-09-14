from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from Article_Module.models import Article


# Create your views here.

# class ArticleView(View):
#     def get( self, request ):
#         articles = Article.objects.filter(is_active = True)
#         return render(request,'Article_Module/articles.html',{
#             'articles': articles
#         })

class ArticlesView(ListView):
    template_name = 'Article_Module/articles.html'
    model = Article
    context_object_name = 'articles'
    # ordering = ['-created_date']
    # paginate_by = 1
    paginate_by = 5

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(is_active = True)
        return data