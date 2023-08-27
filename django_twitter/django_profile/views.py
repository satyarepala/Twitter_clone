from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Post
from .forms import UserProfileForm, PostForm

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    posts = Post.objects.filter(user=request.user)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('profile')
    else:
        post_form = PostForm()

    return render(request, 'profileapp/profile.html', {'user_profile': user_profile, 'posts': posts, 'post_form': post_form})

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user == request.user:
        post.delete()
    return redirect('profile')
