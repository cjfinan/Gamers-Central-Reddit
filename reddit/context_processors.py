from reddit.models import Post
from django.shortcuts import get_object_or_404


def votes(request):
    # queryset = Post.objects.filter(status=1)
    # post = get_object_or_404(queryset, slug=slug)
    upvoted = False
    # if post.upvotes.filter(id=self.request.user.id).exists():
    #     upvoted = True
    downvoted = False
    # if post.downvotes.filter(id=self.request.user.id).exists():
    #     downvoted = True
    return {"upvoted": upvoted,
            "downvoted": downvoted, }

