from django.shortcuts import render
#import timezone info, for published date
from django.utils import timezone
#import Post - imports Post model
from .models import Post
#deal with 404
from django.shortcuts import render, get_object_or_404

#query to get published posts, ordered by published date
#where 'posts' is the same of this query set

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    #parameter 'request' is everything we receive from the user via the internet
    #parameter 'blog/post_list.hmtl' gives the template filter
    #parameter {} is where we can add things for template to user

    #request comes in, checks dates of posts - sends to page post_list.html
    #those are the posts that are returned (rendered)

#post_detail view defined here
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
