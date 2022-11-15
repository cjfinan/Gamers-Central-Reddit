from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Post, UserProfile, User
from django.db.models import Q
from .forms import CommentForm, CreatePostForm, EditUserProfileForm, ChangePasswordForm, CreateProfileForm, UpdatePostForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


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
        voted = False
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
        elif post.downvotes.filter(id=request.user.id).exists():
            post.downvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class PostDownVotes(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.downvotes.filter(id=request.user.id).exists():
            post.downvotes.remove(request.user)
        elif post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        else:
            post.downvotes.add(request.user)
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class PostCreate(SuccessMessageMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post_create.html'
    success_message = 'Your Post has been submitted and now is awaiting approval.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'post_update.html'
    success_message = 'Your Post has successfully been updated.'


class PostDelete(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_message = 'Your Post has successfully been deleted.'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)
    

def PostSearch(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(Q(content__icontains=searched) | Q(title__icontains=searched))
        return render(
            request,
            'post_search.html',
            {'searched': searched, 'posts': posts})
    else:
        return render(request, 'post_search.html')


class UserEdit(SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = 'edit_user.html'
    success_url = reverse_lazy('home')
    success_message = 'Settings successfully changed.'

    def get_object(self):
        return self.request.user


class ChangePassword(SuccessMessageMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('home')
    success_message = 'Password successfully changed.'


class UserProfilePage(DetailView):
    model = UserProfile
    template_name = 'view_profile.html'

    def get_context_data(self, *args, **kwargs):

        selected_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        user_posts = Post.objects.filter(author=selected_user.user)

        context = super().get_context_data(*args, **kwargs)

        context["selected_user"] = selected_user
        context["user_posts"] = user_posts
        return context


class EditProfilePage(SuccessMessageMixin, generic.UpdateView):

    model = UserProfile
    template_name = 'edit_profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('home')
    success_message = 'Profile successfully changed.'


class CreateProfilePage(SuccessMessageMixin, CreateView):
    model = UserProfile
    form_class = CreateProfileForm
    template_name = 'create_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
