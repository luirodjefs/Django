from django.shortcuts import render

def mostrar_acerca(request):
    return render(request, 'about.html')