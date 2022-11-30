from django.urls import path

from . import views

urlpatterns = [
    # path('<>', views.ProductDetailAPIView.as_view()),
    path('', views.product_create_view),
    path('<int:pk>/', views.Product_Detail_view),
]
