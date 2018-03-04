from django.contrib import admin
from .models import BlogPost, Category

# Register your models here.

# Need to register my BlogPost so it shows up in the admin
admin.site.register(BlogPost)
admin.site.register(Category)

