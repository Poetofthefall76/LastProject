from django.shortcuts import get_object_or_404
from . import models, forms
from django.views.generic import ListView, \
    DetailView, CreateView

from .models import Product


class ProductList(ListView):
    model = models.Product
    template_name = "product/product_list.html"

    def get_queryset(self):
        return models.Product.objects.filter().order_by("-id")


class ProductDetail(DetailView):
    model = models.Product
    template_name = "product/product_detail.html"

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)


class CreateOrder(CreateView):
    template_name = "product/create_order.html"
    form_class = forms.OrderForm
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form=form)