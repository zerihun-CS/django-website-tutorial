
from django.urls import path, include
from .views import home, blog,blog_detail, contact_us
urlpatterns = [
   
   path('', home, name="home_url"),
   path('news/',blog, name='blog_url'),
   path('contact/',contact_us, name='contact_us_url'),
   path('detail/<int:post_id>/',blog_detail,name='blog_detail_url')
   

]
