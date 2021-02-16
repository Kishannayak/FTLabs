from django.db import models

# Creating a model called User. Which contains user details and user activity
class User(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)
    start_activity = models.CharField(max_length=100)
    end_activity = models.CharField(max_length=100)
    def __str__(self):
        return self.real_name
    