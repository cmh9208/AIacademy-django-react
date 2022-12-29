

from django.db import models

from blog.buser.models import BlogBuser
from blog.posts.models import BlogPost


# Create your models here.
# 조회수
class BlogView(models.Model):
    use_in_migration = True
    view_id = models.AutoField(primary_key=True)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    blog_user = models.ForeignKey(BlogBuser, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog_views"
    def __str__(self):
        return f'{self.pk} {self.title} {self.created_at}'