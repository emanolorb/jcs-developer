from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    takeout = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name