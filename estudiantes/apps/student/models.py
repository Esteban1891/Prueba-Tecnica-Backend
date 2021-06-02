from django.db import models
from apps.student.validators import valid_max_min_number #here validate extension

class Student(models.Model):
    SEXO_OPTIONS = [
        ('Male', '"Male",'),
        ('Female', 'Female'),
    ]

    id = models.UUIDField(primary_key=True)
    complete_name = models.CharField(max_length = 150, blank=False, null=False)
    document = models.CharField(max_length=50, unique=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50,choices=SEXO_OPTIONS,blank=False, null=False)
    note = models.IntegerField(default=0,validators=[valid_max_min_number])
    autoevaluation = models.IntegerField(default=0, validators=[valid_max_min_number])


    def __str__(self):
        return f'{self.complete_name}'