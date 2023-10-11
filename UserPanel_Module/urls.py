from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardClass.as_view(), name='UserPanel_Dashboard'),
    path('edit-profile', views.EditUserProfile.as_view(), name = 'EditProfile_page'),
    path('change-password', views.ChangePassword.as_view(), name = 'ChangePassword_page'),
    path('user-basket', views.User_Basket, name = 'user_basket_page'),
    path('my-shoppings-history', views.MyShops_History.as_view(), name = 'my_shopping_history'),
    path('my-shop-history-detail/<order_id>', views.Shop_History_Detail, name = 'my_shop_history_detail'),
    path('remove-item-basket', views.remove_order_detail, name = 'remove_item_in_basket_ajax'),
    path('change-item-count', views.Change_Order_Count, name = 'change_item_count_ajax'),

]