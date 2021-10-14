from django.db import models

# Create your models here.

class MetaModel(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        return str([field.name+': '+str(getattr(self, field.name))  for field in self._meta.fields])


class rssFeeds(MetaModel):
    letter = models.CharField(max_length=8, blank=False)
    guid = models.CharField(max_length=50, unique=True)
    link = models.URLField(max_length=200)
    pubDate = models.CharField(max_length=50)
    title = models.TextField(blank=False)
    description = models.TextField()