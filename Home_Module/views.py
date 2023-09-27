from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from Product_Module.models import Product
from Site_Module.models import SiteSetting , FooterLinkBox , Slider
from utils.Custom_Methods import Group_List


# Create your views here.
# class HomeView(View):
#     def get( self, request ):
#         return render(request, 'Home_Module/index.html')

class HomeView(TemplateView):
    template_name = 'Home_Module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active = True)
        context['data'] = 'this is data in home page'

        latest_products = Product.objects.filter(is_active = True, is_deleted = False).order_by('-created_date')[:12]
        most_visited_products = Product.objects.filter(is_active = True, is_deleted = False).annotate(visit_count = Count('productvisit')).order_by('-visit_count')[:12]

        context['latest_products'] = Group_List(latest_products, 4)
        context['most_visited_products'] = Group_List(most_visited_products, 4)
        print(Group_List(latest_products, 4))

        return context


class Site_Header_Component_View(TemplateView):
    template_name = 'shared/components/header.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting = True).first()
        context['site_setting'] = setting
        return context

class Site_Footer_Component_View(TemplateView):
    template_name = 'shared/components/footer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Todo add is active later and filter by is active to show
        footer_link_boxes = FooterLinkBox.objects.all()
        for item in footer_link_boxes:
            item.footerlink_set
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting = True).first()
        context['site_setting'] = setting
        context['footer_link_boxes'] = footer_link_boxes

        return context

class AboutUsView(TemplateView):
    template_name = 'Home_Module/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_setting : SiteSetting = SiteSetting.objects.filter(is_main_setting = True).first()
        context['site_setting'] = site_setting
        return context