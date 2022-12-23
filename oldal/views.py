from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Oldal
from .models import Cimek

def home(request):
    hatters = Oldal.objects.all()
    cimek = Cimek.objects.all()
    return render(request, 'oldal/home.html', {'cimek': cimek, 'hatters': hatters})
