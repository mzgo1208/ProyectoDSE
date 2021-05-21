from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos', views.ProductListView.as_view(), name='producto-list'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='producto-detail')
]

