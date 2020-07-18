from django.shortcuts import render
from .models import Post
'''
posts=[
	{
		'author': 'Sharath',
		'title': 'Blog Post 1',
		'content': 'First post Content',
		'date_posted': 'May 6,2020',
	},
	{	'author': 'Akash',
		'title': 'Blog Post 2',
		'content': 'Second post Content',
		'date_posted': 'May 7,2020',
	}
]
'''

def home(request):
	context={
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html',{'title':'about'})
