# Architecture Notes

## System Architecture Overview

Project follows multi-tenant SaaS architecture.

Hierarchy:

Platform
└── Hospitals
    └── Departments
        └── Users
            ├── Doctors
            ├── Receptionists
            ├── Patients

---

## Core Domain Models

Entities:

- Hospital
- Department
- User
- Role
- DoctorProfile
- PatientProfile
- Appointment
- MedicalRecord
- Prescription
- Schedule

Relationships:

- Hospital has many Departments
- Hospital has many Users
- Doctor belongs to one or many Departments
- Patient has many Appointments
- Appointment produces Medical Record
- Medical Record may contain Prescriptions

---

## Multi-Tenancy Strategy

Tenant isolation model:
(Decide later)

Possible approaches:
- Shared database + tenant_id
- Separate schemas
- Separate databases

Current choice:
(shared DB + tenant_id) [initially]

---

## Permission Model

Role-based access control:

COMS:
full access

Doctor:
clinical access

Receptionist:
appointment operations

Patient:
self-service access

---

## Major Modules

- Authentication
- Appointments
- Scheduling
- Clinical Records
- Billing
- Notifications

---

## Planned App Structure (Django Apps)

accounts/
hospitals/
departments/
appointments/
medical_records/
billing/
notifications/

---

## Design Decisions

Why custom user model?
Why multi-tenant architecture?
Why role permissions instead of separate user tables?

Record decisions here.

---

## Future Architecture Questions

Open problems:

- Multi-branch hospitals?
- Audit logging design?
- Scheduling engine?
- Queue system?