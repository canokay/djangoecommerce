from django.shortcuts import render, redirect
from djangoecommerce_web.serializers.homepage import ProductListSerializer, BlogListSerializer, ProductDetailSerializer, BlogDetailSerializer
from djangoecommerce_app.models import User, City, CompanyAddress, CompanyFeature,Card,Order, Company, ProductCategory,  Product, ProductImage, ProductBrand, Contact
from djangoecommerce_blog.models import Blog
from djangoecommerce_web.forms import ContactForm

def IndexView(request):
    context={
        "blog":BlogListSerializer(Blog.objects.all()[:3], many=True).data,
        "product":ProductListSerializer(Product.objects.all(), many=True).data
    }
    return render(request, 'web/index.html',context)


def ProductDetailView(request,id):
    context = {
        "product":ProductDetailSerializer(Product.objects.get(id=id), many=True).data,
    }
    return render(request, 'web/product/product-detail.html',context)


def BlogDetailView(request,slug):
    context = {
        "blog":BlogDetailSerializer(Blog.objects.get(slug=slug), many=True).data,
    }
    return render(request, 'web/blog-single.html',context)


def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        Contact = form.save(commit=True)
        return redirect("djangoecommerce_web:contact")
    context = {
        "form": form
    }
    return render(request, 'web/contact.html',context)
