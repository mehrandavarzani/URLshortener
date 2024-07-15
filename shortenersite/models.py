from django.db import models

class Url(models.Model):
    shortid=models.SlugField(max_length=6,primary_key=True)
    orginalurl=models.URLField(max_length=200)

    def __str__(self):
        return self.orginalurl
