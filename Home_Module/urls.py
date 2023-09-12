from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('about-us' , views.AboutUsView.as_view() , name = 'about_page') ,

    # path('site-header', views.site_header_partial, name="site_header_partial")
]