from django.core.exceptions import ValidationError

CATEGORIES = ['Mexican', 'Indian', 'Mediteranean', 'American', 'Other']

def validate_category(value):
    cap_category = value.capitalize()
    if not value in CATEGORIES and not cap_category in CATEGORIES:
        raise ValidationError("{0} is not a valid category".format(value))
        #raise ValidationError(f"{value} not a valid category")     # python >= 3.6