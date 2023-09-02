from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"base.html")

def feed(request):
    return render(request,"feed.html")