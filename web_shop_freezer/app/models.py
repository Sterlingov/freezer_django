from django.db import models


class MainModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    char_freeze = models.IntegerField()
    char_ozu = models.IntegerField()
    char_weight = models.IntegerField()
    price = models.IntegerField()
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.title
