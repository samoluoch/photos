from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


# def image(request,image_id):
#     try:
#         image = Image.objects.get(id = image_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"image.html", {"image":image})