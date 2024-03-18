from django.shortcuts import render




# Create your views here.
def index(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def shop(request):
    return render(request, 'shop.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')

