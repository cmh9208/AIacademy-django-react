from django.db import models

from multiplex.showtimes.models import MultiplexShowtime
from multiplex.theaters.models import MultiplexTheater


# Create your models here.
# 예매한 좌석
class MultiplexTheaterTicket(models.Model):
    use_in_migration = True
    theater_ticket_id = models.AutoField(primary_key=True)
    x = models.IntegerField()
    y = models.IntegerField()

    multiplex_showtime = models.ForeignKey(MultiplexShowtime, on_delete=models.CASCADE)
    multiplex_theater = models.ForeignKey(MultiplexTheater, on_delete=models.CASCADE)

    class Meta:
        db_table = "multiplex_theater_tickets"
    def __str__(self):
        return f'{self.pk} {self.x} {self.y}'