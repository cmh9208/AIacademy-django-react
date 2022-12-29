from django.db import models

from movie.showtimes.models import MovieShowtime
from movie.theaters.models import MovieTheater


# Create your models here.
# 예매한 좌석
class MovieTheaterTicket(models.Model):
    use_in_migration = True
    theater_ticket_id = models.AutoField(primary_key=True)
    x = models.IntegerField()
    y = models.IntegerField()

    movie_showtime = models.ForeignKey(MovieShowtime, on_delete=models.CASCADE)
    movie_theater = models.ForeignKey(MovieTheater, on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_theater_tickets"
    def __str__(self):
        return f'{self.pk} {self.x} {self.y}'