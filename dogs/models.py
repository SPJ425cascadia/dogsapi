from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.ForeignKey(   
        'Breed', 
            related_name='breed', 
            on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    favoritefood = models.CharField(max_length=200)
    favoritetoy = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Breed(models.Model):
    Tiny = 't'
    Small = 's'
    Medium = 'm'
    Large = 'l'
    Size_Choices = (
        (Tiny, 'Tiny'),
        (Small, 'Small'),
        (Medium, 'Medium'),
        (Large, 'Large'),
    ) 
    name = models.CharField(max_length=200)
    size = models.CharField(
        max_length=6,
        choices=Size_Choices,
        default=Small,)
    friendliness = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    sheddingamount = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    exerciseneeds = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.name