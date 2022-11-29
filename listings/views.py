from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',{'bands': bands})

def band_detail(request,id):
    # we ask to return the 'band' object with the submited id from url  
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band':band} ) # passage de l'id au model