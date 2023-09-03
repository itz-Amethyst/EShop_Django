from django.urls import path
from . import views

urlpatterns = [
    #! Function based view
    # path('', views.contact_us_page, name='contact_us')
    path('', views.ContactUsView.as_view(), name='contact_us'),
    path('create-profile/', views.CreateProfileView.as_view() , name = 'create_profile'),
    path('profiles/' , views.ProfilesView.as_view() , name = 'profiles')

]