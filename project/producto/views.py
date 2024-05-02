from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.


def home(request):
    query = models.ProductoCategoria.objects.all()
    context = {"productos": query}
    return render(request, "producto/index.html", context)


def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")

    else:  # request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", {"form": form})
