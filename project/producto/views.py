from django.shortcuts import render
from . import models

def home(request):
    consulta_producto = models.Categoria.objects.all()
    context = {"productos": consulta_producto}
    return render(request,"producto/index.html", context)
