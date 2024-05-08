from django.shortcuts import render


def home_page(request):
    return render(request, "catalog/home_page.html")


def contact_info(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    message = request.POST.get("message")
    print(name, phone, message)
    return render(request, "catalog/contact_info.html")
