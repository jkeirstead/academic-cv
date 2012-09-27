from django.db import models

# Create your models here.

class Address(models.Model):
    first_line = models.CharField(max_length=100)
    second_line = models.CharField(max_length=100)
    third_line = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_line + ', ' + self.city



