# from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"
    # model = Contact
    # fields = ('name', 'phone', 'message',)
    # success_url = reverse_lazy('catalog:contacts')
