from django import forms
from .models import PlantedTree


class PlantedTreeForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = PlantedTree
        fields = ['tree', 'age', 'latitude', 'longitude']

class MultiplePlantedTreeForm(forms.Form):
    trees = forms.CharField(
        widget=forms.Textarea,
        help_text="Enter one tree per line in the format: tree_id, age, latitude, longitude"
    )

    def clean_trees(self):
        data = self.cleaned_data['trees']
        trees = []
        for line in data.splitlines():
            tree_data = line.split(',')
            if len(tree_data) != 4:
                raise forms.ValidationError("Each line must contain tree_id, age, latitude, and longitude")
            try:
                tree_id = int(tree_data[0].strip())
                age = int(tree_data[1].strip())
                latitude = float(tree_data[2].strip())
                longitude = float(tree_data[3].strip())
            except ValueError:
                raise forms.ValidationError("Tree ID, age, latitude, and longitude must be valid numbers")
            trees.append((tree_id, age, latitude, longitude))
        return trees
