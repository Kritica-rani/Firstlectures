from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello Home Page")


def about(reques):
    return HttpResponse("hi from about")
