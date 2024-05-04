from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.


def home(request):
    query = models.Instrumento.objects.all()
    context = {"productos": query}
    return render(request, "producto/index.html", context)


def productocategoria_create(request):
    if request.method == "POST":
        form = forms.InstrumentosForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")

    else:  # request.method == "GET"
        form = forms.InstrumentosForm()
    return render(request, "producto/productocategoria_create.html", {"form": form})


def instrumentos_de_cuerdas(request):
    if request.method == "POST":
        form = forms.InstrumentoCuerdasForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")

    else:  # request.method == "GET"
        form = forms.InstrumentoCuerdasForm()
    return render(request, "producto/instrumentos_de_cuerdas.html", {"form": form})


def instrumentos_de_aire(request):
    if request.method == "POST":
        form = forms.InstrumentoAireForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")

    else:  # request.method == "GET"
        form = forms.InstrumentoAireForm()
    return render(request, "producto/instrumentos_de_aire.html", {"form": form})
