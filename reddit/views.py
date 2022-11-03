from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_date')
    template_name = 'index.html'
    paginate_by = 10


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_date')
        upvoted = False
        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        downvoted = False
        if post.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        return render(
            request,
            'post_detail.html', {
                "post": post,
                "comments": comments,
                "commented": False,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "comment_form": CommentForm()
            },)
