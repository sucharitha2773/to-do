from django.shortcuts import render,redirect,get_object_or_404
from main.models import Post
from main.forms import PostForm
from django.contrib import messages

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            messages.info(request, 'Your post is added successfully!')

            return redirect('postlist')
    else:
        form = PostForm()
    return render(request,'main/create or edit post.html',{'form':form})


# curd = c => temp + view +form + url + model
# curd = u => model + view + form + url + model
# curd = r => model + view + url + html
# curd = d => model + view + url + html

def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'main/postlist.html', {'posts':posts})




def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.info(request, 'Your post is delete successfully!')

    return redirect('postlist')

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/postdetail.html', {'post': post})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            messages.info(request, 'Your post is updated successfully!')
            return redirect('postlist')
    else:
        form = PostForm(instance=post)
    return render(request,'main/create or edit post.html',{'form':form})
    
