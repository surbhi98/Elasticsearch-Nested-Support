from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import SearchForm
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search, MultiSearch
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models
from elasticsearch_dsl.query import MultiMatch, Match
from django.shortcuts import render, redirect
# Create your views here.
from .search import *
from .search import BlogPoIndex
from django.db.models import Q,F
from django.http import JsonResponse
from .models import BlogPost, Category

def sh(request, title):
    lis=[]

    s = Search().query("match_phrase_prefix", title=title)
    response= s.execute()
    print(response)
    for hit in response:
        print(hit.author)
        lis.append(hit.title)
    if lis:
        return JsonResponse(lis, safe=False)
    
    s = Search.from_dict(
        {
            "query": { "bool": { "must":[
            
            
        {"nested": {
            "path": "p_category",
            "query": {
              "bool": {
                "must": [
                  {
                    "match_phrase_prefix": {
                      "p_category.name": title
                    }
                  }
                  
                ]
              }
            },
            "inner_hits": {
            
               
                }
          }}]}}})  
    
    
    re = s.execute()
    a = re["hits"]['total']
    print(a)
    i=0
    if re:
        for h in re:
            cat = re["hits"]["hits"][i]["inner_hits"]["p_category"]["hits"]["hits"][0]["_source"]["name"]
                
            titl = re["hits"]["hits"][i]["_source"]["title"]
                #titl = re["hits"]["hits"][i]["_source"]["state"]
            print("..................................staate.....................")
            st = titl + " belongs to " + cat + " category"
                 #print(titl)
            print(st)
            lis.append(st)
            i=i+1

    
    if lis:
        print(lis)
        return JsonResponse(lis, safe= False)
    else:
        return HttpResponse("NOT FOUND")


def home(request):
    return render(request,'base.html')


