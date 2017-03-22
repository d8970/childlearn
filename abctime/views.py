#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings


def index(request):
    with open("content.txt", "r") as f:
        txt=f.readline()
        print txt
    return HttpResponse(txt)



'''
    try:
        #with open("media.png", "rb") as f:
        with open("mortgage1.jpg", "rb") as f:
            print "static url %s" % settings.MEDIA_ROOT
            return HttpResponse(f.read(), content_type="image/jpg")
            #return HttpResponse(f.read(), content_type="image/png")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
'''

