from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
   return render(request, 'home.html')

def blog(request):
   news = Blog.objects.all()
   data = {'news_data':news}
   return render(request, 'blog.html',data)


def blog_detail(request,post_id):
   news = Blog.objects.get(id = post_id)
   return render(request, 'blog_detail.html',{'news_data':news})   
   
def contact_us(request):
   pass
