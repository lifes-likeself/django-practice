#from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render # get_object_or_404
from .models import Post
# Create your views here.



def post_list(request):
    qs = Post.objects.all()

    # 1/0 ZeroDivisionError 500.

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q': q
    })

# 이해 나중에 잘 해보자...

def post_detail(request, id):

    post = Post.objects.get(id=id)

    return render(request, 'blog/post_detail.html', {
        'post': post
    })


