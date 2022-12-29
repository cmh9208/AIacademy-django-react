from django.db import models

# Create your models here.
# 유저
class ShopSuser(models.Model):
    use_in_migration = True
    suer_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    point = models.TextField()
    class Meta:
        db_table = "shop_susers"
    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password} {self.point}'