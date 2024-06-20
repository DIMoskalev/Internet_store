from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
