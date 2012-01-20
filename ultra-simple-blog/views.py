from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from models import Post, PostForm
from django import forms
from datetime import datetime

def index(request):
	post_list = Post.objects.filter(date_deleted = None).order_by('-date_published')[:5]
	return render_to_response('ultra-simple-blog/index.html', {'post_list': post_list})

def new(request):
	c = {}
	c.update(csrf(request))
	
	if request.method == 'POST':
		p = Post(date_published=datetime.now())
		form = PostForm(request.POST, instance=p)

		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return HttpResponseRedirect('/')
			
	else:
		form = PostForm()
	
	return render_to_response('ultra-simple-blog/new.html',{'form': form,})
	
def show(request, post_id):
	post = Post.objects.get(pk=post_id)
	return render_to_response('ultra-simple-blog/show.html',{'post': post,})
	

def edit(request, post_id):
	c = {}
	c.update(csrf(request))

	if request.method == 'POST':
		p = Post.objects.get(pk=post_id)
		form = PostForm(request.POST, instance=p)

		if(form.is_valid()):
			post = form.save(commit=False)
			post.date_modified = datetime.now()
			post.save()
			
			return HttpResponseRedirect('/ultra-simple-blog/' + str(post.id) + '/')			
	
	else:
		post = Post.objects.get(pk=post_id)
		form = PostForm(instance=post)		

	return render_to_response('ultra-simple-blog/edit.html', {'form': form, 'post': post})
	
def delete(request, post_id):	
		post = Post.objects.get(pk=post_id)
		post.date_deleted = datetime.now()
		post.save()
		
		return HttpResponseRedirect('/')
	