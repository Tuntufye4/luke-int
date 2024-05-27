from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Facility
from .forms import FacilityForm, FacilitySearchForm
from django.utils import timezone

def check_registry(facility_code):
    # Placeholder function to simulate registry check
    # Replace with actual registry API call
    existing_facilities = ["LL000001", "LL000002"]  # Example facility codes
    return facility_code in existing_facilities

def facility_list(request):
    form = FacilitySearchForm(request.GET)
    facilities = Facility.objects.filter(is_active=True)
    if form.is_valid():
        if form.cleaned_data['facility_name']:
            facilities = facilities.filter(facility_name__icontains=form.cleaned_data['facility_name'])
        if form.cleaned_data['district_id']:
            facilities = facilities.filter(district_id=form.cleaned_data['district_id'])
    return render(request, 'facilities/facility_list.html', {'facilities': facilities, 'form': form})

def facility_create(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            facility_code = form.cleaned_data['facility_code']
            if check_registry(facility_code):
                return render(request, 'facilities/facility_form.html', {
                    'form': form,
                    'error': 'Facility already exists in the master registry.'
                })
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'facilities/facility_form.html', {'form': form})

def facility_archive(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    facility.is_active = False
    facility.archived_at = timezone.now()
    facility.save()
    return redirect('facility_list')
