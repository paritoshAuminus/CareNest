from django.db import models
from hospital.models import Hospital, HospitalMembership

class Department(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DepartmentMembership(models.Model):
    hospital_membership = models.ForeignKey(HospitalMembership, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = models.UniqueConstraint(
            fields= ["department, hospital_membership"],
            name="department_belongs_to_same_hospital"
        )

