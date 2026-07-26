# Universal PUDO SaaS - Project Memory

Version: 1.1.0

Status: Active

Last Updated: 2026-07-25

---

# PURPOSE

This document preserves the long-term memory of the project.

It contains:

- strategic decisions
- architectural direction
- validated assumptions
- completed milestones
- lessons learned
- current state
- next milestones

This document complements:

- source code
- ADRs
- roadmap
- project-status

Source of Truth Priority:

1. Source Code
2. Tests
3. Database Schema
4. Approved ADRs
5. Architecture Documents
6. Project Documentation

When conflicts exist, source code wins.

---

# PROJECT SUMMARY

Universal PUDO SaaS is a multi-tenant SaaS platform built on top of Universal PUDO Engine.

The SaaS owns:

- authentication
- organisations
- users
- memberships
- permissions
- carrier accounts
- exports
- administration

Universal PUDO Engine owns:

- carrier integrations
- provider implementations
- search orchestration
- normalization
- carrier intelligence

The SaaS consumes the Core.

The SaaS must never duplicate Core responsibilities.

---

# STRATEGIC ARCHITECTURAL DECISIONS

## D001

Hosting Strategy

Decision:

SaaS-first

Self-host-ready

ADR-0006

---

## D002

Repository Strategy

Decision:

Monorepo

ADR-0001

---

## D003

Authentication

Decision:

Email + Password

JWT

ADR-0002

---

## D004

Credential Ownership

Decision:

Credentials are managed by the SaaS.

The Core consumes credentials.

ADR-0003

---

## D005

Multi-Tenant Model

Decision:

Tenant = Organisation

ADR-0004

---

## D006

Module Boundaries

Decision:

Business Modules

ADR-0005

---

---

## D007

Carrier Catalog Ownership

Decision:

Universal PUDO Engine owns the carrier catalog.

Universal PUDO SaaS does not persist carrier definitions.

Universal PUDO SaaS references carriers through carrier_code.

Universal PUDO SaaS owns carrier accounts and carrier credentials.

Reason:

Avoid duplicating Core responsibilities inside the SaaS.

Status:

Validated during Phase 14.

---

# VALIDATED TECHNOLOGY STACK

Backend

✅ FastAPI

✅ Python 3.14

---

Database

✅ PostgreSQL 17

✅ SQLAlchemy

✅ Alembic

---

Authentication

✅ passlib 1.7.4

✅ bcrypt 4.3.0

✅ python-jose

✅ cryptography

---

Frontend

Planned

✅ Next.js

✅ React

✅ TypeScript

---

# DATABASE OWNERSHIP STRATEGY

Universal PUDO Engine

Database:

universal_pudo

---

Universal PUDO SaaS

Database:

universal_pudo_saas

---

Architectural Rule:

One database per product.

Core and SaaS remain independent.

---

# CURRENT DATABASE STATE

Tables:

✅ alembic_version

✅ organisations

✅ users

✅ memberships

✅ carrier_accounts

✅ carrier_credentials

---

Validated Foreign Keys

✅ memberships.organisation_id

→ organisations.id

✅ memberships.user_id

→ users.id

✅ carrier_accounts.organisation_id
→ organisations.id

✅ carrier_credentials.carrier_account_id
→ carrier_accounts.id

---

Authentication Columns

✅ password_hash

✅ is_active

✅ is_verified

✅ last_login_at

✅ is_platform_admin

---

# IMPLEMENTED FOUNDATIONS

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

✅ Persistence Test Foundation

✅ Access Model Foundation

✅ Tenant Access Foundation

✅ Role Persistence Foundation

✅ Carrier Account Model Foundation

✅ Carrier Account Database Foundation

✅ Carrier Account ORM Foundation

✅ Carrier Account SQLAlchemy Foundation

✅ Carrier Credential Foundation

✅ Carrier Account Persistence Test Foundation

✅ Carrier Account Service Foundation

✅ Carrier Credential Service Foundation

✅ Carrier Account API Foundation

✅ Carrier Credential API Foundation

✅ Engine Catalog Foundation

✅ Engine Catalog Models

✅ Engine Catalog Client

✅ Engine Catalog Service

---

# CURRENT DOMAIN MODEL

Organisation

✅ Implemented

✅ Persisted

✅ Persistence Validated

---

User

✅ Implemented

✅ Persisted

✅ Authentication Ready

✅ Persistence Validated

---

Membership

✅ Implemented

✅ Persisted

✅ Persistence Validated

---

CarrierAccount

✅ Implemented

✅ Persisted

✅ Persistence Validated

✅ Repository Implemented

---

CarrierCredential

✅ Implemented

✅ Persisted

✅ Persistence Validated

✅ Repository Implemented

---

Relationship Model

Organisation

▲

│

Membership

│

▼

User

✅ Implemented

✅ Validated

---

# IMPLEMENTED AUTHENTICATION FOUNDATION

Authentication Model

✅ password_hash

✅ is_active

✅ is_verified

✅ last_login_at

---

Password Hashing

✅ hash_password()

✅ verify_password()

---

JWT

✅ create_access_token()

✅ decode_access_token()

---

Authentication Service

✅ authenticate_user()

✅ create_user_token()

---

Authentication API

✅ POST /auth/login

✅ GET /auth/me

✅ JWT Authentication Flow

✅ JWT Decoding

✅ User Lookup Foundation

✅ Repository-Based Authentication

---

# IMPLEMENTED PERSISTENCE FOUNDATION

Organisation Persistence

✅ session.add()

✅ session.commit()

✅ session.refresh()

✅ session.get()

✅ session.delete()

---

User Persistence

✅ session.add()

✅ session.commit()

✅ session.refresh()

✅ session.get()

✅ session.delete()

---

Membership Persistence

✅ session.add()

✅ session.commit()

✅ session.refresh()

✅ session.get()

✅ session.delete()

---

Validated:

✅ PostgreSQL Writes

✅ PostgreSQL Reads

✅ Foreign Key Persistence

✅ CRUD Persistence Workflows

---

# CURRENT TEST STATUS

Validated Test Suites

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

✅ test_user_platform_admin.py

✅ test_carrier_account.py

✅ test_carrier_account_persistence.py

✅ test_carrier_credential.py

✅ test_carrier_credential_persistence.py

✅ test_carrier_account_repository.py

✅ test_carrier_credential_repository.py

✅ test_carrier_account_api.py

✅ test_carrier_credential_api.py

---

Current Result

113 passed

0 failed

---

# CURRENT CODE STATUS

Implemented

✅ FastAPI Startup

✅ Health Endpoint

✅ Settings

✅ PostgreSQL Configuration

✅ SQLAlchemy Base

✅ BaseEntity

✅ Session Factory

✅ Alembic

✅ Organisation Model

✅ User Model

✅ Membership Model

✅ Foreign Keys

✅ Authentication Model

✅ Password Hashing

✅ JWT Generation

✅ JWT Decoding

✅ Authentication Service

✅ Authentication API

✅ POST /auth/login

✅ GET /auth/me

✅ User Lookup Foundation

✅ users/repository.py

✅ Organisation Persistence Tests

✅ User Persistence Tests

✅ Membership Persistence Tests

✅ CarrierAccount Model

✅ CarrierCredential Model

✅ Carrier Account Migration

✅ Carrier Credential Migration

✅ Carrier Account Persistence Tests

✅ Carrier Credential Persistence Tests

✅ Carrier Account Repository

✅ Carrier Credential Repository

✅ Carrier Account Repository Tests

✅ Carrier Credential Repository Tests

✅ Engine Catalog Models

✅ Engine Catalog Client

✅ Engine Catalog Service

✅ InMemory Engine Catalog Client

✅ Engine Catalog Tests

---

Not Implemented

❌ Permission Enforcement

❌ Searches

❌ Exports

❌ Administration

❌ Frontend

❌ Public API

---

# LESSONS LEARNED

Lesson 001

Infrastructure first works.

---

Lesson 002

Alembic must be validated before business entities.

---

Lesson 003

Source code remains the source of truth.

---

Lesson 004

Separate databases early.

---

Lesson 005

Validate PostgreSQL before debugging application code.

---

Lesson 006

Documentation must be updated before Forward.

---

Lesson 007

Core and SaaS boundaries must remain explicit.

---

Lesson 008

Always audit autogenerated migrations.

---

Lesson 009

Relationship-first modeling works.

---

Lesson 010

Tests before documentation.

---

Lesson 011

Model tests and persistence tests are different.

---

Lesson 012

Passlib 1.7.4 is validated with bcrypt 4.3.0.

---

Lesson 013

Authentication APIs should be validated independently from persistence.

---

Lesson 014

Persistence tests provide significantly more confidence than model-only tests.

---

Lesson 015

SQLAlchemy Python-side defaults should not be asserted before persistence.

Default value validation belongs to persistence tests.

---

Lesson 016

When no SQLAlchemy relationship or cascade delete is defined, child records must be deleted before parent records in persistence tests.

Example:

CarrierCredential must be deleted before CarrierAccount.

---

Lesson 017

Engine carrier metadata must not be duplicated inside the SaaS.

Lesson 018

Engine integration should begin with DTOs and service abstractions before introducing runtime connectivity.

---

# CURRENT PROJECT WORKFLOW

1. Development

2. Validation

3. PostgreSQL Validation

4. Test Validation

5. Documentation Update

6. Audit Documentation

7. Commit

8. Push

9. Forward

---

# CURRENT PROJECT STATE

Completed

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

✅ Persistence Test Foundation

✅ Access Model Foundation

✅ Tenant Access Foundation

✅ Role Persistence Foundation

✅ Carrier Account SQLAlchemy Foundation

✅ Carrier Credential Foundation

✅ Carrier Account Persistence Test Foundation

✅ Carrier Account Repository Foundation

✅ Carrier Credential Repository Foundation

---

Current Focus

Universal PUDO Engine Integration Foundation

---

# NEXT MILESTONE

Universal PUDO Engine Integration Foundation

Objectives:

- Define Engine integration contract
- Discover carrier catalog from Universal PUDO Engine
- Preserve ADR-0007 ownership model
- Avoid local carrier catalog persistence
- Prepare carrier synchronization layer
- Define SaaS ↔ Engine communication strategy

---

# FUTURE MILESTONES

Carrier Account Service Foundation
↓
Carrier Credential Service Foundation
↓
Carrier Account API Foundation
↓
Carrier Credential API Foundation
↓
Universal PUDO Engine Integration
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

# CHANGE HISTORY

2026-07-23

Authentication Model Foundation completed.

19 automated tests passing.

---

2026-07-23

Password Hashing Foundation completed.

26 automated tests passing.

---

2026-07-23

JWT Foundation completed.

30 automated tests passing.

---

2026-07-25

Authentication Service Foundation completed.

35 automated tests passing.

---

2026-07-25

Authentication API Foundation completed.

42 automated tests passing.

---

2026-07-25

Persistence Test Foundation implemented.

Added:

- test_organisation_persistence.py
- test_user_persistence.py
- test_membership_persistence.py

Validated:

- PostgreSQL persistence
- CRUD persistence
- Foreign key persistence

52 automated tests passing.

Documentation synchronized.

---

2026-07-25

Role Persistence Foundation completed.

Implemented:

- users.is_platform_admin
- migration 2270054c9c72_add_platform_admin_to_users
- test_user_platform_admin.py

Validated:

- SAAS_ADMIN persistence
- OWNER role alignment
- VIEWER role alignment

Result:

54 passed

0 failed

---

2026-07-25

Carrier Account Persistence Foundation completed.

Implemented:

- carrier_accounts/models.py
- carrier_credentials/models.py
- migration 3fb1f82a4474_create_carrier_accounts_table
- migration 2bc5746479e6_create_carrier_credentials_table
- test_carrier_account.py
- test_carrier_account_persistence.py
- test_carrier_credential.py
- test_carrier_credential_persistence.py

Validated:

- CarrierAccount model
- CarrierCredential model
- PostgreSQL persistence
- Foreign key persistence
- carrier_code reference model
- child-before-parent deletion order in persistence tests

Result:

73 passed

0 failed

---

2026-07-25

Carrier Account Repository Foundation completed.

Implemented:

- carrier_accounts/repository.py
- test_carrier_account_repository.py

Validated:

- get_carrier_account()
- list_carrier_accounts_by_organisation()

Result:

75 passed

0 failed

---

2026-07-25

Carrier Credential Repository Foundation completed.

Implemented:

- carrier_credentials/repository.py
- test_carrier_credential_repository.py

Validated:

- get_carrier_credential()
- list_credentials_by_carrier_account()

Result:

77 passed

0 failed

---

2026-07-26

Engine Catalog Foundation completed.

Implemented:

- engine_catalog/models.py
- engine_catalog/client.py
- engine_catalog/service.py
- engine_catalog/**init**.py
- test_engine_catalog_models.py
- test_engine_catalog_client.py
- test_engine_catalog_service.py

Validated:

- Carrier DTO
- CarrierCapability DTO
- CarrierLifecycle DTO
- EngineCatalogClient
- InMemoryEngineCatalogClient
- EngineCatalogService

Result:
113 passed
0 failed
