from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey("auth.User",on_delete="DO_NOTHING")
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    published_time = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approve_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={"pk":self.pk})



class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete="DO_NOTHING")
    author = models.CharField(max_length=50)
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=timezone.now)

    def approve_comment(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("post_list")
