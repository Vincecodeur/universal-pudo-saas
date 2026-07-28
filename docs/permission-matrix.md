# Universal PUDO SaaS - Permission Matrix

Version: 1.0.0

Status: Approved

Last Updated: 2026-07-25

---

# PURPOSE

This document defines the permissions associated with each user type.

The objective is to ensure a clear separation between:

- SaaS platform administration
- organisation administration
- operational platform usage

---

# USER TYPES

The platform currently supports:

- SaaS Administrator
- Owner
- Viewer

---

# PLATFORM ADMINISTRATION

| Permission               | SaaS Admin | Owner | Viewer |
| ------------------------ | ---------- | ----- | ------ |
| Create Organisation      | ✅         | ❌    | ❌     |
| Suspend Organisation     | ✅         | ❌    | ❌     |
| Reactivate Organisation  | ✅         | ❌    | ❌     |
| Manage Subscription      | ✅         | ❌    | ❌     |
| Manage Billing           | ✅         | ❌    | ❌     |
| Manage Platform Quotas   | ✅         | ❌    | ❌     |
| Access Global Statistics | ✅         | ❌    | ❌     |
| Access All Tenants       | ✅         | ❌    | ❌     |

---

# CARRIER PUBLICATION MANAGEMENT

| Permission                           | SaaS Admin | Owner | Viewer |
| ------------------------------------ | ---------- | ----- | ------ |
| Publish Engine Carrier               | ✅         | ❌    | ❌     |
| Unpublish Engine Carrier             | ✅         | ❌    | ❌     |
| Enable Carrier Integration Globally  | ✅         | ❌    | ❌     |
| Disable Carrier Integration Globally | ✅         | ❌    | ❌     |
| Make Integration Available To Owners | ✅         | ❌    | ❌     |
| View Carrier Catalog                 | ✅         | ✅    | ✅     |

---

# ORGANISATION USER MANAGEMENT

| Permission         | SaaS Admin | Owner | Viewer |
| ------------------ | ---------- | ----- | ------ |
| Create Viewer      | ❌         | ✅    | ❌     |
| Disable Viewer     | ❌         | ✅    | ❌     |
| Enable Viewer      | ❌         | ✅    | ❌     |
| Remove Viewer      | ❌         | ✅    | ❌     |
| View User List     | ❌         | ✅    | ✅     |
| Manage Permissions | ❌         | ✅    | ❌     |

---

# CARRIER ACCOUNT MANAGEMENT

| Permission                       | SaaS Admin | Owner | Viewer |
| -------------------------------- | ---------- | ----- | ------ |
| Connect Carrier Account          | ❌         | ✅    | ❌     |
| Configure Carrier Credentials    | ❌         | ✅    | ❌     |
| Update Carrier Credentials       | ❌         | ✅    | ❌     |
| Test Carrier Connectivity        | ❌         | ✅    | ❌     |
| Enable Carrier Account           | ❌         | ✅    | ❌     |
| Disable Carrier Account          | ❌         | ✅    | ❌     |
| View Configured Carrier Accounts | ❌         | ✅    | ✅     |

---

# DASHBOARD MANAGEMENT

| Permission         | SaaS Admin | Owner | Viewer |
| ------------------ | ---------- | ----- | ------ |
| Create Dashboard   | ❌         | ✅    | ❌     |
| Modify Dashboard   | ❌         | ✅    | ❌     |
| Delete Dashboard   | ❌         | ✅    | ❌     |
| Select KPI Widgets | ❌         | ✅    | ❌     |
| Configure Charts   | ❌         | ✅    | ❌     |
| View Dashboard     | ✅         | ✅    | ✅     |

---

# PUDO OPERATIONS

| Permission            | SaaS Admin | Owner | Viewer |
| --------------------- | ---------- | ----- | ------ |
| Search Pickup Points  | ✅         | ✅    | ✅     |
| Filter Search Results | ✅         | ✅    | ✅     |
| View Search Results   | ✅         | ✅    | ✅     |
| View Carrier Coverage | ✅         | ✅    | ✅     |

---

# EXPORTS

| Permission                     | SaaS Admin | Owner | Viewer |
| ------------------------------ | ---------- | ----- | ------ |
| Export Search Results          | ✅         | ✅    | ✅     |
| Export Coverage Data           | ✅         | ✅    | ❌     |
| Export Organisation Statistics | ❌         | ✅    | ❌     |
| Export Platform Statistics     | ✅         | ❌    | ❌     |

---

# ANALYTICS

| Permission                    | SaaS Admin | Owner | Viewer |
| ----------------------------- | ---------- | ----- | ------ |
| View Platform Analytics       | ✅         | ❌    | ❌     |
| View Organisation Analytics   | ❌         | ✅    | ✅     |
| View Usage Statistics         | ❌         | ✅    | ✅     |
| Configure Analytics Dashboard | ❌         | ✅    | ❌     |

---

# ARCHITECTURAL RULES

Carrier integration ownership:

SaaS Administrator controls:

- carrier publication
- carrier visibility
- carrier availability

Carrier catalog ownership remains inside Universal PUDO Engine.

- platform availability

Owner owns:

- organisation carrier accounts
- carrier credentials

Viewer owns:

- no configuration

---

Dashboard ownership:

Owner owns:

- dashboard configuration
- KPI selection
- dashboard layout

Viewer consumes:

- dashboards
- charts
- statistics

---

# FUTURE ROLES

Not part of V1:

- Organisation Admin
- API User
- Service Account
- Auditor

These roles may be introduced in future releases if validated by customer demand.

---

# SUCCESS CRITERIA

The access model is considered implemented when:

✅ SaaS Administrator permissions enforced

✅ Owner permissions enforced

✅ Viewer permissions enforced

✅ Automated permission tests passing

✅ Permission matrix aligned with access-model.md

✅ Documentation synchronized
