from django import forms
from . import models


class InstrumentosForm(forms.ModelForm):
    class Meta:
        model = models.Instrumento
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"})
        }


class InstrumentoAireForm(forms.ModelForm):
    class Meta:
        model = models.InstrumentoAire
        fields = "__all__"
        widgets = {
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class InstrumentoCuerdasForm(forms.ModelForm):
    class Meta:
        model = models.InstrumentoCuerdas
        fields = "__all__"
        widgets = {
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }
