from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        "title": "home",
        "conf": "hello is"
    }
    return render(request, "main/index.html", context)