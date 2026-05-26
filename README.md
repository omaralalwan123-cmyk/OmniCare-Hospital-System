# 🏥 OmniCare: Multi-Tenant Smart Hospital Management Platform

OmniCare is a robust, enterprise-grade Multi-Tenant Hospital Management System (HMS) built to empower modern healthcare facilities. Designed with a highly scalable architecture, it features dynamic tenant isolation to serve multiple medical institutions securely on a single platform while managing complex clinical and administrative workflows.

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | Django & Django REST Framework | Robust RESTful APIs and complex medical business logic |
| **Database** | PostgreSQL | Advanced relational data storage with optimized indexing |
| **Multi-Tenancy** | Schema-based Isolation | Dynamic and secure data isolation per medical facility |
| **Authentication** | JWT (JSON Web Tokens) | Secure, stateless authentication across tenants |
| **Task Queue** | Celery & Redis | Asynchronous background tasks and scheduled medical reports |
| **Containerization** | Docker & Docker Compose | Seamless and reproducible environment orchestration |

---

## 🚀 Key Enterprise Features

*   **Dynamic Multi-Tenancy:** Secure data isolation ensuring that each hospital's clinical records, staff, and billing are strictly separated.
*   **Electronic Health Records (EHR):** Smart tracking of patient history, medical diagnoses, prescriptions, and lab results.
*   **Appointment & Scheduling System:** Intelligent queuing and scheduling for doctors, clinics, and emergency departments.
*   **Staff & Faculty Management:** Granular Role-Based Access Control (RBAC) for Doctors, Nurses, Receptionists, and Super Admins.
*   **Smart Analytics & Billing:** Automated invoice generation and administrative dashboards tracking hospital performance.

---

## 📁 Multi-Tenancy Architecture Overview

OmniCare utilizes **PostgreSQL Schemas** (or Shared Database with Tenant Filtering) to provide clean data separation. 
*   **Shared Infrastructure:** One core codebase runs the entire platform, reducing maintenance and hosting costs.
*   **Tenant Isolation:** Data routing is dynamically handled at the database level based on the sub-domain or request headers, ensuring maximum security and GDPR/HIPAA compliance principles.

---

## ⚙️ Getting Started (Locally)

### Prerequisites
Ensure you have **Docker** and **Docker Compose** installed.

### Installation

1. **Clone the repository:**
```bash
   git clone [https://github.com/omaralalwan123-cmyk/OmniCare-HMS.git](https://github.com/omaralalwan123-cmyk/OmniCare-HMS.git)
   cd OmniCare-HMS
