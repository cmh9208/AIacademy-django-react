from django.db import models

from shop.products.models import ShopProduct
from shop.suser.models import ShopSuser


# Create your models here.
# 장바구니
class ShopCart(models.Model):
    use_in_migration = True
    cart_id = models.AutoField(primary_key=True)

    shop_product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
    shop_user = models.ForeignKey(ShopSuser, on_delete=models.CASCADE)

    class Meta:
        db_table = "shop_carts"
    def __str__(self):
        return f'{self.pk}'