from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, InnerDoc, Text, Nested, Date, Search, MultiSearch, analyzer, tokenizer
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models
from elasticsearch_dsl.query import MultiMatch, Match
from django.shortcuts import render, redirect





#from .forms import SearchForm
# Create a connection to ElasticSearch
connections.create_connection(hosts=['localhost'], timeout=20)

# ElasticSearch "model" mapping out what fields to index


class CategoryIndex(InnerDoc):
    name = Text()
    

class BlogPoIndex(DocType):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()
    p_category = Nested(CategoryIndex)

    class Meta:
        index = 'blogpo-index'

    def add_category(self,name):
        print("adding..")
        #print(self.p_category.name)
        c = CategoryIndex(name=name)
        self.p_category.append(c)
        

    
    
        
# Bulk indexing function, run in shell
def bulk_indexing():
    BlogPoIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))



