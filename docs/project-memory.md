# Universal PUDO SaaS - Project Memory

Version: 1.1.0

Status: Active

Last Updated: 2026-07-27

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
- carrier accounts
- carrier credentials
- organisation search orchestration
- multi-carrier search orchestration
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

## D008

Universal PUDO Engine Integration Strategy

Decision:

Phase 15 was kept open until Universal PUDO Engine integration closure was completed.

Status:

Completed

✅ Phase 15.1 Engine Catalog Foundation
✅ Phase 15.2 Carrier Catalog Integration Service
✅ Phase 15.3 Engine Search Foundation
✅ Phase 15.4 Organisation Search Foundation
✅ Phase 15.5 Multi-Carrier Execution Foundation
✅ Phase 15.6 Universal PUDO Engine Integration Closure

Reason:

The primary SaaS use case is allowing an organisation to locate pickup points using only its activated carriers.

The SaaS owns orchestration.

Universal PUDO Engine owns carrier integrations.

---

D009

Search Platform Strategy

Decision:

Search Platform is implemented in six phases:

16.1 Search Domain Design
16.2 Search Platform Models Foundation
16.3 Search Platform Service Foundation
16.4 Search Result Enrichment Foundation
16.5 Search Platform Validation
16.6 Search Platform Closure

Reason:

Prevent roadmap drift and enforce Planning Freeze.

---

## D010

Phase 16 Persistence Boundary

Decision:

Phase 16 Search Platform is non-persistent.

Search Platform may introduce:

- SearchRequest
- SearchResult
- SearchPlatformService

Phase 16 must not introduce:

- SearchResult table
- SearchHistory table
- Alembic migration
- Search persistence

Reason:

Search Platform domain boundaries must be stabilised before persistence decisions.

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

✅ Multi-Carrier Execution Foundation

✅ MultiCarrierSearchService

✅ Organisation Search Foundation

✅ Organisation Search Service

✅ Engine Search Foundation

✅ Engine Search Models

✅ Engine Search Client

✅ Engine Search Service

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

✅ Carrier Catalog Integration Service

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

✅ test_engine_catalog_models.py

✅ test_engine_catalog_client.py

✅ test_engine_catalog_service.py

✅ test_engine_search_models.py

✅ test_engine_search_client.py

✅ test_engine_search_service.py

✅ test_carrier_catalog_service.py

✅ test_organisation_search_service.py

✅ test_multi_carrier_search_service.py

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

136 passed

0 failed

---

# CURRENT CODE STATUS

Implemented

✅ MultiCarrierSearchService

✅ multi_carrier_search/service.py

✅ test_multi_carrier_search_service.py

✅ Organisation Search Service

✅ organisation_search/service.py

✅ Engine Search Models

✅ Engine Search Client

✅ Engine Search Service

✅ InMemory Engine Search Client

✅ Engine Search Tests

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

✅ Carrier Catalog Service

✅ Carrier Catalog Integration Tests

---

Not Implemented

❌ Permission Enforcement

❌ Search Platform

❌ Search Result Enrichment

❌ Search Persistence

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

Lesson 019

The SaaS can expose organisation-specific carrier catalogue views without persisting Engine carrier definitions.

Lesson 020

Carrier catalogue integration must use Carrier.code and CarrierAccount.carrier_code as the mapping boundary.

Lesson 021

The SaaS should consume Engine search capabilities through a dedicated client and service layer instead of recreating Engine search use cases.

Lesson 022

Engine Search Foundation must remain read-only and must not introduce search persistence, SaaS-side search orchestration, or Engine modifications.

Lesson 023

Before starting any new phase, all sub-phases, objectives, deliverables, validation criteria and exit criteria must be frozen.

No phase implementation may start until phase planning is completed.

This rule exists to prevent roadmap zig-zagging and architectural redefinition during implementation.

---

# CURRENT PROJECT WORKFLOW

0. Phase Planning Freeze

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

✅ Phase 15.6 Universal PUDO Engine Integration Closure

✅ Multi-Carrier Execution Foundation

✅ Engine Search Foundation

✅ Organisation Search Foundation

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

Phase 16.1

Search Domain Design

---

# NEXT MILESTONE

Phase 16.1

Search Domain Design

Objectives:

- Define Search Platform scope
- Define SearchRequest concept
- Define SearchResult concept
- Define Search Platform boundaries
- Confirm persistence boundaries
- Prepare Phase 16.2

---

# FUTURE MILESTONES

Phase 16 Search Platform
↓
Phase 17 Map Experience
↓
Phase 18 Export Platform
↓
Phase 19 Administration Portal
↓
Phase 20 Public API Foundation
↓
Phase 21 Observability And Audit
↓
Phase 22 Security Hardening
↓
Phase 23 Frontend Foundation
↓
Phase 24 Core Upgrade Strategy
↓
Phase 25 Release Preparation
↓
Phase 26 Universal PUDO SaaS v1.0.0

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

---

2026-07-26

Carrier Catalog Integration Service completed.

Implemented:

- carrier_catalog/**init**.py
- carrier_catalog/service.py
- test_carrier_catalog_service.py

Validated:

- Available carrier listing
- Organisation carrier listing
- Activatable carrier listing
- Carrier.code to CarrierAccount.carrier_code mapping

Result:
118 passed
0 failed

---

2026-07-27

Engine Search Foundation completed.

Implemented:

- engine_search/**init**.py
- engine_search/models.py
- engine_search/client.py
- engine_search/service.py
- test_engine_search_models.py
- test_engine_search_client.py
- test_engine_search_service.py

Validated:

- PickupPoint SaaS projection
- EngineSearchClient
- InMemoryEngineSearchClient
- EngineSearchService
- pickup point search methods

Result:
130 passed
0 failed

---

2026-07-27

Phase 15 roadmap frozen.

Validated structure:

✅ Phase 15.1 Engine Catalog Foundation
✅ Phase 15.2 Carrier Catalog Integration Service
✅ Phase 15.3 Engine Search Foundation
✅ Phase 15.4 Organisation Search Foundation
✅ Phase 15.5 Multi-Carrier Execution Foundation
⏳ Phase 15.6 Universal PUDO Engine Integration Closure

Reason:

Engine integration boundaries were formalized before Search Platform implementation.

- Adapter Layer
- Search Integration
- Multi-Carrier Execution

After completing Engine Search Foundation, remaining objectives were still outstanding.

Roadmap updated to explicitly represent remaining Universal PUDO Engine integration work before Phase 16 Search Platform.

---

2026-07-27

Organisation Search Foundation completed.

Implemented:

- organisation_search/service.py
- test_organisation_search_service.py

Validated:

- organisation-based pickup point search
- organisation carrier filtering
- aggregation of organisation carrier results

Result:

133 passed
0 failed

---

2026-07-27

Multi-Carrier Execution Foundation completed.

Implemented:

- multi_carrier_search/service.py
- test_multi_carrier_search_service.py

Validated:

- MultiCarrierSearchService
- OrganisationSearchService integration
- Dedicated SaaS search boundary

Result:

136 passed
0 failed

---

2026-07-27

Universal PUDO Engine Integration Closure completed.

Validated:

- Engine Catalog Foundation
- Carrier Catalog Integration
- Engine Search Foundation
- Organisation Search Foundation
- Multi-Carrier Search Foundation

Result:

136 passed
0 failed

Phase 15 closed.

Phase 16.1 Search Domain Design becomes current focus.
