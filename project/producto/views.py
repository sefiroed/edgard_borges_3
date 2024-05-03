from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.


# def home(request):
#     query = models.ProductoCategoria.objects.all()
#     context = {"productos": query}
#     return render(request, "producto/index.html", context)
# def home(request):
#     categorias_query = models.ProductoCategoria.objects.all()
#     instrumentos_query = models.InstrumentosDeCuerdas.objects.all()
#     context = {
#         "productos": categorias_query,
#         "instrumentos_de_cuerdas": instrumentos_query
#     }
#     return render(request, "producto/index.html", context)


# def productocategoria_create(request):
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect("producto:home")

#     else:  # request.method == "GET"
#         form = forms.ProductoCategoriaForm()
#     return render(request, "producto/productocategoria_create.html", {"form": form})


# def instrumentos_de_cuerdas(request):
#     if request.method == "POST":
#         form = forms.InstrumentosDeCuerdasForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect("producto:home")
#     else:  # request.method == "GET"
#         form = forms.InstrumentosDeCuerdasForm()
#     return render(request, "producto/instrumentos_de_cuerdas.html", {"form": form})


def home(request):
    query = models.Instrumento.objects.all()
    context = {"productos": query}
    return render(request, "producto/index.html", context)


def instrumentos_de_cuerdas(request):
    if request.method == "POST":
        form = forms.InstrumentosForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")

    else:  # request.method == "GET"
        form = forms.InstrumentosForm()
    return render(request, "producto/instrumentos_de_cuerdas.html", {"form": form})
