from django.contrib import admin
from .models import Blog,ContactInformation, ContactMessage


admin.site.register(Blog)

admin.site.register(ContactInformation)

admin.site.register(ContactMessage)