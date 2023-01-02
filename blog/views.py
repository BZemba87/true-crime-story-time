
"""
Imported functions for views code
"""

from django.shortcuts import render, get_object_or_404, reverse
from .models import Post
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from .forms import PostForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "liked": liked,
            },
        )


class PostLike(View):
  
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('home')


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = [
        'title',
        'slug',
        'author',
        'content',
        'status'
        ]
    success_url = reverse_lazy('home')
