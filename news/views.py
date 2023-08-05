from django.shortcuts import render
from .models import Blog,ContactInformation,ContactMessage
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
   info = ContactInformation.objects.all().first()
   
   if request.method == 'POST':
      
      name1  = request.POST.get('name')
      email1  = request.POST.get('email')
      subject1  = request.POST.get('subject')
      message1  = request.POST.get('message')
      
      contact = ContactMessage()
      
      contact.name = name1
      contact.email = email1
      contact.subject = subject1
      contact.message =message1
      
      contact.save()
         
      
      
   else:
      pass
   return render(request, 'contact_us.html',{'info':info}) 
