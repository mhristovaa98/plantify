import datetime

from django import forms

from cares.models import CareLog


class CareLogBaseForm(forms.ModelForm):
    class Meta:
        model = CareLog
        fields = '__all__'
        labels = {
            'plant': 'Plant:',
            'care_type': 'Care Type:',
            'performed_minutes': 'Time spent (minutes):',
            'notes': 'Notes:',
            'date_performed': 'Date:',

        }
        widgets = {
            'care_type': forms.Select(),
            'performed_minutes': forms.NumberInput(attrs={'placeholder': 'Enter Minutes between 1 and 60 minutes.',}),
            'notes': forms.Textarea(attrs={'rows': 5, 'cols': 30, 'placeholder': 'Enter Notes....',}),
            'date_performed': forms.DateInput()
        }
        error_messages = {
            'care_type': {
                'required': 'Choose at least one care type! ',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_performed'].initial = datetime.date.today()

    def clean_date_performed(self):
        data = self.cleaned_data['date_performed']
        if data > datetime.date.today():
            raise forms.ValidationError('Date cannot be in the future!')
        return data


class CareLogAddForm(CareLogBaseForm):
    ...

class CareLogUpdateForm(CareLogBaseForm):
    ...