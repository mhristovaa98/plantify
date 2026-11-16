from django import forms

from plant_collections.models import Collection

from plants.models import Plant


class CollectionFormBase(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'background_image','description', 'plants']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name:'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description:',
                'cols':10
            }),
            'background_image': forms.URLInput(attrs={'placeholder': 'Enter URL here:'}),
            'plants': forms.CheckboxSelectMultiple(),
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        plants = Plant.objects.all()

        for plant in plants:
            if plant.scientific_name.lower() in name.lower():
                raise forms.ValidationError(
                    "Please enter a unique name for the collection."
                )
        return name

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('plants'):
            raise forms.ValidationError(
                "Please enter a plant."
            )
        return cleaned_data

class CollectionAddForm(CollectionFormBase):
    ...

class CollectionAddPlantsForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['plants']
