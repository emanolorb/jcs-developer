from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    alcoholic_beverage = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name