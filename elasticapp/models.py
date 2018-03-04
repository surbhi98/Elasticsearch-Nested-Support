from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import BlogPoIndex

# Create your models here.

# Blogpost to be indexed into ElasticSearch


class Category(models.Model):
    name = models.CharField(max_length=100)


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    posted_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    p_category = models.ManyToManyField("Category", null= True, default="category")

    # Method for indexing the model
    def __str__(self):
        return self.title

    
    def indexing(self):
        obj = BlogPoIndex(
            meta={'id': self.id},
            author=self.author.username,
            posted_date=self.posted_date,
            title=self.title,
            text=self.text,
        
        )
        print(self.text)
        be = self.p_category.all()
        print(be)
        for i in be:
            print(i.name)
            obj.add_category(i.name)
        obj.save()
        ob = BlogPost.objects.get(id= self.id)
        obe = obj.p_category
        print(obe)
        print(obj.meta.id)
        return obj.to_dict(include_meta=True)


    
    
