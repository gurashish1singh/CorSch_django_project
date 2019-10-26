from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Pooja Noob',
        'title': 'Blog Post 1',
        'content': 'I am such a noob',
        'date_posted': 'October 24,2019'
    },

        {
        'author': 'Gushu',
        'title': 'Blog Post 2',
        'content': 'The post above is totally true!',
        'date_posted': 'October 25,2019'
    }
]
def home(request,):
    context = {
        'posts': posts,
    }
    template = 'blog/home.html'
    return render(request,template,context)

def about(request):
    context = {
        'title': 'About',
    }
    template = 'blog/about.html'
    return render(request,template,context)