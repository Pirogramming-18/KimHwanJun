from django.shortcuts import render, redirect
from server.apps.posts.models import Post, Dev
# Create your views here.
def posts_main(request, *args, **kwargs):
    posts = Post.objects.all()

    if request.method == "GET":
        selected = request.GET.get('arrange')   
        if selected == 'register':
            posts = Post.objects.order_by('created_at')

        elif selected == 'current':
            posts = Post.objects.order_by('-created_at')

        elif selected == 'title':
            posts = Post.objects.order_by('title')

        elif selected == 'star':
            posts = Post.objects.order_by('star')
    
    context = {
        "posts":posts,
    }   
    return render(request, "posts/posts_main.html", context=context)

def posts_register_idea(request, *args, **kwargs):
    if request.method == "POST":
        devtoolName = Dev.objects.get(name=request.POST["devtool"])
        Post.objects.create(
            title=request.POST["title"],
            photo=request.FILES.get("photo"),
            content=request.POST["content"],
            interest=request.POST["interest"],
            devtool=devtoolName
        )
        return redirect("/")
        
    devtools = Dev.objects.all()
    context = {
        "devtools":devtools
    }
    return render(request, "posts/posts_register_idea.html", context=context)

def posts_idea_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    context = {
        "post":post
    }
    return render(request, "posts/posts_idea_detail.html", context=context)

def posts_tool_detail(request, pk, *args, **kwargs):
    dev = Dev.objects.get(id=pk)
    posts = Post.objects.all()
    context = {
        "dev":dev,
        "posts":posts
    }
    return render(request, "posts/posts_tool_detail.html", context=context)

def posts_idea_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

def posts_idea_update(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    devtools = Dev.objects.all()
    if request.method == "POST":
        post.title=request.POST["title"]
        post.photo=request.FILES.get("photo")
        post.content=request.POST["content"]
        post.interest=request.POST["interest"]
        if request.POST["devtool"]:
            devtoolName = Dev.objects.get(name=request.POST["devtool"])
            post.devtool = devtoolName
        post.save()
        return redirect(f"/posts/{post.id}/idea_detail")
    context = {
        "post":post,
        "devtools":devtools
    }
    return render(request, "posts/posts_idea_update.html", context=context)

def posts_tool_list(request, *args, **kwargs):
    devs = Dev.objects.all()
    context = {
        "devs":devs
    }
    return render(request, "posts/posts_tool_list.html", context=context)

def posts_register_tool(request, *args, **kwargs):
    if request.method == "POST":
        Dev.objects.create(
            name = request.POST["name"],
            kind = request.POST["kind"],
            content = request.POST["content"],
        )
        return redirect("/posts/tool_list")
    return render(request, "posts/posts_register_tool.html")

def posts_tool_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        dev = Dev.objects.get(id=pk)
        dev.delete()
    return redirect("/posts/tool_list")

def posts_tool_update(request, pk, *args, **kwargs):
    dev = Dev.objects.get(id=pk)
    if request.method == "POST":
        dev.name = request.POST["name"]
        dev.kind = request.POST["kind"]
        dev.content = request.POST["content"]
        dev.save()
        return redirect(f"/posts/{dev.pk}/tool_detail")
    context = {
        "dev":dev
    }
    return render(request, "posts/posts_tool_update.html", context=context)