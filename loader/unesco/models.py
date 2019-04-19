from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

...

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    ....

    def __str__(self) :
        return self.name