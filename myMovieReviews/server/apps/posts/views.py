from django.shortcuts import render, redirect
from server.apps.posts.models import Post
# Create your views here.

def posts_main(request, *args, **kwargs):
    return render(request, "posts\post_main.html")

def posts_review(request, *args, **kwargs):
    posts = Post.objects.all()
    return render(request, "posts\post_review.html", {"posts": posts})

def posts_create(request, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title = request.POST["title"],
            year = request.POST["year"],
            genre = request.POST["genre"],
            rate = request.POST["rate"],
            runningtime = request.POST["runningtime"],
            content = request.POST["content"],
            director = request.POST["director"],
            act = request.POST["act"],
        )
        return redirect("/review")
    return render(request, "posts\post_create.html")

def posts_detail(request, pk, *args, **kwargs):
    post = Post.objects.all().get(id=pk)
    return render(request, "posts\post_detail.html", {'post':post})

def posts_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.all().get(id=pk)
        post.delete()
    return redirect("/review")

def posts_update(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.year = request.POST["year"]
        post.genre = request.POST["genre"]
        post.rate = request.POST["rate"]
        post.runningtime = request.POST["runningtime"]
        post.content = request.POST["content"]
        post.director = request.POST["director"]
        post.act = request.POST["act"]
        post.save()
        return redirect(f"/review/{post.id}")
    
    return render(request, "posts/post_update.html", {"post":post})