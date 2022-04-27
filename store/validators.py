from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if len(value) != 9:
        raise ValidationError('Phone number must containt 9 numbers')
    try:
        int(value)
    except:
        raise ValidationError('Phone number must containt only numbers')