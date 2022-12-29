from django.db import models

from movie.cinemas.models import MovieCinema


# Create your models here.
# 극장
class MovieTheater(models.Model):
    use_in_migration = True
    theater_id = models.AutoField(primary_key=True)
    title = models.TextField()
    seat = models.TextField()

    movie_cinema = models.ForeignKey(MovieCinema, on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_theaters"
    def __str__(self):
        return f'{self.pk} {self.title} {self.seat}'