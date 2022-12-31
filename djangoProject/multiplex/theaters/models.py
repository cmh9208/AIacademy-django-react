from django.db import models

from multiplex.cinemas.models import MultiplexCinema


# Create your models here.
# 극장
class MultiplexTheater(models.Model):
    use_in_migration = True
    theater_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    seat = models.CharField(max_length=20)

    multiplex_cinema = models.ForeignKey(MultiplexCinema, on_delete=models.CASCADE)

    class Meta:
        db_table = "multiplex_theaters"
    def __str__(self):
        return f'{self.pk} {self.title} {self.seat}'