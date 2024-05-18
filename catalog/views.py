from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Contacts


def home_page(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
    }
    return render(request, "catalog/home_page.html", context)


def contact_info(request):
    contact_list = Contacts.objects.all()
    context = {
        'object_list': contact_list
    }

    name = request.POST.get("name")
    phone = request.POST.get("phone")
    message = request.POST.get("message")
    print(name, phone, message)
    return render(request, "catalog/contact_info.html", context)


def product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product
    }
    return render(request, "catalog/product_page.html", context)
