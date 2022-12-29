
from django.db import models

from blog.buser.models import BlogBuser
from blog.posts.models import BlogPost


# Create your models here.
# 댓글
class BlogComment(models.Model):
    use_in_migration = True
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.TextField(null=True)

    blog_user = models.ForeignKey(BlogBuser, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)


    class Meta:
        db_table = "blog_comments"
    def __str__(self):
        return f'{self.pk} {self.content} {self.created_at} {self.updated_at} {self.parent_id}'