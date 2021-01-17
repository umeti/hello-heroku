from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from . import api_proxy

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def bili_video_info(req,id,ext):
    if ext == ".json":
        body = api_proxy.bili_video()
    else:
        body = api_proxy.bili_video_simple(id)

    return HttpResponse(body)


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
