from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image

import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')



# FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
def image_of_day(request):
    date = dt.date.today()
    images = Image.todays_image()
    return render(request, 'all-images/today-images.html', {"date": date, "images": images})


# View Function to present images from past days
def past_days_image(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(image_of_day)

    images = Image.days_image(date)
    return render(request, 'all-images/past-images.html', {"date": date, "images": images})



def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})


def image(request,image_id):
    '''
    This is a function that displays individual images
    '''
    try:
        images = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/image.html", {"image":images})


def all_images(request):
    images = Image.objects.all()

    return render(request, "all-images/today-images.html", {"images": images})