from django.shortcuts import render, redirect
from .forms import post_form
from django.contrib import messages
from .models import post_model

def post_home(request):
    
    
    if request.method == "POST":
        form = post_form(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()  # Actually save the message
            posts = post_model.objects.all()
            messages.success(request, "Post created successfully")
            return redirect("post_home")
        else:
            print("no")
            messages.error(request, "Please fill in all required fields")
    else:
        posts = post_model.objects.all()
        form = post_form()
    posts = post_model.objects.all()
    
    return render(request, "post_home.html", {"posts": posts, "form": form})
def create_post(request):
    if request.method=="POST":
        form=post_form(request.POST)
        if form.is_valid():
            form.save()
            print("dd")
            return redirect("post_home")
        else:
            messages.success(request, "Please fill in")
            print("why")
            return render(request, ("create_post.html"), {"form": form})
    else:
        form=post_form()
        return render(request, ("create_post.html"), {"form": form})
