from django.db import models


class Blog(models.Model):
    title       = models.CharField(max_length = 50)
    category    = models.CharField(max_length = 20)
    description = models.CharField(max_length = 250)
    blogtext    = models.TextField(max_length = 1500)
    url         = models.URLField(blank = True)
    date        = models.DateField()


    def __str__(self):
        return self.title
