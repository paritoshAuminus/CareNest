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