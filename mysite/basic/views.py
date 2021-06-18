from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')
# return HttpResponse("This  is home pages")

# Create your views here.
