from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# 유저
class BlogBuser(models.Model):
    use_in_migration = True
    buser_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    class Meta:
        db_table = "blog_busers"
    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password}'