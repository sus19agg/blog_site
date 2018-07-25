from blog import views
from django.conf.urls import url

urlpatterns = [
    url(r'^about/$',views.AboutView.as_view(),name="about"),
    url(r'^$',views.PostListView.as_view(),name="post_list"),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name="post_detail"),
    url(r'^post/create/$',views.PostCreateView.as_view(),name="post_create"),
    url(r'^post/(?P<pk>\d+)/update/$',views.PostUpdateView.as_view(),name="post_update"),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name="post_delete"),
    url(r'^drafts/$',views.DraftListView.as_view(),name="draft_list"),
    url(r'^post/(?P<pk>\d+)/publish/$',views.PostPublish,name="post_publish"),
    url(r'^post/(?P<pk>\d+)/comment/add/$',views.AddComment,name="add_comment"),
    url(r'^post/(?P<pk>\d+)/comment/approve/$',views.ApproveComment,name="approve_comment"),
    url(r'^post/(?P<pk>\d+)/comment/delete/$',views.DeleteComment,name="delete_comment"),
]
