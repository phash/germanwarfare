from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Fahrzeug
from .models import Waffe


def index(request):
    latest_fahrzeug_list = Fahrzeug.objects.order_by('-pub_date')[:5]
    context = {'latest_fahrzeug_list': latest_fahrzeug_list}
    return render(request, 'compare/index.html', context)

def vergleich(request, fahrzeug_id1, fahrzeug_id2, waffe_id1, waffe_id2):
    tank1 = Fahrzeug.objects.get(id=fahrzeug_id1)
    tank2 = Fahrzeug.objects.get(id=fahrzeug_id2)
    waffe1 = Waffe.objects.get(id=waffe_id1)
    waffe2 = Waffe.objects.get(id=waffe_id2)

    context ={'tank1':tank1, 'tank2':tank2, 'waffe1':waffe1, 'waffe2':waffe2 }
    response = "Vergleich von %s und %s"
    return render(request, 'compare/vergleich.html', context)

def detail(request, fahrzeug_id):
    return HttpResponse("You're looking at question %s." % fahrzeug_id)