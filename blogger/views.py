from django.shortcuts import render
from .models import Post

# Create your views here.
def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    template = 'blogger/tests.html'
    if request.method == 'POST':
        if 'next_post' in request.POST:
            next_post = request.POST.get('next_post')
            next_posst = Post.objects.get(pk=next_post)
            return render(request, template, {'post': next_posst})
        if 'previous' in request.POST:
            prev_post = request.POST.get('previous')
            previous_post = Post.objects.get(pk=prev_post)
            return render(request, template, {'post': previous_post})

    return render(request, template, {'post': post})
