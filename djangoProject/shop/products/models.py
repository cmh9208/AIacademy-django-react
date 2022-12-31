from django.db import models

from shop.categories.models import ShopCategory


# Create your models here.
# 상품
class ShopProduct(models.Model):
    use_in_migration = True
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)

    shop_category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = "shop_products"
    def __str__(self):
        return f'{self.pk} {self.name} {self.price} {self.image_url}'