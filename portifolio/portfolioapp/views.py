from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Post, Comment  # Import the Post and Comment models

def comment(request, id):
    # Retrieve the post object based on the provided ID
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        # Use the request.POST data to initialize the CommentForm
        cf = CommentForm(request.POST)
        if cf.is_valid():
            # Extract the content from the form
            content = cf.cleaned_data['content']
            # Create a new Comment object and associate it with the post and user
            comment = Comment.objects.create(post=post, user=request.user, content=content)
            # Save the comment to the database
            comment.save()
            # Redirect to the post's detail view
            return redirect(post.get_absolute_url())
    else:
        # If the request method is not POST, initialize an empty CommentForm
        cf = CommentForm()
       
    # Prepare the context to pass to the template
    context = {
        'comment_form': cf,
        'post': post,  # Pass the post object to the template
    }
    # Render the template with the provided context
    return render(request, 'comment.html', context)
