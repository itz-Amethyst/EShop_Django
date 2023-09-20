from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView , DetailView

from Article_Module.models import Article , ArticleCategory , ArticleComment


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
    paginate_by = 1

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


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'Article_Module/article_view.html'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(is_active = True)
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article: Article = kwargs.get('object')

        context['comments'] = ArticleComment.objects.filter(article_id = article.id, is_submitted = True, parent = None).prefetch_related('articlecomment_set') # prefetch same as join in .net

        return context