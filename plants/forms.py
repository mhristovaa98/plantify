from django import forms

from plants.models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = [
            'scientific_name',
            'image_url',
            'difficulty',
            'description',
            'price',
            'watering_interval'
        ]
        widgets = {
            'scientific_name': forms.TextInput(),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'watering_interval': forms.NumberInput(),
            'difficulty': forms.Select(),
            'price': forms.NumberInput(),

        }
        help_texts = {
            'scientific_name':'Enter scientific name, e.g., Helianthus annuus',
            'watering_interval':'The interval must be between 1 and 90 days',
        }
        error_messages = {
            'scientific_name': {
                'invalid': 'Please enter a valid scientific name.',
            },
            'watering_interval': {
                'max_value': 'Watering interval cannot exceed 90 days.',
                'min_value': 'Watering interval must be at least 1 day.'
            }
        }
        labels = {
            'watering_interval':'Watering interval (days).',
        }

class PlantCreateForm(PlantForm):
    ...

class PlantEditForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['scientific_name'].disabled = True


class PlantDeleteForm(PlantForm):
    ...