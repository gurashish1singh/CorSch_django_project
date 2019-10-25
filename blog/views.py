from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'October 25,2019'
    },

        {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'October 13,2019'
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

    }
    template = 'blog/about.html'
    return render(request,template,context)