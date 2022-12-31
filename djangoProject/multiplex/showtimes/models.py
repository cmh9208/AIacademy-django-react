from django.db import models

from multiplex.cinemas.models import MultiplexCinema
from multiplex.movies.models import MultiplexMovie
from multiplex.theaters.models import MultiplexTheater


# Create your models here.
# 상영시간
class MultiplexShowtime(models.Model):
    use_in_migration = True
    showtime_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    multiplex_cinema = models.ForeignKey(MultiplexCinema, on_delete=models.CASCADE)
    multiplex_movies = models.ForeignKey(MultiplexMovie, on_delete=models.CASCADE)
    multiplex_theater = models.ForeignKey(MultiplexTheater, on_delete=models.CASCADE)

    class Meta:
        db_table = "multiplex_showtimes"
    def __str__(self):
        return f'{self.pk} {self.start_time} {self.end_time}'