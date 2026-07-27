# Universal PUDO SaaS

Version: 1.7.0

Status: Universal PUDO Engine Integration In Progress

Last Updated: 2026-07-27

---

# OVERVIEW

Universal PUDO SaaS is a multi-tenant platform built on top of Universal PUDO Engine.

The objective of the platform is to allow organisations to:

- manage users
- manage organisations
- manage memberships
- manage roles
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
- search orchestration

Universal PUDO SaaS remains responsible for:

- authentication
- organisations
- users
- memberships
- permissions
- carrier accounts
- carrier credentials
- exports
- administration

The SaaS must never duplicate Core responsibilities.

Carrier catalog ownership:

Universal PUDO Engine owns the carrier catalog.

Universal PUDO SaaS does not persist carrier definitions.

Universal PUDO SaaS stores carrier_code as a logical reference to carriers exposed by the Engine.

---

# CURRENT STATUS

Current Phase:

Phase 15.6

Universal PUDO Engine Integration Closure

Status:

Planned

Completed Milestones:

✅ Phase 15.1 Engine Catalog Foundation

✅ Phase 15.2 Carrier Catalog Integration Service

✅ Phase 15.3 Engine Search Foundation

✅ Phase 15.4 Organisation Search Foundation

✅ Phase 15.5 Multi-Carrier Execution Foundation

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

✅ Organisation Foundation

✅ Users Foundation

✅ Membership Foundation

✅ Authentication Model Foundation

✅ Password Hashing Foundation

✅ JWT Foundation

✅ Authentication Service Foundation

✅ Authentication API Foundation

✅ Persistence Test Foundation Implementation

✅ Carrier Account Model Foundation

✅ Carrier Credential Foundation

✅ Carrier Account Persistence Foundation

✅ Carrier Account Repository Foundation

✅ Carrier Credential Repository Foundation

✅ Carrier Account Service Foundation

✅ Carrier Credential Service Foundation

✅ Carrier Account API Foundation

✅ Carrier Credential API Foundation

✅ Engine Catalog Foundation

✅ Carrier Catalog Integration Service

---

# IMPLEMENTED FOUNDATIONS

Backend

✅ MultiCarrierSearchService

✅ Multi-Carrier Execution Foundation

✅ Organisation Search Foundation

✅ Organisation Search Service

✅ Engine Search Models

✅ Engine Search Client

✅ Engine Search Service

✅ FastAPI

✅ Health Endpoint

✅ Configuration Layer

✅ Application Foundation

✅ Engine Catalog Models

✅ Engine Catalog Client

✅ Engine Catalog Service

✅ Carrier Catalog Service

✅ Carrier Catalog Integration Service

---

Persistence

✅ PostgreSQL 17

✅ SQLAlchemy

✅ Alembic

✅ BaseEntity

✅ UUID Strategy

✅ Timestamp Strategy

✅ Soft Delete Strategy

---

Identity Domain

✅ Organisation Foundation

✅ Users Foundation

✅ Membership Foundation

✅ Authentication Model Foundation

✅ Password Hashing Foundation

✅ JWT Foundation

✅ Authentication Service Foundation

✅ Authentication API Foundation

✅ User Lookup Foundation

✅ Carrier Account Foundation

✅ Carrier Credential Foundation

---

Databases

✅ universal_pudo

Universal PUDO Engine database

✅ universal_pudo_saas

Universal PUDO SaaS database

---

Testing

✅ test_multi_carrier_search_service.py

✅ test_organisation_search_service.py

✅ test_engine_search_models.py

✅ test_engine_search_client.py

✅ test_engine_search_service.py

✅ test_main.py

✅ test_settings.py

✅ test_entities.py

✅ test_organisation.py

✅ test_user.py

✅ test_membership.py

✅ test_passwords.py

✅ test_tokens.py

✅ test_auth_service.py

✅ test_auth_api.py

✅ test_organisation_persistence.py

✅ test_user_persistence.py

✅ test_membership_persistence.py

✅ test_carrier_account.py

✅ test_carrier_account_persistence.py

✅ test_carrier_credential.py

✅ test_carrier_credential_persistence.py

✅ test_carrier_account_service.py

✅ test_carrier_credential_service.py

✅ test_carrier_account_api.py

✅ test_carrier_credential_api.py

✅ test_engine_catalog_models.py

✅ test_engine_catalog_client.py

✅ test_engine_catalog_service.py

✅ test_carrier_catalog_service.py

✅ test_user_platform_admin.py

Result:

136 passed

0 failed

---

# CURRENT DATABASE MODEL

Implemented Tables:

✅ organisations

✅ users

✅ memberships

✅ carrier_accounts

✅ carrier_credentials

---

User Authentication Fields:

✅ password_hash

✅ is_active

✅ is_verified

✅ last_login_at

---

Validated Foreign Keys:

✅ memberships.organisation_id
→ organisations.id

✅ memberships.user_id
→ users.id

✅ carrier_accounts.organisation_id
→ organisations.id

✅ carrier_credentials.carrier_account_id
→ carrier_accounts.id

---

# CURRENT DOMAIN MODEL

Organisation
▲
│
Membership
│
▼
User

Organisation
│
▼
CarrierAccount
│
▼
CarrierCredential

CarrierCatalogService
│
├── list_available_carriers()
├── list_organisation_carriers()
└── list_activatable_carriers_for_organisation()

carrier_code
│
▼
Universal PUDO Engine Carrier Catalog

EngineSearchService
│
├── search_pickup_points()
├── search_pickup_points_by_radius()
├── get_pickup_point()
└── list_carrier_pickup_points()

▼

Universal PUDO Engine Search API

Status:

✅ Implemented

✅ Persisted

✅ Validated

✅ Persistence Tested

---

# CURRENT PROJECT STRUCTURE

UNIVERSAL-PUDO-SAAS/

├── backend/

│ ├── alembic/

│ ├── alembic.ini

│ ├── .env.example

│ ├── pyproject.toml

│ ├── README.md

│ ├── src/

│ │ └── universal_pudo_saas/

│ │ ├── carrier_accounts/
│ │ ├── carrier_credentials/

│ │ ├── engine_catalog/
│ │ │ ├── **init**.py
│ │ │ ├── client.py
│ │ │ ├── models.py
│ │ │ └── service.py
│ │ ├── engine_search/
│ │ │ ├── **init**.py
│ │ │ ├── models.py
│ │ │ ├── client.py
│ │ │ └── service.py

│ │ ├── carrier_catalog/
│ │ │ ├── **init**.py
│ │ │ └── service.py

│ │ ├── organisation_search/
│ │ │ ├── **init**.py
│ │ │ └── service.py

│ │ ├── multi_carrier_search/
│ │ │ ├── **init**.py
│ │ │ └── service.py

│ │ ├── auth/

│ │ ├── core/

│ │ ├── database/

│ │ ├── shared/

│ │ ├── organisations/

│ │ ├── users/

│ │ ├── memberships/

│ │ ├── security/

│ │ └── main.py

│ └── tests/

│ ├── test_main.py

│ ├── test_settings.py
│ ├── test_engine_search_models.py
│ ├── test_engine_search_client.py
│ └── test_engine_search_service.py
│ ├── test_entities.py

│ ├── test_organisation.py

│ ├── test_user.py

│ ├── test_membership.py

│ ├── test_passwords.py

│ ├── test_tokens.py

│ ├── test_auth_service.py

│ └── test_auth_api.py

| ├── test_organisation_persistence.py

| ├── test_user_persistence.py

│ ├── test_carrier_account.py
│ ├── test_carrier_account_persistence.py
│ ├── test_carrier_credential.py
│ ├── test_carrier_credential_persistence.py
│ ├── test_carrier_account_repository.py
│ ├── test_carrier_credential_repository.py
│ └── test_membership_persistence.py
│ ├── test_engine_catalog_models.py
│ ├── test_engine_catalog_client.py
│ ├── test_engine_catalog_service.py
│ └── test_carrier_catalog_service.py

└── docs/

---

# VALIDATED TECHNOLOGY STACK

Frontend

- Next.js
- React
- TypeScript

Status:

Planned

---

Backend

- FastAPI
- Python 3.14

Status:

Validated

---

Database

- PostgreSQL 17
- SQLAlchemy
- Alembic

Status:

Validated

---

Authentication

- passlib
- bcrypt
- python-jose
- cryptography

Status:

Validated

---

Maps

- Leaflet
- OpenStreetMap

Status:

Planned

---

# AUTHENTICATION STATUS

Completed:

✅ Authentication Model Foundation

✅ password_hash

✅ is_active

✅ is_verified

✅ last_login_at

✅ Alembic Migration

✅ PostgreSQL Validation

✅ Automated Tests

---

✅ Password Hashing Foundation

✅ hash_password()

✅ verify_password()

---

✅ JWT Foundation

✅ create_access_token()

✅ decode_access_token()

---

✅ Authentication Service Foundation

✅ authenticate_user()

✅ create_user_token()

---

✅ Authentication API Foundation

✅ POST /auth/login

✅ GET /auth/me

✅ JWT Authentication Flow

✅ User Lookup Foundation

✅ Repository-Based Authentication

---

# PERSISTENCE STATUS

Implemented:

✅ test_organisation_persistence.py

✅ test_user_persistence.py

✅ test_membership_persistence.py

✅ test_carrier_account_persistence.py

✅ test_carrier_credential_persistence.py

✅ test_carrier_account_repository.py

✅ test_carrier_credential_repository.py

✅ test_carrier_account_repository.py

✅ test_carrier_account_service.py

✅ test_carrier_account_api.py

✅ test_carrier_credential_repository.py

✅ test_carrier_credential_service.py

✅ test_carrier_credential_api.py

✅ test_engine_catalog_models.py

✅ test_engine_catalog_client.py

✅ test_engine_catalog_service.py

✅ test_carrier_catalog_service.py

✅ test_user_platform_admin.py

Validated:

✅ session.add()

✅ session.commit()

✅ session.refresh()

✅ session.get()

✅ session.delete()

✅ PostgreSQL Reads

✅ PostgreSQL Writes

✅ CRUD Persistence Validation

✅ Foreign Key Persistence Validation

Status:

Implementation Complete

Repository Layer Complete

Documentation Synchronization Complete

---

Not Yet Implemented:

❌ Refresh Tokens

❌ Password Reset

❌ Email Verification

⚠ Advanced Role Permissions

---

# IMPLEMENTATION STRATEGY

Infrastructure

↓

Persistence

↓

Domain Models

↓

Authentication

✅ Completed

↓

Persistence Validation

✅ Implemented

↓

Roles & Permissions 

Planned

↓

Carrier Account Management

✅ Foundation Completed

↓

Business Features

↓

Frontend

---

# NEXT MILESTONE

Phase 15.6

Universal PUDO Engine Integration Closure

Objectives:

- End-to-end validation
- Architecture validation
- Documentation validation
- Repository synchronization
- Phase 15 closure

---

# FUTURE ROADMAP

Universal PUDO Engine Integration Closure
↓
Search Platform
↓
Map Experience
↓
Export Platform
↓
Administration Portal
↓
Public API
↓
Frontend
↓
Universal PUDO SaaS v1.0.0

---

# DEPLOYMENT STRATEGY

Official Decision:

SaaS-first

Self-host-ready

Current Scope:

Multi-tenant SaaS

Future Possibility:

Enterprise self-hosted deployments

ADR:

ADR-0006

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
- domain-model.md
- database-model.md
- persistence-decisions.md

---

# CURRENT QUALITY STATUS

Database:

✅ Validated

PostgreSQL:

✅ Validated

Migrations:

✅ Validated

Tests:

✅ 136 passed

Documentation:

✅ Synchronized

Git:

✅ Committed

GitHub:

✅ Pushed

---

# LICENSE

To Be Defined.
