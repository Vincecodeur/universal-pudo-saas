# Universal PUDO SaaS - Roadmap

Version: 0.5.0

Status: Organisation Foundation Ready

Last Updated: 2026-07-23

---

# ROADMAP PHILOSOPHY

This roadmap is an execution roadmap.

Every phase must produce:

- deliverables
- validation
- documentation
- commit
- push

before the next phase begins.

The objective is to maintain synchronization between:

- source code
- tests
- ADRs
- documentation

at all times.

---

# PROJECT COMPLETION CRITERIA

Universal PUDO SaaS V1 is successful when an organisation can:

- authenticate
- manage users
- manage memberships
- manage carrier accounts
- search pickup points
- visualize pickup points
- export pickup point data
- administer the platform

while Universal PUDO Engine remains responsible for carrier intelligence and carrier integrations.

---

# PHASE 1

Documentation Foundation

Status:

Completed

Deliverables:

- README.md
- product-vision.md
- architecture.md
- roadmap.md
- project-memory.md
- project-status.md

---

# PHASE 2

Repository Foundation

Status:

Completed

Deliverables:

- Git repository
- GitHub repository
- Initial commit
- Branch strategy

---

# PHASE 3

Architecture Foundation

Status:

Completed

Deliverables:

- Architecture Definition
- Core/SaaS Separation
- Technology Stack Validation

---

# PHASE 4

ADR Foundation

Status:

Completed

Deliverables:

ADR-0001 Repository Structure Strategy

ADR-0002 Authentication Strategy

ADR-0003 Credential Storage Strategy

ADR-0004 Multi-Tenant Strategy

ADR-0005 Module Boundary Strategy

ADR-0006 Self-Hosted Compatibility Strategy

---

# PHASE 5

Domain Model Design

Status:

Completed

Deliverables:

docs/domain-model.md

---

# PHASE 6

Database Model Design

Status:

Completed

Deliverables:

docs/database-model.md

docs/persistence-decisions.md

---

# PHASE 7

Implementation Foundation

Status:

Completed

---

## Phase 7.1

Backend Foundation

Status:

Completed

Deliverables:

- FastAPI Application
- Health Endpoint
- Configuration Foundation
- Universal PUDO Engine Dependency

Validation:

1 passed

0 failed

---

## Phase 7.2

Database Configuration Foundation

Status:

Completed

Deliverables:

- SQLAlchemy Base
- BaseEntity
- Database Session
- Runtime Settings
- .env.example

Validation:

3 passed

0 failed

---

## Phase 7.3

Alembic Foundation

Status:

Completed

Deliverables:

- alembic.ini
- alembic/env.py
- Alembic Integration
- PostgreSQL Connectivity
- Dedicated SaaS Database

Validation:

✅ alembic init

✅ alembic current

✅ SQLAlchemy metadata integration

✅ PostgreSQL connectivity

✅ Dedicated SaaS database

---

# PHASE 8

Organisation Foundation

Status:

Next

Priority:

High

Objectives:

- Create Organisation ORM Model
- Create Organisation Repository Foundation
- Create Organisation Table
- Create Organisation Constraints
- Create Organisation Persistence Tests

Deliverables:

organisation.py

First Business Entity

First Business Table

Validation:

alembic revision --autogenerate

alembic upgrade head

Organisation persistence validation

---

# PHASE 9

Membership Foundation

Status:

Planned

Objectives:

- Membership Entity
- Organisation Memberships
- Role Assignment Foundation

---

# PHASE 10

Users Foundation

Status:

Planned

Objectives:

- User Entity
- User Profiles
- User Persistence

---

# PHASE 11

Authentication Foundation

Status:

Planned

Objectives:

- Password Hashing
- JWT
- Login
- Logout
- Session Management

---

# PHASE 12

Roles And Permissions

Status:

Planned

Objectives:

- RBAC
- Organisation Roles
- Permission Matrix

---

# PHASE 13

Carrier Account Management

Status:

Planned

Objectives:

- CarrierAccount Entity
- Credential Storage
- Validation Layer
- Encryption Strategy

---

# PHASE 14

Universal PUDO Engine Integration

Status:

Planned

Objectives:

- Core Adapter Layer
- Search Service Integration
- Multi-Carrier Execution

---

# PHASE 15

Search Platform

Status:

Planned

Objectives:

- Search Execution
- Search History
- Search Persistence

---

# PHASE 16

Map Experience

Status:

Planned

Technology:

- Leaflet
- OpenStreetMap

Objectives:

- Search Visualization
- Pickup Point Discovery

---

# PHASE 17

Export Platform

Status:

Planned

Objectives:

- CSV Export
- Excel Export
- JSON Export
- Export History

---

# PHASE 18

Administration Portal

Status:

Planned

Objectives:

- Platform Monitoring
- Organisation Management
- Support Tools

---

# PHASE 19

Public API Foundation

Status:

Planned

Future ADR:

ADR-0007 Public API Strategy

Objectives:

- API Authentication
- API Access Control
- API Search Access

---

# PHASE 20

Observability And Audit

Status:

Planned

Objectives:

- Audit Logs
- Monitoring
- Diagnostics

---

# PHASE 21

Security Hardening

Status:

Planned

Objectives:

- Credential Encryption
- MFA Preparation
- Security Review

---

# PHASE 22

Frontend Foundation

Status:

Planned

Technology:

- Next.js
- React
- TypeScript

Objectives:

- Authentication UI
- Organisation UI
- Search UI

---

# PHASE 23

Core Upgrade Strategy

Status:

Planned

Objectives:

- Core Versioning
- Upgrade Procedures
- Compatibility Management

---

# PHASE 24

Release Preparation

Status:

Planned

Objectives:

- Documentation Freeze
- QA Validation
- Release Checklist

---

# PHASE 25

Universal PUDO SaaS V1.0.0

Status:

Future

Release Criteria:

Organisation Management

✅

User Management

✅

Authentication

✅

Carrier Accounts

✅

Searches

✅

Maps

✅

Exports

✅

Administration

✅

---

# CURRENT STATE

Completed:

✅ Documentation Foundation

✅ Repository Foundation

✅ Architecture Foundation

✅ ADR Foundation

✅ Domain Model Design

✅ Database Model Design

✅ Persistence Decisions

✅ Backend Foundation

✅ Database Configuration Foundation

✅ Alembic Foundation

Current Focus:

Organisation Foundation

---

# CURRENT TECHNICAL BASELINE

Validated:

✅ FastAPI

✅ SQLAlchemy

✅ Alembic

✅ PostgreSQL 17

✅ Universal PUDO Engine

✅ BaseEntity

✅ Database Session

✅ Dedicated SaaS Database

✅ 3 Automated Tests

Current Databases:

universal_pudo

Purpose:

Universal PUDO Engine

---

universal_pudo_saas

Purpose:

Universal PUDO SaaS

---

# PHASE COMPLETION RULE

A phase is completed only when:

1. Development Finished

2. Auto-Critique Completed

3. Validation Completed

4. Documentation Updated

5. Commit Created

6. Push Completed

7. Next Phase Opened

---

# CHANGE HISTORY

2026-07-22

Roadmap V1 created.

---

2026-07-22

ADR Foundation added.

---

2026-07-22

Domain Model and Database Model phases added.

---

2026-07-22

Backend Foundation completed.

---

2026-07-22

Database Configuration Foundation completed.

---

2026-07-23

Alembic Foundation completed.

---

2026-07-23

Dedicated SaaS PostgreSQL database created.

---

2026-07-23

Roadmap aligned with real implementation progress.

---

2026-07-23

Organisation Foundation defined as next milestone.
