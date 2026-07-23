# Universal PUDO SaaS

Version: 0.5.0

Status: Active Development

---

# OVERVIEW

Universal PUDO SaaS is a multi-tenant platform built on top of Universal PUDO Engine.

The objective of the platform is to allow organisations to:

- manage users
- manage organisations
- manage memberships
- connect carrier accounts
- search pickup points
- visualize pickup points
- export pickup point data
- administer platform usage

without implementing carrier-specific integrations.

---

# RELATIONSHIP WITH UNIVERSAL PUDO ENGINE

Universal PUDO SaaS depends on:

Universal PUDO Engine

Repository:

https://github.com/Vincecodeur/universal-pudo-engine

Universal PUDO Engine remains responsible for:

- carrier integrations
- provider implementations
- pickup point normalization
- carrier abstraction
- carrier synchronization
- carrier intelligence

Universal PUDO SaaS remains responsible for:

- authentication
- users
- organisations
- permissions
- carrier credentials
- exports
- administration

The SaaS must never duplicate Core responsibilities.

---

# CURRENT STATUS

Current Phase:

Phase 8

Organisation Foundation

Current State:

✅ Documentation Foundation

✅ Repository Foundation

✅ ADR Foundation

✅ Domain Model Design

✅ Database Model Design

✅ Persistence Decisions

✅ Backend Foundation

✅ Database Configuration Foundation

✅ Alembic Foundation

---

# IMPLEMENTED FOUNDATIONS

Backend

✅ FastAPI

✅ Health Endpoint

✅ Configuration Layer

✅ Application Foundation

---

Persistence

✅ PostgreSQL

✅ SQLAlchemy

✅ Alembic

✅ BaseEntity

✅ UUID Strategy

✅ Timestamp Strategy

✅ Soft Delete Strategy

---

Databases

✅ universal_pudo

Universal PUDO Engine database

✅ universal_pudo_saas

Universal PUDO SaaS database

---

Testing

✅ test_main.py

✅ test_entities.py

✅ test_settings.py

Result:

3 passed

0 failed

---

# NOT IMPLEMENTED YET

Authentication

Users

Organisations

Memberships

Carrier Accounts

Searches

Exports

Administration

Frontend

Public API

---

# TARGET TECHNOLOGY STACK

Frontend

- Next.js
- React
- TypeScript

Backend

- FastAPI
- Python 3.14

Database

- PostgreSQL 17
- SQLAlchemy
- Alembic

Maps

- Leaflet
- OpenStreetMap

---

# PROJECT STRUCTURE

UNIVERSAL-PUDO-SAAS/

├── backend/

│ ├── alembic/

│ ├── src/

│ │ └── universal_pudo_saas/

│ └── tests/

│

└── docs/

---

# IMPLEMENTATION STRATEGY

Infrastructure

↓

Persistence

↓

Business Entities

↓

Authentication

↓

Business Features

↓

Frontend

---

# NEXT MILESTONE

Organisation Foundation

Objectives:

- First ORM Model
- First Business Table
- First Alembic Migration
- Persistence Validation

---

# DEPLOYMENT STRATEGY

Official Decision:

SaaS-first

Self-host-ready

Current Scope:

Multi-tenant SaaS

Future Possibility:

Enterprise self-hosted deployments.

---

# DOCUMENTATION

Project documentation is located in:

docs/

Main Documents:

- project-memory.md
- product-vision.md
- architecture.md
- roadmap.md
- project-status.md

---

# LICENSE

To Be Defined.
