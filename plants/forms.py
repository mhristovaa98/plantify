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
            'watering_interval',
            'location',
            'light_requirement'
        ]
        widgets = {
            'scientific_name': forms.TextInput(attrs={'placeholder': 'Enter scientific name, e.g., Helianthus annuus'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'watering_interval': forms.NumberInput(attrs={'placeholder': 'The interval must be between 1 and 90 days'}),
            'difficulty': forms.Select(),
            'price': forms.NumberInput(),
            'location': forms.Select(),
            'light_requirement': forms.Select(),

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
            'difficulty':'Difficulty to cares',
            'location': 'Room',
            'light_requirement': 'Light',
        }

class PlantCreateForm(PlantForm):
    ...

class PlantEditForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['scientific_name'].disabled = True
