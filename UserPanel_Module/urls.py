from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardClass.as_view(), name='UserPanel_Dashboard'),
    path('edit-profile', views.EditUserProfile.as_view(), name = 'EditProfile_page'),
    path('change-password', views.ChangePassword.as_view(), name = 'ChangePassword_page'),
    path('user-basket', views.User_Basket, name = 'user_basket_page')

]