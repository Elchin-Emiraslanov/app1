from django.shortcuts import render, HttpResponse
from goods.models import*
# Create your views here.
def index(request):


    context={
        "title": "home - General",
        'content': 'maqazin mebeli home',
    }
    return render(request, "main/index.html", context)

def about(request):
    context={
    "title": "home - haqqimizda",
    'content': 'haqqimizda',
    'text_on_page' : "magaza mebellere aiddir"
}
    return render(request, "main/about.html", context)
