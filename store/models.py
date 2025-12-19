from django.db import models

class Attend(models.Model):
    id = models.AutoField(primary_key=True)
    photo1 = models.ImageField(upload_to='photos/')
    photo2 = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"Attend {self.id}"
