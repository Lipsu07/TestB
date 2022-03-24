from re import template
from django.shortcuts import render,HttpResponse
from django.views.generic import ListView, DetailView , CreateView, UpdateView
from .models import Post
# Create your views here.
#def index(request):
    #return HttpResponse('This is home')
    #return render(request,'index.html')
class IndexView(ListView):
    model =Post
    template_name ='index.html'

class ArticleView(DetailView):
    model =Post
    template_name ='article-details.html'

class AddPostView(CreateView):
    model =Post
    template_name ='addpost.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model =Post
    template_name ='updatepost.html'
    fields = '__all__'
