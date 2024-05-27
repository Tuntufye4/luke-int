from django.db import models

class Facility(models.Model):
    facility_code = models.CharField(max_length=50, unique=True)
    facility_name = models.CharField(max_length=255)
    district_id = models.PositiveIntegerField()
    owner_id = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    archived_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.facility_name
