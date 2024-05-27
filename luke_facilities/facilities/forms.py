from django import forms
from .models import Facility

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['facility_code', 'facility_name', 'district_id', 'owner_id']

class FacilitySearchForm(forms.Form):
    facility_name = forms.CharField(max_length=255, required=False)
    district_id = forms.IntegerField(required=False)
