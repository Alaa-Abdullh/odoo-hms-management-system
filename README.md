# odoo-hms-management-system
# 🏥 Odoo HMS - Hospital Management System

This project is a simple **Hospital Management System (HMS)** built using **Odoo** as part of a training task. It demonstrates user access control, model design, form view customization, and report generation.

## 📌 Features

### User Groups and Access Rights

#### 👤 User Group:
- Can **create/read/update** their **own** patients' records.
- Can **read** departments and doctors.
- **Cannot view**:
  - Doctors menu.
  - Doctor fields in the patient form view.

#### 👨‍💼 Manager Group:
- Can **create/read/update/delete**:
  - All patients' records.
  - Departments.
  - Doctors.
- Can **view**:
  - Doctors menu.
  - Doctor fields in the patient form view.

---

### 📄 Report
- A **Patients Report** was created with a custom design that lists relevant patient data.

## 🧩 Technologies
- Odoo 16+ (or the version you used)
- XML (for views, security, and reports)

