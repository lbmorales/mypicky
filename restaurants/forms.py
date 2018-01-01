from django import forms

from .models import RestaurantLocation

class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category'
        ]

    # Example of validating an attribute of the model. Dummy code.

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) == 1:
            raise forms.ValidationError("Not a valid name")
        else:
            name.capitalize()
        return name

    