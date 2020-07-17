from django.shortcuts import render

# Create your views here.
def Blogs(request):
    data = 'This is my blog'
    return render(request, 'blogs/index.html', {
        'context': data
    })