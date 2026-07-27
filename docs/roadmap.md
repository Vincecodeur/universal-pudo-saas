# Universal PUDO SaaS - Roadmap

Version: 1.7.0

Status: Universal PUDO Engine Integration In Progress

Last Updated: 2026-07-27

---

# ROADMAP PHILOSOPHY

This roadmap is an execution roadmap.

Every phase must produce:

- deliverables
- validation
- PostgreSQL validation
- documentation
- commit
- push

before the next phase begins.

The goal is to keep synchronization between:

- source code
- database
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
- manage roles
- manage carrier accounts
- search pickup points
- visualize pickup points
- export pickup point data
- administer the platform

while Universal PUDO Engine remains fully responsible for carrier intelligence.

---

# PHASE 1

Documentation Foundation

Status:

Completed

---

# PHASE 2

Repository Foundation

Status:

Completed

---

# PHASE 3

Architecture Foundation

Status:

Completed

---

# PHASE 4

ADR Foundation

Status:

Completed

Approved ADRs:

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

Validation:

1 passed

0 failed

---

## Phase 7.2

Database Configuration Foundation

Status:

Completed

Validation:

3 passed

0 failed

---

## Phase 7.3

Alembic Foundation

Status:

Completed

Validation:

✅ Alembic

✅ PostgreSQL

✅ Metadata Integration

✅ Dedicated SaaS Database

---

# PHASE 8

Organisation Foundation

Status:

Completed

Validation:

✅ ORM Model

✅ Migration

✅ PostgreSQL

✅ Tests

---

# PHASE 9

Users Foundation

Status:

Completed

Validation:

✅ ORM Model

✅ Migration

✅ PostgreSQL

✅ Tests

---

# PHASE 10

Membership Foundation

Status:

Completed

Validation:

✅ ORM Model

✅ Foreign Keys

✅ PostgreSQL

✅ Tests

---

# PHASE 11

Authentication Foundation

Status:

Completed

Objective:

Secure platform identities.

---

## Phase 11.1

Authentication Model Foundation

Status:

Completed

Validation:

✅ Migration generated

✅ Migration audited

✅ Migration applied

✅ PostgreSQL validated

✅ Tests passing

---

## Phase 11.2

Password Hashing Foundation

Status:

Completed

Deliverables:

security/passwords.py

Functions:

- hash_password()
- verify_password()

Validation:

✅ Password hashing

✅ Password verification

✅ Dedicated tests

✅ bcrypt compatibility validated

Result:

26 passed

0 failed

---

## Phase 11.3

JWT Foundation

Status:

Completed

Deliverables:

security/tokens.py

Functions:

- create_access_token()
- decode_access_token()

Validation:

✅ JWT generation

✅ JWT validation

✅ JWT decoding

Result:

30 passed

0 failed

---

## Phase 11.4

Authentication Service Foundation

Status:

Completed

Deliverables:

auth/service.py

Functions:

- authenticate_user()
- create_user_token()

Validation:

✅ Password verification integration

✅ JWT integration

✅ Service tests

Result:

35 passed

0 failed

---

## Phase 11.5

Authentication API Foundation

Status:

Completed

Deliverables:

auth/routes.py

auth/schemas.py

users/repository.py

Endpoints:

✅ POST /auth/login

✅ GET /auth/me

Validation:

✅ API tests

✅ Authentication workflow tests

✅ End-to-end authentication flow

✅ JWT Authentication Flow

✅ User Lookup Foundation

Result:

42 passed

0 failed

---

## Authentication Success Criteria

✅ Password Hashing

✅ JWT

✅ Authentication Service

✅ Login Endpoint

✅ Current User Endpoint

✅ Dedicated Tests

✅ Documentation Updated

---

# PHASE 12

Persistence Test Foundation

Status:

Completed

Objectives:

- SQLAlchemy Session Tests
- PostgreSQL Persistence Tests
- CRUD Validation
- Relationship Validation
- Migration Validation

Deliverables:

tests/test_organisation_persistence.py

tests/test_user_persistence.py

tests/test_membership_persistence.py

Validation:

✅ session.add()

✅ session.commit()

✅ session.refresh()

✅ session.delete()

✅ PostgreSQL persistence verified

✅ Relationship persistence verified

✅ CRUD workflow verified

---

# PHASE 13

Tenant Access Foundation

Status:

Completed

Objectives:

- Tenant Access Model
- Role Strategy
- Role Definitions
- Permission Matrix

## Phase 13.1

Access Model Foundation

Status:

Completed

Deliverables:

✅ product-vision.md

✅ PUDO-focused product scope

✅ access-model.md

✅ permission-matrix.md

✅ carrier-integration-model.md

✅ role-strategy.md

✅ domain-model.md

✅ database-model.md

✅ architecture.md

## Phase 13.2

Role Persistence Foundation

Status:

Completed

Deliverables:

✅ users.is_platform_admin

✅ memberships.role alignment

✅ migration 2270054c9c72

✅ test_user_platform_admin.py

Validated:

✅ PostgreSQL migration applied

✅ Platform role persistence

✅ Membership role alignment

✅ OWNER role

✅ VIEWER role

Validation:

54 passed

0 failed

---

# PHASE 14

Carrier Account Management

Status:

Completed

---

## Phase 14.1

Carrier Account Model Foundation

Status:

Completed

Validated:

✅ Organisation ownership

✅ Carrier Account ownership

✅ Carrier Credential ownership

✅ Universal PUDO Engine owns Carrier Catalog

✅ SaaS references carriers through carrier_code

---

## Phase 14.2

Carrier Account Database Model

Status:

Completed

Validated:

✅ carrier_accounts

✅ carrier_credentials

✅ no carrier_integrations table

✅ carrier_code reference strategy

---

## Phase 14.3

Carrier Account ORM Model

Status:

Completed

Validated:

✅ CarrierAccount

✅ CarrierCredential

✅ no CarrierIntegration SaaS entity

---

## Phase 14.4

Carrier Account Lifecycle

Status:

Completed

---

## Phase 14.5

Carrier Account Architecture

Status:

Completed

---

## Phase 14.6

Carrier Account Implementation Plan

Status:

Completed

---

## Phase 14.7

Documentation Realignment Foundation

Status:

Completed

Result:

✅ Option B validated

✅ Universal PUDO Engine owns carrier catalog

✅ Universal PUDO SaaS does not persist carrier definitions

---

## Phase 14.8

Carrier Account SQLAlchemy Foundation

Status:

Completed

Deliverables:

✅ carrier_accounts/models.py

✅ migration 3fb1f82a4474_create_carrier_accounts_table

✅ test_carrier_account.py

✅ test_carrier_account_persistence.py

Validation:

✅ PostgreSQL migration applied

✅ Persistence tests passing

---

## Phase 14.9

Carrier Credential Foundation

Status:

Completed

Deliverables:

✅ carrier_credentials/models.py

✅ migration 2bc5746479e6_create_carrier_credentials_table

✅ test_carrier_credential.py

✅ test_carrier_credential_persistence.py

Validation:

✅ PostgreSQL migration applied

✅ Persistence tests passing

---

## Phase 14.10

Carrier Account Persistence Test Foundation

Status:

Completed

Result:

73 passed

0 failed

---

## Phase 14.11

Carrier Account Repository Foundation

Status:

Completed

Deliverables:

✅ carrier_accounts/repository.py

✅ test_carrier_account_repository.py

Validated:

✅ get_carrier_account()

✅ list_carrier_accounts_by_organisation()

Result:

75 passed

0 failed

---

## Phase 14.12

Carrier Credential Repository Foundation

Status:

Completed

Deliverables:

✅ carrier_credentials/repository.py

✅ test_carrier_credential_repository.py

Validated:

✅ get_carrier_credential()

✅ list_credentials_by_carrier_account()

Result:

77 passed

0 failed

---

## Phase 14.13

Carrier Account Service Foundation

Status:

Completed

Objectives:

- Create Carrier Account service layer
- Define business validation rules
- Prepare API consumption

Validated:

✅ create_carrier_account()
✅ get_carrier_account_service()
✅ list_carrier_accounts_for_organisation()

Result:

85 passed
0 failed

---

## Phase 14.14

Carrier Credential Service Foundation

Status:

Completed

Objectives:

- Create Carrier Credential service layer
- Define credential validation rules
- Prepare API consumption

Validated:

✅ get_carrier_credential_service()
✅ list_credentials_for_carrier_account()

Result:

85 passed
0 failed

---

## Phase 14.15

Carrier Account API Foundation

Status:

Completed

Objectives:

- Create Carrier Account endpoints
- Create request schemas
- Create response schemas
- Add API tests

Validated:

✅ GET /carrier-accounts/
✅ GET /carrier-accounts/organisation/

Result:

93 passed
0 failed

---

## Phase 14.16

Carrier Credential API Foundation

Status:

Completed

Objectives:

- Create Carrier Credential endpoints
- Create request schemas
- Create response schemas
- Add API tests

Validated:

✅ GET /carrier-credentials/
✅ GET /carrier-credentials/carrier-account/

Result:

93 passed
0 failed

---

## Phase 14.17

End-to-End Validation

Status:

Completed

Objectives:

- Repository validation
- Service validation
- API validation
- PostgreSQL validation

---

## Phase 14.18

Documentation Closure

Status:

Completed

Objectives:

- Synchronize documentation
- Synchronize roadmap
- Synchronize project-status
- Synchronize project-memory

---

# PHASE 15

Universal PUDO Engine Integration

Status:

In Progress

Objectives:

- Adapter Layer
- Search Integration
- Multi-Carrier Execution

---

## Phase 15.1

Engine Catalog Foundation

Status:

Completed

Deliverables:

✅ engine_catalog/models.py
✅ engine_catalog/client.py
✅ engine_catalog/service.py

Validated:

✅ Carrier
✅ CarrierCapability
✅ CarrierLifecycle
✅ EngineCatalogClient
✅ InMemoryEngineCatalogClient
✅ EngineCatalogService

Result:

113 passed
0 failed

---

## Phase 15.2

Carrier Catalog Integration Service

Status:

Completed

Objectives:

- Cross Engine carriers with CarrierAccount
- Preserve carrier_code mapping
- No Engine modifications
- No catalog persistence
- Prepare organisation carrier activation workflows

Deliverables:

✅ carrier_catalog/**init**.py
✅ carrier_catalog/service.py
✅ test_carrier_catalog_service.py

Validated:

✅ list_available_carriers()
✅ list_organisation_carriers()
✅ list_activatable_carriers_for_organisation()
✅ Carrier.code to CarrierAccount.carrier_code mapping
✅ No catalog persistence
✅ No Engine modifications
✅ No database migration

Result:

118 passed
0 failed

---

## Phase 15.3

Engine Search Foundation

Status:

Completed

Objectives:

- Consume Universal PUDO Engine pickup point search capabilities
- Create SaaS-side search DTOs
- Create EngineSearchClient contract
- Create InMemoryEngineSearchClient for tests
- Create EngineSearchService
- Avoid search persistence
- Avoid SaaS-side search orchestration
- Avoid Engine modification

Deliverables:

✅ engine_search/**init**.py
✅ engine_search/models.py
✅ engine_search/client.py
✅ engine_search/service.py
✅ test_engine_search_models.py
✅ test_engine_search_client.py
✅ test_engine_search_service.py

Validated:

✅ PickupPoint SaaS read model
✅ Address SaaS projection
✅ GeoLocation SaaS projection
✅ PickupType SaaS enum
✅ EngineSearchClient
✅ InMemoryEngineSearchClient
✅ EngineSearchService
✅ search_pickup_points()
✅ search_pickup_points_by_radius()
✅ get_pickup_point()
✅ list_carrier_pickup_points()

Result:

130 passed
0 failed

---

## Phase 15.4

Organisation Search Foundation

Status:

Completed

Objectives:

- Connect organisation carrier accounts with Engine Search
- Search only through activated organisation carriers
- Use CarrierAccount.carrier_code as the organisation carrier boundary
- Use EngineSearchService as the Engine search entry point
- Avoid search persistence
- Prepare Multi-Carrier Execution

Deliverables:

- organisation_search/
- OrganisationSearchService
- dedicated tests

---

## Phase 15.5

Multi-Carrier Execution Foundation

Status:

Planned

Objectives:

- Create a dedicated SaaS orchestration layer for multi-carrier search execution
- Provide a single entry point for future Search Platform features
- Delegate organisation-based carrier filtering to OrganisationSearchService
- Preserve SaaS ownership of multi-carrier orchestration
- Preserve Universal PUDO Engine ownership of carrier integrations
- Prepare Phase 16 Search Platform

Responsibilities:

✅ Expose a MultiCarrierSearchService

✅ Use OrganisationSearchService as the organisation search execution dependency

✅ Return pickup point results through a dedicated multi-carrier service boundary

✅ Prepare future execution strategies without implementing them yet

Out of Scope:

❌ FastAPI routes

❌ Frontend

❌ Map rendering

❌ Export

❌ Search persistence

❌ Cache

❌ Ranking

❌ Distance calculation

❌ Advanced deduplication

❌ Provider timeout handling

❌ Parallel execution

Deliverables:

- multi_carrier_search/
- MultiCarrierSearchService
- test_multi_carrier_search_service.py

Validation:

✅ MultiCarrierSearchService created

✅ MultiCarrierSearchService uses OrganisationSearchService

✅ PickupPoint results are returned

✅ No Engine modification

✅ No SQLAlchemy model

✅ No Alembic migration

✅ Dedicated tests passing

Exit Criteria:

✅ Multi-carrier orchestration boundary exists

✅ Future Search Platform has a single search execution entry point

✅ Tests passing

✅ Documentation updated

✅ Commit created

✅ Push completed

---

## Phase 15.6

Universal PUDO Engine Integration Closure

Status:

Planned

Objectives:

- End-to-end validation
- Documentation synchronization
- Architecture validation
- Completion review

Exit Criteria:

✅ Engine Catalog Foundation completed

✅ Carrier Catalog Integration Service completed

✅ Engine Search Foundation completed

✅ Organisation Search Foundation completed

✅ Multi-Carrier Execution Foundation completed

✅ Documentation Updated

✅ Tests Passing

✅ Commit Created

✅ Push Completed

---

# PHASE 16

Search Platform

Status:

Planned

---

# PHASE 17

Map Experience

Status:

Planned

Technology:

- Leaflet
- OpenStreetMap

---

# PHASE 18

Export Platform

Status:

Planned

---

# PHASE 19

Administration Portal

Status:

Planned

---

# PHASE 20

Public API Foundation

Status:

Planned

Future ADR:

ADR-0007 Public API Strategy

---

# PHASE 21

Observability And Audit

Status:

Planned

---

# PHASE 22

Security Hardening

Status:

Planned

Objectives:

- Credential Encryption
- MFA Preparation
- Security Review

---

# PHASE 23

Frontend Foundation

Status:

Planned

Technology:

- Next.js
- React
- TypeScript

---

# PHASE 24

Core Upgrade Strategy

Status:

Planned

---

# PHASE 25

Release Preparation

Status:

Planned

---

# PHASE 26

Universal PUDO SaaS v1.0.0

Status:

Future

Release Criteria:

✅ Authentication

✅ Organisations

✅ Users

✅ Memberships

✅ Roles

✅ Carrier Accounts

✅ Searches

✅ Maps

✅ Exports

✅ Administration

---

# CURRENT STATE

Completed:

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

✅ Persistence Test Foundation Implementation

✅ Access Model Foundation

✅ Tenant Access Foundation

✅ Role Persistence Foundation

✅ Carrier Account SQLAlchemy Foundation

✅ Carrier Credential Foundation

✅ Carrier Account Persistence Test Foundation

✅ Carrier Account Repository Foundation

✅ Carrier Credential Repository Foundation

✅ Carrier Account Service Foundation

✅ Carrier Credential Service Foundation

✅ Carrier Account API Foundation

✅ Carrier Credential API Foundation

✅ Engine Catalog Foundation

✅ Carrier Catalog Integration Service

✅ Engine Search Foundation

---

Current Focus:

Phase 15.5

Multi-Carrier Execution Foundation

---

Future Validation Gate:

Universal PUDO Engine Integration

---

# CURRENT TECHNICAL BASELINE

Validated:

✅ FastAPI

✅ PostgreSQL 17

✅ SQLAlchemy

✅ Alembic

✅ Universal PUDO Engine v1.0.0

✅ Organisation Model

✅ User Model

✅ Membership Model

✅ Authentication Fields

✅ Password Hashing

✅ JWT

✅ Authentication Service

✅ Authentication API

✅ User Lookup Foundation

✅ 133 Automated Tests

✅ Organisation Persistence Tests

✅ User Persistence Tests

✅ Membership Persistence Tests

✅ users.is_platform_admin

✅ SAAS_ADMIN persistence

✅ OWNER / VIEWER role strategy

✅ CarrierAccount Model

✅ CarrierCredential Model

✅ carrier_accounts table

✅ carrier_credentials table

✅ carrier_code reference strategy

✅ Universal PUDO Engine carrier catalog ownership

✅ CarrierAccount Repository

✅ CarrierCredential Repository

✅ CarrierAccount Repository Tests

✅ CarrierCredential Repository Tests

✅ Engine Catalog Models

✅ Engine Catalog Client

✅ Engine Catalog Service

✅ Engine Catalog Tests

✅ Carrier Catalog Service

✅ Carrier Catalog Service Tests

✅ Engine Search Models

✅ Engine Search Client

✅ Engine Search Service

✅ Engine Search Tests

---

# CURRENT DATABASE STATE

Database:

universal_pudo_saas

Tables:

- alembic_version
- organisations
- users
- memberships

Authentication Fields:

- password_hash
- is_active
- is_verified
- last_login_at
- is_platform_admin

Carrier Account Tables:

- carrier_accounts
- carrier_credentials

Carrier Account Migrations:

- 3fb1f82a4474_create_carrier_accounts_table
- 2bc5746479e6_create_carrier_credentials_table

---

# PHASE COMPLETION RULE

A phase is completed only when:

1. Development Finished

2. Validation Finished

3. PostgreSQL Validated

4. Tests Passing

5. Documentation Updated

6. Commit Created

7. Push Completed

8. Forward Approved

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

Implemented:

- POST /auth/login
- GET /auth/me

Implemented:

- JWT Authentication Flow
- User Lookup Foundation
- Repository-Based Authentication

42 automated tests passing.

---

2026-07-25

Persistence Test Foundation selected as next milestone.

---

2026-07-25

Persistence Test Foundation implemented.

Added:

- test_organisation_persistence.py
- test_user_persistence.py
- test_membership_persistence.py

Validated:

- session.add()
- session.commit()
- session.refresh()
- session.get()
- session.delete()

- PostgreSQL persistence
- CRUD persistence
- Foreign key persistence

52 automated tests passing.

Documentation synchronization in progress.

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

- CarrierAccount model
- CarrierCredential model
- carrier_accounts table
- carrier_credentials table
- Carrier Account persistence tests
- Carrier Credential persistence tests

Validated:

- Universal PUDO Engine owns carrier catalog
- SaaS does not persist carrier definitions
- SaaS references carriers through carrier_code
- Carrier credentials belong to carrier accounts
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

- Engine Catalog and CarrierAccount crossing
- Carrier.code to CarrierAccount.carrier_code mapping
- Available carrier listing
- Organisation carrier listing
- Activatable carrier listing

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
- Address SaaS projection
- GeoLocation SaaS projection
- PickupType SaaS enum
- EngineSearchClient
- InMemoryEngineSearchClient
- EngineSearchService
- pickup point search
- pickup point radius search
- pickup point detail retrieval
- carrier pickup point listing

Result:

130 passed
0 failed
