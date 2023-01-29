from django.shortcuts import render


def index(request):
    context = {
        'title': 'Elit Photography'
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    context = {
        'title': 'Фото'
    }
    return render(request, 'mainapp/products.html', context=context)
#
#
# def contacts(request):
#     return render(request, 'mainapp/contacts.html')

# Create your views here.
