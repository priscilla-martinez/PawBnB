from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator 

class Home(models.Model):
    title = models.CharField(max_length=100)
    home_url = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=100, null=False, default="city")
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    max_guests = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])

    def __str__(self): 
        return f"'{self.title}' owned by {self.owner}, allows up to {self.max_guests} guests."