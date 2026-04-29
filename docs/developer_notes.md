# Hospital Management System Overview

## Purpose
Web-based hospital management system for:
- Patient registration
- Appointments
- OPD/IPD management
- Billing
- Pharmacy
- Lab reports
- Staff management

## Main Modules
1. Authentication / Roles
2. Patient Management
3. Doctor Management
4. Appointments
5. Admissions (IPD)
6. Billing
7. Pharmacy
8. Laboratory
9. Reports

## User Roles
- Admin
- Receptionist
- Doctor
- Nurse
- Pharmacist (later)
- Lab Technician (later)

## Core Workflow
Patient registers
→ Appointment booked
→ Doctor consultation
→ Prescription/Lab tests
→ Billing
→ Pharmacy / Admission if required

## Tech Stack
Backend: Django
Database: PostgreSQL
Frontend: React JS
Task queue: Celery (if used) 
Testing: Factory boy (search other options as well)   

# Developer Notes

## Conventions

Use UUIDs for external identifiers.

Soft delete instead of hard delete for patients.

All models should include:
- created_at
- updated_at

---

## Ideas

Maybe appointments should generate Visit objects.

Maybe patient reports should be immutable after doctor signs.

---

## Things to revisit

Should doctors belong to multiple departments?

Need better permission hierarchy later.

---

## Django Notes

Use custom user model from start.
Do not use default auth user.

---

## Pitfalls

Do not couple patient data directly to auth model too tightly.

Avoid premature microservices thinking.

---

## TODO Ideas

- Audit logs
- Celery for notifications
- Slot generation algorithm
