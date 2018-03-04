from .models import BlogPost
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .search import BlogPoIndex


# Signal to save each new blog post instance into ElasticSearch










@receiver(post_save, sender=BlogPost)
def index_post(sender, instance, **kwargs):
    print(sender)
    #print(action)
    b = instance.p_category.filter(id=83)
    print(b)
    for i in b:
        print(i.name)
    print("...................signal......................")
    instance.indexing()

def p_category_changed(sender, instance, action, pk_set, **kwargs):
    print('changed')
    print(pk_set)
    for i in pk_set:
        print(i)
    if(action=="post_add"):
        print(instance)
        print(action)
        b= instance.p_category.all()
        for i in b:
            print(i.name)
        print("......................................................")
        obj = BlogPostIndex(
            meta={'id': instance.id},
            author=instance.author.username,
            posted_date=instance.posted_date,
            title=instance.title,
            text=instance.text,
        
        )
        for i in pk_set:
            b= instance.p_category.filter(id=i)
            for j in b:
                obj.add_category(j.name)

        obj.save()
        return obj.to_dict(include_meta=True)
            
        


        #instance.indexing()

m2m_changed.connect(p_category_changed, sender = BlogPost.p_category.through)

