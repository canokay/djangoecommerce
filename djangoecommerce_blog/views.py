from django.shortcuts import render
from djangoecommerce_blog.models import BlogCategory
from djangoecommerce_blog.models import Blog,Hashtag

def IndexView(request):
    return render(request, 'blog/index.html')

def BlogListView(request):
    context = {
        "blog": Blog.objects.order_by('-created_date')
    }
    return render(request, 'blog/blog.html', context)


def CategoryListView(request,category_slug):
    category = BlogCategory.objects.get(category_slug=category_slug)
    blog = Blog.objects.filter(category=category).order_by('-created_date')
    context = {
        "category": category,
        "blog": blog
    }
    return render(request, 'blog/category.html',context)


def HashtagListView(request,hashtag):
    hashtag = Hashtag.objects.get(hashtag=hashtag)
    blog = Blog.objects.filter(hashtag=hashtag).order_by('-created_date')
    context = {
        "hashtag": hashtag,
        "blog": blog

    }
    return render(request, 'blog/hashtag.html',context)

def BlogDetailView(request,slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        "blog": blog
    }
    return render(request, 'blog/blog-single.html',context)
