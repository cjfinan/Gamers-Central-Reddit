from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_search/', views.PostSearch, name='post_search'),
    path('edit_user/', views.UserEdit.as_view(), name='edit_user'),
    path('<int:pk>/profile/', views.UserProfilePage.as_view(), name='view_profile'),
    path('<int:pk>/edit_profile_page/', views.EditProfilePage.as_view(), name='edit_profile'),
    path('create_profile_page/', views.CreateProfilePage.as_view(), name='create_profile'),
    path('password/', views.ChangePassword.as_view()),
    path('password_success/', views.password_success, name="password_success"),
    path('upvote/<slug:slug>', views.PostUpVotes.as_view(), name="post_up_vote"),
    path('downvote/<slug:slug>', views.PostDownVotes.as_view(), name="post_down_vote"),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('post_update/<slug:slug>', views.PostUpdate.as_view(), name='post_update'),
    path('post_delete/<slug:slug>', views.PostDelete.as_view(), name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
