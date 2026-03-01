from django.db import models
from django.db.models import Q
from accounts.models import User

# Create your models here.
class Hospital(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=700)

    def __str__(self):
        return self.title

class HospitalMembership(models.Model):
    roles = [
        ('CHIEF', 'Chief of medical staff'),
        ('DOCTOR', 'Doctor'),
        ('RECEPTIONIST', 'Receptionist'),
        ('PATIENT', 'Patient'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    role = models.CharField(max_length=12, choices=roles)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.role})'
    
    class Meta:
        unique_together = ('user', 'hospital')
        constraints = [
            models.UniqueConstraint(
                fields=['hospital'],
                condition=Q(role='CHIEF'),
                name='only_one_chief_per_hospital'
            )
        ]

