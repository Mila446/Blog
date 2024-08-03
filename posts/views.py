from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts': posts})

@login_required
def post(request,pk):
    posts = Post.objects.get(id=pk)
    comments = posts.comments.all()
    if request.method=='POST':
        if request.POST.get("form_id")=='deletion':
            comments.filter(id=request.POST['comment_id']).delete()
            form = CommentForm()
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = posts
                comment.author = request.user
                comment.save()
                return redirect('post', pk=pk)
            else:
                form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'post.html', {'posts': posts, 'comments': comments, 'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Error! Please try again.')
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})