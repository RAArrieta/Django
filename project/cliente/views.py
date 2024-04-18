from django.shortcuts import render
from . import models

def home(request):
    consulta_cliente = models.Cliente.objects.all()
    context = {"clientes": consulta_cliente}
    return render(request,"cliente/index.html", context)
