from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.
# class HomeView(View):
#     def get( self, request ):
#         return render(request, 'Home_Module/index.html')

class HomeView(TemplateView):
    template_name = 'Home_Module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is data in home page'
        return context

def site_header_component(request):
    return render(request, 'shared/components/header.html', {
        'link': 'آموزش پایتون'
    })

def site_footer_component(request):
    return render(request, 'shared/components/footer.html', {})