from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_search/', views.PostSearch, name='post_search'),
    path('edit_profile/', views.UserEdit.as_view(), name='edit_profile'),
    path('upvote/<slug:slug>', views.PostUpVotes.as_view(), name="post_up_vote"),
    path('downvote/<slug:slug>', views.PostDownVotes.as_view(), name="post_down_vote"),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
