from .forms import PostForm
from .models import Hashtag, Post

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

def homepage(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'django_homepage/homepage.html', {'posts': posts})

@login_required()
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            hashtags = form.cleaned_data['hashtags']

            # Split hashtags by spaces (assuming space-separated hashtags)
            hashtag_list = hashtags.split()

            # Create a new Post instance and set the author
            post = Post.objects.create(
                author=request.user,  # Set the author to the currently logged-in user
                message=message
            )

            for hashtag_text in hashtag_list:
                # Get or create the Hashtag instance
                hashtag, created = Hashtag.objects.get_or_create(hashtags=hashtag_text)

                # Add the Hashtag to the Post
                post.hashtags.add(hashtag)

            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'django_homepage/upload_post.html', {'form': form})


def delete_post(request, post_id):
    # Retrieve the post to delete or return a 404 error if not found
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        # Check if the user has the permission to delete the post (e.g., they are the author of the post)
        print(request.user,post.author)
        if request.user == post.author:  # You need to adjust this condition based on your user model and how you track post ownership
            # Delete the post
            post.delete()
            return redirect('homepage')
