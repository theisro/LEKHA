from django.forms import ModelForm
from archival.models import Work, MediaFile

class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ['name', 'year', 'medium', 'description', 'authors', 'classification', 'location', 'link', 'record_creator', 'cd1_name', 'cd1_value', 'cd2_name', 'cd2_value', 'cd3_name', 'cd3_value', 'cd4_name', 'cd4_value', 'cd5_name', 'cd5_value', 'cd6_name', 'cd6_value', 'cd7_name', 'cd7_value']