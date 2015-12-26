from django.shortcuts import render
#from django.utils import timezone
from .models import Post
from datetime import datetime

def post_list(request):

    allposts=Post.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
         
    return render(request,'blog/post_list.html', {'allposts':allposts})

