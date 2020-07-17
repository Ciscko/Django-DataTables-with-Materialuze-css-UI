from django.shortcuts import render

# Create your views here.
def Articles(request):
    template_name = ''
    context = ''
    return render(request, 'articles/index.html', {
        'context' : context
    })
