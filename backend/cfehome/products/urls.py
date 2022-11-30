from django.urls import path

from . import views

urlpatterns = [
    # path('<>', views.ProductDetailAPIView.as_view()),
    path('', views.product_create_view),
    path('<int:pk>/', views.Product_Detail_view),
    path('<int:pk>/update', views.Product_Update_view),
    path('<int:pk>/delete', views.Product_Delete_view),
]
