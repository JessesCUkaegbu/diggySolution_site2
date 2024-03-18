from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('shop/', views.shop, name="shop"),
    path('blog/', views.blog, name="blog"),
    path('blog_detial/', views.blog_detail, name="blog-detail"),
    path('contact/', views.contact, name="contact"),
]