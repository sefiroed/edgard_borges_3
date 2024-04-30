from django.shortcuts import render
from . import models, forms

# Create your views here.


def home(request):
    consulta_productos = models.ProductoCategoria.objects.all()
    context = {"productos": consulta_productos}
    return render(request, "producto/index.html", context)


def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()

    else:  # request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", {"form": form})
