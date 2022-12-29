from django.db import models

from movie.cinemas.models import MovieCinema
from movie.movies.models import Movie
from movie.theaters.models import MovieTheater


# Create your models here.
# 상영시간
class MovieShowtime(models.Model):
    use_in_migration = True
    showtime_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)

    movie_cinema = models.ForeignKey(MovieCinema, on_delete=models.CASCADE)
    movie_movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_theater = models.ForeignKey(MovieTheater, on_delete=models.CASCADE)

    class Meta:
        db_table = "movie_showtimes"
    def __str__(self):
        return f'{self.pk} {self.start_time} {self.end_time}'