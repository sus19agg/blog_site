from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.utils import timezone
from django.urls import reverse_lazy


class AboutView(TemplateView):
    template_name = "blog/about.html"

class PostListView(ListView):
    template_name = "blog/post_list_view.html"
    context_object_name = "PostList"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_time__lte=timezone.now()).order_by("-published_time")


class PostDetailView(DetailView):
    template_name = "blog/post_detail_view.html"
    context_object_name = "PostDetail"
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    template_name = "blog/post_form_view.html"
    model = Post
    login_url = "/login/"
    redirect_field_name = "blog/post_detail_view.html"
    form_class = PostForm



class PostUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "blog/post_form_view.html"
    model = Post
    login_url = "/login/"
    redirect_field_name = "blog/post_detail_view.html"
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "blog/post_delete_view.html"
    model = Post
    login_url = "/login/"
    redirect_field_name = "blog/post_list_view.html"
    success_url = reverse_lazy("post_list")


class DraftListView(LoginRequiredMixin,ListView):
    template_name = "blog/draft_list_view.html"
    model = Post
    context_object_name = "DraftList"
    login_url = "/login/"
    redirect_field_name = "blog/draft_list_view.html"

    def get_queryset(self):
        return Post.objects.filter(published_time__isnull=True).order_by("created_time")


####################################################
####################################################

@login_required
def PostPublish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect("post_detail",pk=pk)


@login_required
def AddComment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect("post_detail",pk=post.pk)
    else :
        form = CommentForm()
    return render(request,"blog/comment_form_view.html",{"form":form})


@login_required
def ApproveComment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve_comment()
    return redirect("post_detail",pk=comment.post.pk)


@login_required
def DeleteComment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    pk = comment.post.pk
    comment.delete()
    return redirect("post_detail",pk=pk)
