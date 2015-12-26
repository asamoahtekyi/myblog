from django.shortcuts import render, get_object_or_404
#from django.utils import timezone
from .models import Post
from datetime import datetime

def post_list(request):

    allposts=Post.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
         
    return render(request,'blog/post_list.html', {'allposts':allposts})


def post_detail(request, pk):

    allposts = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'allposts':allposts})

   

