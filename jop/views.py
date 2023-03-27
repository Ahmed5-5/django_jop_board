from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def jop_list(request):
    jop_list = jop.objects.all()
    
    paginator = Paginator(jop_list,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    con = {'jops': page_obj}   #template name
    return render(request,'jop/jop_list.html', con)


def jop_detail(request, id):
    jop_detail = jop.objects.get(id= id)

    con = {'jop': jop_detail}
    return render(request,'jop/jop_detail.html',con)