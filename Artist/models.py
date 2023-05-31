from django.db import models

class Prompt(models.Model):
    id = models.AutoField(primary_key=True)
    positive = models.CharField(max_length=500)
    negative = models.CharField(max_length=500)

