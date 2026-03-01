from django.contrib import admin
from .models import Hospital, HospitalMembership

# Register your models here.
admin.site.register(Hospital)
admin.site.register(HospitalMembership)

