from django.db import models

from shop.suser.models import ShopSuser


# Create your models here.
# 배송지
class ShopDelivery(models.Model):
    use_in_migration = True
    delivery_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    shop_user = models.ForeignKey(ShopSuser, on_delete=models.CASCADE)

    class Meta:
        db_table = "shop_deliveries"
    def __str__(self):
        return f'{self.pk} {self.username} {self.address} {self.detail_address}' \
               f' {self.phone}'