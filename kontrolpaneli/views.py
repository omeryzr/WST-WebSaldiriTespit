from django.http import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from kontrolpaneli.models import *



def kayit_ekle(request):
    if request.method=='POST':
        adi=request.POST.get('adi')


        kyt= kayit1(adi=adi)
        kyt.save()
        return HttpResponse('sadsad')
    else:
        return render_to_response('deneme.html', context_instance=RequestContext(request))
