from django.shortcuts import render, redirect
from server.apps.posts.models import Post, Comment
from server.apps.posts.forms import PostForm
# Create your views here.
def main(request, *args, **kwargs):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        "posts" : posts,
        "comments" : comments
    }
    return render(request, "posts/main.html", context=context)

def post_create(request, *args, **kwargs):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            context = {
                'form': form,
            }
            return render(request, 'posts/post_create.html', context=context)
    form = PostForm()
    context = {
        "form" : form,
    }
    return render(request, "posts/post_create.html", context=context)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request, *args, **kwargs):
    req = json.loads(request.body)

    post_id = req['id'] 
    post = Post.objects.get(id=post_id)
    
    if post.like == True:
        post.like = False
        post.heartIcon = '<i class="fa-regular fa-heart"></i>' 
    else:
        post.like = True
        post.heartIcon = '<i class="fa-solid fa-heart"></i>'

    post.save()

    status = post.like
    return JsonResponse({'id': post_id, 'status': status})

@csrf_exempt
def create_comment_ajax(request, *args, **kwargs):
    req = json.loads(request.body)

    post_id = req['id']
    text = req['text']

    comment = Comment.objects.create(
        post = Post.objects.get(id=post_id),
        text = text
    )
    return JsonResponse({'post_id': post_id, 'comment_id': comment.id, 'text': comment.text})

@csrf_exempt
def del_comment_ajax(request, *args, **kwargs):
    req = json.loads(request.body)

    post_id = req['post_id']
    comment_id = req['comment_id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'post_id': post_id, 'comment_id': comment_id})

    
