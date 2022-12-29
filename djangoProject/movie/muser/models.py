from django.db import models

# Create your models here.
from django.db import models

# 유저
class MovieMuser(models.Model):
    use_in_migration = True
    muser_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    age = models.TextField()
    class Meta:
        db_table = "movie_musers"
    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password} {self.age}'








