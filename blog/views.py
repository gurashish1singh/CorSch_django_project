from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )

from .models import *

# Create your views here.

# Hard coding data
# posts = [
#     {
#         'author': 'Pooja Noob',
#         'title': 'Blog Post 1',
#         'content': 'I am such a noob',
#         'date_posted': 'October 24,2019'
#     },

#         {
#         'author': 'Gushu',
#         'title': 'Blog Post 2',
#         'content': 'The post above is totally true!',
#         'date_posted': 'October 25,2019'
#     }
# ]

# def home(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#     }
#     template = 'blog/home.html'
#     return render(request,template,context)


# Django built in List view
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    template_name = 'blog/home.html'


# Django built in Detail view
class PostDetailView(DetailView):
    model = Post


# Django built in Create view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Chaning the built-in form validation to suit our needs of creating by logged in author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Django built in Update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Chaning the built-in form validation to suit our needs of creating by logged in author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # To check if the author wrote that post or not
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Django built in Delete view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    # To check if the author wrote that post or not
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'title': 'About',
    }
    template = 'blog/about.html'
    return render(request,template,context)