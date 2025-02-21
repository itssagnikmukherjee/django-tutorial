from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Screen")

def about(request):
    return HttpResponse("About Screen")