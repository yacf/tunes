from django.db import models

class Videos(models.Model):
    videoid = models.CharField(max_length=25)

    def __str__(self):
        return self.videoid