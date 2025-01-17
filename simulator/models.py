from django.db import models

class Scenario(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    decision_1 = models.CharField(max_length=255)
    decision_2 = models.CharField(max_length=255)
    decision_1_outcome = models.TextField()
    decision_2_outcome = models.TextField()

    def __str__(self):
        return self.title
