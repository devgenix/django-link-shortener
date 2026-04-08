from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortenedURL

def home(request):
    if request.method == "POST":
        url = request.POST.get("url")
        obj = ShortenedURL.objects.create(original_url=url)
        return render(request, "shortener/home.html", {"short_url": request.build_absolute_uri('/') + obj.short_code})
    return render(request, "shortener/home.html")

def redirect_url(request, short_code):
    obj = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(obj.original_url)
