from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="song_images")
    bio = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="song_images")
    other_artists = models.ManyToManyField(Artist, related_name='featured_in', blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title

