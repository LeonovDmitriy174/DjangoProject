from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product, Contacts


class ProductListView(ListView):
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contact_info.html"
    model = Contacts

    def get(self, request, *args, **kwargs):
        object_list = self.model.objects.all()
        return render(request, self.template_name, {"object_list": object_list})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            print(f"Message from {name} (Tel: {phone}): {message}")
        return render(request, self.template_name)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:home_page")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:home_page")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home_page")
