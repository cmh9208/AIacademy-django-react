from django.db import models

# Create your models here.
# 영화
class Movie(models.Model):
    use_in_migration = True
    movie_id = models.AutoField(primary_key=True)
    title = models.TextField()
    director = models.TextField()
    description = models.TextField()
    poster_url = models.TextField()
    running_time = models.IntegerField()
    age_rating = models.IntegerField()
    class Meta:
        db_table = "movies"
    def __str__(self):
        return f'{self.pk} {self.title} {self.director} {self.description}' \
               f' {self.poster_url} {self.running_time} {self.age_rating}'

