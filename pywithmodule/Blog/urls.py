from django.conf.urls import patterns, include, url
from Blog import views
from Blog.views import posts, search, searchform, i, searchh, MyView, BookListView, bloglist, item_edit, authorlist, entry, contact, contact2, contact3, searchblog
from django.conf.urls import patterns
from .views import AboutView
from django.conf.urls import patterns
from .views import BookListView
from django.conf.urls import patterns
from .views import MyView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^year_archive/(?P<year>\d{4})/$', views.year_archive),
	#url(r'^foo/$', views.foo_view),
    #url(r'^bar/$', views.bar_view),
	#url(r'^blog/entries/$', views.entry_list),
	url(r'^about/', MyView.as_view()),
	url(r'^list/$', BookListView.as_view()),
	url(r'^bloglist/$', views.bloglist),
	url(r'^entry/$', views.entry),
	#url(r'^about/', AboutView.as_view()),
	url(r'^contact/$', views.contact),
	url(r'^contact2/$', views.contact2),
	url(r'^contact3/$', views.contact3),
	url(r'^posts/$', views.posts),
	url(r'^authorlist/$', views.authorlist),
	url(r'^date/$', views.item_edit),
	url(r'^searchform/$', views.searchform),
	url(r'^search/$', views.search),
	url(r'^searchblog/$', views.searchblog),
	url(r'^searchh/$', views.searchh),
	url(r'^i/$', views.i),
	#url(r'^blogs_of_author/$', views.blogs_of_author),
	#url(r'^fo/$', views.fo),
	#url(r'^f/$', views.f),
	#url(r'^blog/edit/(?P<id>.*)$', 'views.edit_view', name='item_edit'),
    #url(r'^blog/remove/(?P<id>.*)$', 'views.remove_view', name='item_remove'),
    # ...
	)