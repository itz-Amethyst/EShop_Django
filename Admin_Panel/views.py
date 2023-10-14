from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from Article_Module.models import Article


# Create your views here.


def Index(request: HttpRequest):
    return render(request, 'Admin_Panel/Dashboard/Index.html', {})


def All_Articles(request: HttpRequest):
    return render(request, 'Admin_Panel/Articles/Articles_List.html', {})



class ArticlesView(ListView):
    template_name = 'Admin_Panel/Articles/Articles_List.html'
    model = Article
    context_object_name = 'Article_Lists'
    # ordering = ['-created_date']
    paginate_by = 7

    def get_queryset(self):
        base_query = super().get_queryset()
        # base_query: Article = base_query.selected_categories
        # category_name = self.kwargs.get('category')
        # if category_name is not None:
        #     base_query = base_query.filter(selected_categories__url_title__iexact = category_name)
        return base_query

    def get_context_data(self,  *args, **kwargs):
        context = super(ArticlesView, self).get_context_data(*args, **kwargs)
        # context['date'] = datetime2jalali(self.request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
        # context['date'] = datetime2jalali(self.request.user.date_joined)
        return context

