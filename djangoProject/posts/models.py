from django.db import models

from users.models import User


class Post(models.Model):
    use_in_migration = True
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "posts"
    def __str__(self):
        return f'{self.pk} {self.title} {self.content} {self.create_at}' \
               f' {self.updated_at}'