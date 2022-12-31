from django.db import models

# Create your models here.
# 카테고리
class ShopCategory(models.Model):
    use_in_migration = True
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


    class Meta:
        db_table = "shop_categories"
    def __str__(self):
        return f'{self.pk} {self.name}'

