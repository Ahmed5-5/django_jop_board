from django.shortcuts import render
from .models import *
# Create your views here.

def jop_list(request):
    jop_list = jop.objects.all()
    
    con = {'jops': jop_list}   #template name
    return render(request,'jop/jop_list.html', con)


def jop_detail(request, id):
    jop_detail = jop.objects.get(id= id)

    con = {'jop': jop_detail}
    return render(request,'jop/jop_detail.html',con)