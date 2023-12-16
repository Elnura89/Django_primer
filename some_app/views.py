from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     rows = Post.objects.all()
#     context = {
#         'rows':rows
#     }
#     return render(request, 'index.html')

class Index(ListView):
    model = Post
    template_name = 'index.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
 
 
class BlogDeleteView(DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')