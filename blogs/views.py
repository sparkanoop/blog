from django.core import serializers
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Post
from .forms import PostForm
from django.shortcuts import render


class ListPosts(APIView):
	"""
	View to list all posts in the system.
	"""

	def get(self, request):
	    """
	    Return a list of all blogs.
	    """
	    posts = [post for post in Post.objects.filter(public=True)]

	    return render(request, 'posts.html', {"posts": posts})


class UserPostLitView(APIView):
	"""
	View to list all posts in the system.
	"""

	def get(self, request , username):
	    """
	    Return a list of all posts.
	    """
	    form = PostForm()
	    user = User.objects.get(username=username)
	    posts = user.posts.all()

	    return render(request, 'posts.html', {"posts": posts ,'form':form})


	def post(self, request, username):
	    form = PostForm(data=request.DATA)
	    user = User.objects.get(username=username)
	    posts = user.posts.all()

	    if form.is_valid():
	        post = form.save(commit=False)
	        post.author = request.user
	        post.public = True
	        post.published = datetime.now()
	        post.save()
	    else:
	    	form = PostForm()
	    return render(request, 'posts.html', {"posts": posts ,'form':form})


class UserPostDetailView(APIView):
	"""
	View to list all posts in the system.
	"""

	def get(self, request , username , post_id):
	    """
	    Return a list of all posts.
	    """
	    form = PostForm()
	    user = User.objects.get(username=username)
	    post = Post.objects.get(id=post_id)
	    if post.author != user:
	    	return 
	    posts = user.posts.all()

	    return render(request, 'posts.html', {"posts": posts ,'form':form})


	def post(self, request, username):
	    form = PostForm(data=request.DATA)
	    user = User.objects.get(username=username)
	    posts = user.posts.all()

	    if form.is_valid():
	        post = form.save(commit=False)
	        post.author = request.user
	        post.public = True
	        post.published = datetime.now()
	        post.save()
	    else:
	    	form = PostForm()
	    return render(request, 'posts.html', {"posts": posts ,'form':form})	    




