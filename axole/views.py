from django.shortcuts import render, redirect
from .models import Blog,About
from .forms import Subform,Comentsform,ContactForm
# Create your views here.


def index(request):
    return render(request,'index.html')


def blog(request):
    blog = Blog.objects.all()
    sub = Subform(request.POST or None)
    if sub.is_valid():
        sub.save()
    cxt = {
        "blogs": blog,
        "sub":sub
    }
    return render(request,'blog.html',cxt)


def detail(request,pk):
    blog = Blog.objects.get(id=pk)
    comments = Comentsform(request.POST or None)
    if comments.is_valid():
        com = comments.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    cxt = {
        "blog" : blog,
        'comments':comments
    }
    return render(request,'blog-single.html',cxt)


def about(request):
    about = About.objects.all()
    cxt = {
        "about":about
    }
    return render(request,'about.html',cxt)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    cxt = {
        'form': form
    }
    return render(request,'contact.html',cxt)
