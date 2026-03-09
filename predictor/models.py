from django.db import models

class PredictionHistory(models.Model):

    disease = models.CharField(max_length=50)

    result = models.CharField(max_length=50)

    probability = models.FloatField()

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disease