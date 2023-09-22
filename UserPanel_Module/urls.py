from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardClass.as_view(), name='UserPanel_Dashboard')
]