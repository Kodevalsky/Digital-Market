from django.shortcuts import render

# Create your views here.

def HomeView(request):
    context={}
    return render(request, 'core/home.html', context)

def AboutView(request):
    context = {}
    return render(request, "core/about.html", context)

def ContactView(request):
    context = {}
    return render(request, "core/contact.html", context)