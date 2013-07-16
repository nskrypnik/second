
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import Post

def archive(request):
    posts=Post.objects.all()
    t=loader.get_template('archive.html')
    c=Context({'posts': posts})
    return HttpResponse(t.render(c))
