from django.db import models

class Scenario(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    decision_1 = models.CharField(max_length=255)
    decision_2 = models.CharField(max_length=255)
    outcomes = models.JSONField(default=list)  # Store outcomes as a list of dictionaries

    def __str__(self):
        return f"Scenario: {self.title} - {self.decision_1} vs {self.decision_2}"
