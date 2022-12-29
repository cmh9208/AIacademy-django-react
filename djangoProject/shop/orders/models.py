from datetime import datetime

from django.db import models

from shop.deliveries.models import ShopDelivery
from shop.products.models import ShopProduct
from shop.suser.models import ShopSuser


# Create your models here.
# 주문목록
class ShopOrder(models.Model):
    use_in_migration = True
    order_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    shop_user = models.ForeignKey(ShopSuser, on_delete=models.CASCADE)
    shop_product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
    shop_deliveries = models.ForeignKey(ShopDelivery, on_delete=models.CASCADE)

    class Meta:
        db_table = "shop_orders"
    def __str__(self):
        return f'{self.pk} {self.created_at}'