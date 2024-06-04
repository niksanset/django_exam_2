from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    cast = models.TextField(blank=True) 
    genres = models.TextField(blank=True)  
    href = models.CharField(max_length=255, blank=True, null=True)  
    extract = models.TextField(blank=True, null=True)  
    thumbnail = models.URLField(blank=True, null=True)  
    thumbnail_width = models.IntegerField(default=0)  
    thumbnail_height = models.IntegerField(default=0)  

    def __str__(self):
        return self.title
    
    
    
class TVShow(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    genres = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    runtime = models.IntegerField(null=True,blank=True,default=None)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1,null=True,blank=True)
    premiered = models.DateField(null=True,blank=True,default=None)
    ended = models.DateField(null=True,blank=True,default=None)
    official_site = models.URLField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    imdb_id = models.CharField(max_length=20,null=True)
    image_medium = models.URLField(blank=True, null=True)
    image_original = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name