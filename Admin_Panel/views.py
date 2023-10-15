from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse , reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView , UpdateView

from Article_Module.models import Article
from utils.Permission_Checker import permission_checker_decorator


# Create your views here.



@permission_checker_decorator
def Index(request: HttpRequest):
    return render(request, 'Admin_Panel/Dashboard/Index.html')


def All_Articles(request: HttpRequest):
    return render(request, 'Admin_Panel/Articles/Articles_List.html', {})


@method_decorator(permission_checker_decorator, name = 'dispatch')
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


@method_decorator(permission_checker_decorator, name = 'dispatch')
class ArticleEditView(UpdateView):
    model = Article
    template_name = 'Admin_Panel/Articles/EditArticle.html'
    fields = '__all__'
    success_url = reverse_lazy('Admin_Articles')
