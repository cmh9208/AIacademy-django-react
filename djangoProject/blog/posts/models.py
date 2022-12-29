from datetime import datetime

from django.db import models

from blog.buser.models import BlogBuser


# Create your models here.



class BlogPost(models.Model):
    use_in_migration = True
    post_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    blog_user = models.ForeignKey(BlogBuser, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog_posts"
    def __str__(self):
        return f'{self.pk} {self.title} {self.content} {self.create_at}' \
               f' {self.updated_at}'