from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm


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

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_date')
        upvoted = False
        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        downvoted = False
        if post.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html', {
                "post": post,
                "comments": comments,
                "commented": True,
                "commented": False,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "comment_form": CommentForm()
            },)


class PostUpVotes(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostDownVotes(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.downvotes.filter(id=request.user.id).exists():
            post.downvotes.remove(request.user)
        else:
            post.downvotes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreate(View):
    model = Post

    def get(self, request):
        post_form = PostForm()
        context = {"post_form": post_form}
        return render(request, 'post_create.html', context)

    def post(self, request, *args, **kwargs):

        post_form = PostForm(request.POST)

        if post_form.is_valid():

            post_form.instance.author = request.user.username
            post_form.instance.status = 0
            post = post_form.save(commit=False)
            post.post = post
            post.save()
            return HttpResponseRedirect('/post_detail')

        context = {'post_form': post_form}
        return render(request, 'post_create.html', context)
