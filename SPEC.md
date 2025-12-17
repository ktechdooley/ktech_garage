# kTech GMS – Codex Specification

## Purpose
This document defines **non-negotiable rules** for building features.
ChatGPT Codex must follow this exactly.

---

## Canonical IDs (LOCKED)
- customers.id
- vehicles.id
- vehicles.customer_id
- jobs.vehicle_id
- invoices.vehicle_id
- ecu_jobs.vehicle_id

Never invent alternative names.

---

## UI Architecture (LOCKED)
- Top bar contains:
  - Logo
  - Business name
  - Services
  - Address / phone / email
- Sidebar is navigation only
- UI style: dark graphite background, off-white text, neon green hover

Files:
- app/templates/_layout.html
- app/templates/_topbar.html
- app/static/css/theme.css

---

## Module Build Order
Codex should implement modules **one at a time**:

1. Customers
2. Vehicles (with mileage history)
3. Jobs
4. Invoices (money in / money out)
5. ECU Programming & Calibration
6. Reporting

Do not build multiple modules at once.

---

## Deletion Rules
- Never hard-delete financial records
- Use:
  - status = 'archived'
  - deleted_at timestamps if needed
- Admin override may permanently delete

---

## Definition of Done (per feature)
- CRUD works
- Uses locked naming
- UI matches theme
- No inline CSS
- No breaking existing routes
