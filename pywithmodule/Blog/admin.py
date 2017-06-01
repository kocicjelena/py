from .models import Blog, Author, Entry
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#class contactAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)