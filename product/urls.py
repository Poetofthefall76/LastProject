from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name="home-view"),
    path('<int:id>/', views.ProductDetail.as_view(), name="product-detail"),
    path('add-order/', views.CreateOrder.as_view(), name="create-order"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)