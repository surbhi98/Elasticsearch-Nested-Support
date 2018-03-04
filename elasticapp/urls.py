from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sh/(?P<title>.+)/$', views.sh, name='sh'),
    
        

]
