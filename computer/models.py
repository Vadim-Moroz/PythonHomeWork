from django.db import models

class ComputerModel(models.Model):
    class Meta:
        db_table = 'computer'
    name = models.CharField(max_length=20)
    price = models.FloatField()
    status = models.BooleanField(default=False)
    color = models.CharField(max_length=20)