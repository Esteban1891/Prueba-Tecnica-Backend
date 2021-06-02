from django.core.exceptions import ValidationError
 
def valid_max_min_number(value):
    if value < 0:
        raise ValidationError("solo se permite de 0 a 5")
    if value > 5:
        raise ValidationError("solo se permite de 0 a 5")
