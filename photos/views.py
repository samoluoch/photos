from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image

import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def image_of_day(request):
    date = dt.date.today()
    images = Image.todays_image()
    return render(request, 'all-news/today-news.html', {"date": date, "images": images})



# FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
def image_of_day(request):
    date = dt.date.today()
    images = Image.todays_image()
    return render(request, 'all-images/today-images.html', {"date": date, "images": images})


def image(request,image_id):
    try:
        images = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/image.html", {"image":images})