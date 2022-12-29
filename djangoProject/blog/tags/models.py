from django.db import models

from blog.buser.models import BlogBuser
from blog.posts.models import BlogPost


# Create your models here.
# 태그
class BlogTag(models.Model):
    use_in_migration = True
    tag_id = models.AutoField(primary_key=True)
    title = models.TextField()

    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog_tags"
    def __str__(self):
        return f'{self.pk} {self.title}'