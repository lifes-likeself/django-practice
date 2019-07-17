from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#def mysum(request, x):
    #request : HttpRequest
    #return HttpResponse(int(x))

def post_list(request):
    return render(request, 'blog/post_list.html')

# Fuction Based View
def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
<p>{name}</p>
<p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>
    '''.format(name=name))

def post_list2(request):
    name = '공유'
    response = render(request, 'dojo/post_list2.html', {'name' : name})
    return response

# Class Based View next time~



