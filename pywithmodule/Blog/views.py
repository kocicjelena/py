from django.shortcuts import render, render_to_response
from .models import Blog, Author, Entry
from django.http import Http404, HttpResponse
from django.template import RequestContext, loader
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Blog
from django.http import HttpResponse
from django.views.generic import View
from .forms import ContactForm
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html',
        {'errors': errors})
def contact2(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })
def contact3(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
def authorlist(request):
    obj_list = Author.objects.all()
    return render(request, 'authorlist.html', {'obj_list': obj_list})
def entry(request):
    m_list = Entry.objects.all()
    return render(request, 'template.html', {'m_list': m_list})
def item_edit(request):
    blog_list = Blog.objects.all()
    return render(request, 'template2.html', {'blog_list': blog_list})
class MyView(View):
    greeting = "Good Day"
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
class BookListView(ListView):
    model = Blog

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('pub_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_book.pub_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response
class AboutView(TemplateView):
    template_name = "about.html"
def posts(request):
    ent = Blog.objects.all()[:10]
    return render(request, 'index.html', {'posts' : ent})
def searchform(request):
    return render(request, 'search_form2.html')
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Entry.objects.filter(headline=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html',
        {'error': error})
def searchblog(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Blog.objects.filter(headline=q)
            return render(request, 'searchblog.html',
                {'books': books, 'query': q})
    return render(request, 'searchbform.html',
        {'error': error})
def bloglist(request):
    bloglist = Blog.objects.order_by('name')
    return render(request, 'book_list.html', {'bloglist': bloglist})
def searchh(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
def i(request):
    errors = []
    if 'q' and 'b' in request.GET:
        q = request.GET['q']
        b = request.GET['b']
        if not q and not b:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            blog = Blog.objects.create(name=q, tagline=b)
            blog.save()
            return render(request, 'print.html',
                {'blog': blog, 'query': q})
    return render(request, 'input.html',
        {'errors': errors})