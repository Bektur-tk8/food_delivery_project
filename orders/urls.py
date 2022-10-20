from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('update-status/<int:pk>/', views.OrderStatusUpdateView.as_view(), name='order_status_update')
    
    
]