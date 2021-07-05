from App1.models import Contactdata,Blog
import App1

from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404, resolve_url
from django.core.paginator import Paginator

# Create your views here.

def Home(request):
    return render(request,'App1/home.html')

def Team(request):
    return render(request,'App1/team.html')

def Contact(request):
    if request.method=="POST":
        form=Contactdata(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=Contactdata(name=name,email=email,phone=phone,message=message)
        data.save()
        return redirect('Home')
    else:
        form=Contactdata()
    return render(request,'App1/contact.html')

def Price(request):
    return render(request,'App1/price.html')


def blog(request):
    posts=Blog.objects.all().order_by('-posted_date')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'App1/blog.html', context)

    
def post(request, post_id=None):
    post=get_object_or_404(Blog,id=post_id)
    context={
        'post':post
        }        
    return render(request, 'App1/post.html',context)

def fsd(request):
    if request.method=="POST":
        form=Contactdata(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=Contactdata(name=name,email=email,phone=phone,message=message)
        data.save()
    return render(request,'App1/fsd.html')

def dm(request):
    if request.method=="POST":
        form=Contactdata(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=Contactdata(name=name,email=email,phone=phone,message=message)
        data.save()
        
    return render(request,'App1/dm.html')

