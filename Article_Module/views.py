from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from Article_Module.models import Article , ArticleCategory
from jalali_date import date2jalali , datetime2jalali


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
        data = []
        base_query = super().get_queryset()
        data = base_query.filter(is_active = True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            data = base_query.filter(selected_categories__url_title__iexact = category_name)
        return data

    def get_context_data(self,  *args, **kwargs):
        context = super(ArticlesView, self).get_context_data(*args, **kwargs)
        # context['date'] = datetime2jalali(self.request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
        # context['date'] = datetime2jalali(self.request.user.date_joined)
        return context


def Article_Categories_Partial(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active = True, parent_id = None)
    context = {
        'main_categories': article_main_categories
    }
    return render(request, 'Article_Module/partials/article_categories.html', context)