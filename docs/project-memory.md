# Universal PUDO SaaS - Project Memory

Version: 1.4.0

Status: Active

Last Updated: 2026-08-04

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
- search platform service boundary

Universal PUDO Engine owns:

- carrier integrations
- provider implementations
- search orchestration
- normalization
- carrier intelligence

The SaaS consumes the Universal PUDO Engine.

The SaaS must never duplicate Universal PUDO Engine responsibilities.

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

The Universal PUDO Engine consumes credentials.

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

Avoid duplicating Universal PUDO Engine responsibilities inside the SaaS.

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

## D009

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
- SearchExecutionMetadata

Phase 16 must not introduce:

- SearchResult table
- SearchHistory table
- Alembic migration
- Search persistence

Reason:

Search Platform domain boundaries must be stabilised before persistence decisions.

---

## D011

Map Experience Strategy

Decision:

Phase 17 Map Experience was frozen before implementation.

SearchResult remains the unique business contract.

Map Experience is a presentation layer.

Map Experience consumes SearchResult without introducing new search models.

Carrier branding is consumed by Map Experience.

Carrier branding administration belongs to Phase 19 Administration Portal.

Status:

Planning Freeze Completed

Reason:

Prevent duplication of business contracts and preserve Search Platform boundaries.

### D012

Carrier Visibility Strategy

Decision:

Carrier availability and carrier visibility are separate concepts.

Carrier availability:

- Engine published carrier
- Active organisation CarrierAccount

Carrier visibility:

- User display preference

Users may only display carriers available to their organisation.

### D013

Analytics Ready Map Strategy

Decision:

PickupPoint selection is considered a future business event.

Phase 17 remains non-persistent.

Future analytics may reuse pickup point selections without introducing persistence during Map Experience foundations.

### D014

Map Service Strategy

Decision:

Map Experience consumes SearchResult
through MapService projections.

MapService produces:

- MapMarker
- MapPopup
- MapProjectionResult

MapService remains non-persistent.

Reason:

Preserve SearchResult as the unique
search business contract while preparing
frontend map consumption.

#### D015

Leaflet Integration Strategy

Decision:
Leaflet consumes MapProjectionResult.

Leaflet does not consume SearchResult directly.

Leaflet does not consume Universal PUDO Engine directly.

Leaflet remains a presentation technology and must not become a business layer.

Phase 17.4 defines:

- Leaflet architectural position
- marker lifecycle
- popup lifecycle
- carrier logo strategy
- carrier color strategy
- map refresh strategy
- selection strategy
- frontend boundary
- backend boundary
- out-of-scope implementation rules

Reason:
Preserve SearchResult as the business contract and MapProjectionResult as the presentation contract before frontend implementation starts.

#### D016

Leaflet Component Foundation Strategy

Decision:

Phase 17.5 defines the first frontend-facing Leaflet component foundation.

Leaflet consumes MapProjectionResult.

Leaflet component responsibilities:

- marker rendering
- popup rendering
- selection handling
- empty state rendering

Leaflet does not own:

- search execution
- SearchResult interpretation
- carrier administration
- persistence

Phase 17.5 preserves:

- SearchResult business contract
- MapProjectionResult presentation contract
- MapService boundary

Reason:

Freeze frontend responsibilities before implementation starts.

#### D017

Roadmap Reprioritization - Frontend Before Export Platform

Decision:

Frontend MVP is moved to Phase 18.

Export Platform is moved to Phase 22.

Reason:

Export Platform does not yet have a validated business use case.

No confirmed export consumer exists yet.

The platform does not yet have frontend usage, observability data, audit data or dashboard data to justify export implementation.

Frontend MVP provides immediate product value by enabling users to interact with the existing Search Platform and Map Experience foundations.

Export Platform becomes more relevant after Observability And Audit.

Accepted Roadmap:

- Phase 18 Frontend MVP
- Phase 19 Administration Portal
- Phase 20 Public API
- Phase 21 Observability And Audit
- Phase 22 Export Platform
- Phase 23 Security Hardening

### D018

Frontend MVP Strategy

Decision:

Frontend MVP follows a documentation-first approach.

All UX, UI, accessibility, security, architecture,
quality and observability decisions must be frozen
before frontend implementation starts.

Frontend implementation begins only after
Phase 18.14 Frontend Planning Freeze.

Frontend MVP execution phases:

18.1 Frontend Product Vision

18.2 User Personas & User Journeys

18.3 Information Architecture

18.4 UX Strategy

18.5 UI Strategy & Design System

18.6 Accessibility Strategy

18.7 Responsive Strategy

18.8 Security UX Strategy

18.9 Frontend Architecture Design

18.10 Data Fetching & State Strategy

18.11 Frontend Quality Strategy

18.12 Error Handling Strategy

18.13 Frontend Observability Strategy

18.14 Frontend Planning Freeze

18.15 Frontend Foundation

18.16 Authentication UX Foundation

18.17 Application Shell Foundation

18.18 Search Experience Foundation

18.19 Search Results Foundation

18.20 Map Experience Integration

18.21 Frontend Validation

18.22 Frontend Closure

### D019

Frontend User Personas And User Journeys Strategy

Decision:
Phase 18.2 defines business personas separately from technical roles.

Technical roles:

- Viewer
- Owner
- SaaS Administrator

Business personas:

- Operations User
- Transport Configuration Manager
- Platform Administrator

Role mapping:

- Viewer maps primarily to Operations User
- Owner maps primarily to Transport Configuration Manager
- SaaS Administrator maps to Platform Administrator

Frontend MVP user journey remains:
Login
↓
Search
↓
Results
↓
Map
↓
Pickup Point Details
↓
Select Pickup Point

Search is independent from any order, OMS workflow, WMS workflow or shipment workflow.

Address is required.

Carrier is optional.

Default carrier value:
All available carriers.

Pickup point selection is the final MVP action.

Selection does not trigger:

- reservation
- shipment creation
- parcel creation
- label creation
- carrier workflow
- persistence

Selection remains active until a new SearchResult is generated.

A new SearchResult resets the current selection.

Address search nature remains unresolved and must be handled in later frontend phases.

Unresolved decision:
UX-D001 - Address Search Strategy

Impacted future phases:

- Phase 18.3 Information Architecture
- Phase 18.4 UX Strategy
- Phase 18.9 Frontend Architecture Design
- Phase 18.10 Data Fetching And State Strategy

Reason:
Personas and journeys must be frozen before Information Architecture starts.

### D020

Information Architecture Strategy

Decision:

Phase 18.3 freezes:

- page inventory
- navigation hierarchy
- route structure
- application layout
- Search page architecture
- Carrier Accounts architecture
- Search / Results / Map relationship

Key Decisions:

- Search is homepage
- Results are authoritative
- Map reflects results
- Left sidebar navigation
- Right drawer pickup point details
- Multiple carrier accounts per carrier
- Non-persistent selection
- Non-persistent searches

Reason:

Freeze information structure before UX and UI decisions.

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

Universal PUDO Engine and SaaS remain independent.

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

✅ Frontend MVP Vision

✅ Information Architecture

✅ docs/information-architecture.md

✅ docs/frontend-mvp-vision.md

✅ User Personas And User Journeys

✅ docs/user-personas-and-user-journeys.md

✅ Map Experience Validation

✅ docs/map-experience-validation.md

✅ Leaflet Integration Planning Freeze

✅ Leaflet Component Foundation

✅ docs/leaflet-component-foundation.md

✅ docs/leaflet-integration-design.md

✅ Map Service Foundation

✅ MapService

✅ MapProjectionResult

✅ MapMarker

✅ MapPopup

✅ MapViewState

✅ Search Platform Validation

✅ Search Result Enrichment Foundation

✅ SearchExecutionMetadata

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

✅ Search Platform Models Foundation

✅ SearchRequest

✅ SearchResult

✅ Search Platform Service Foundation

✅ SearchPlatformService

---

# CURRENT DOMAIN MODEL

Search Platform

✅ SearchRequest

✅ SearchResult

✅ SearchExecutionMetadata

✅ SearchPlatformService

✅ Non-persistent

✅ Validated

✅ MultiCarrierSearchService

✅ OrganisationSearchService

---

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

✅ test_search_platform_service.py

✅ test_search_platform_models.py

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

166 passed

0 failed

---

# CURRENT CODE STATUS

Implemented

✅ SearchExecutionMetadata

✅ SearchResult enrichment

✅ execution metadata support

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

✅ SearchRequest

✅ SearchResult

✅ search_platform/models.py

✅ SearchPlatformService

✅ search_platform/service.py

✅ test_search_platform_service.py

✅ Search Platform Service Foundation Completed

✅ Search Result Enrichment Foundation Completed

✅ Search Platform Validation

✅ Search Platform Closure

✅ Map Domain Design

✅ Map Models Foundation

✅ docs/map-models-foundation.md

✅ docs/leaflet-integration-design.md

---

Not Implemented

❌ Permission Enforcement
❌ Search Persistence
❌ Exports
❌ Administration
⏳ Frontend MVP Planning
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

Universal PUDO Engine and SaaS boundaries must remain explicit.

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

Lesson 024

Business contracts must be reused across presentation layers.

SearchResult remains the unique search contract.

Map-specific contracts should not be introduced unless business requirements differ.

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

✅ Phase 16.1 Search Domain Design

✅ Phase 16.2 Search Platform Models Foundation

✅ Phase 16.3 Search Platform Service Foundation

✅ Phase 16.4 Search Result Enrichment Foundation

✅ Phase 16.5 Search Platform Validation

✅ Phase 16.6 Search Platform Closure

✅ Phase 17.1 Map Domain Design

✅ Phase 17.2 Map Models Foundation

✅ Phase 17.3 Map Service Foundation

✅ Phase 17.4 Leaflet Integration Planning Freeze

✅ Phase 17.5 Leaflet Component Foundation

✅ Phase 17.6 Map Experience Validation

✅ docs/map-experience-validation.md

---

Current Focus

Phase 18.4
UX Strategy

Status:
Ready To Start

---

# NEXT MILESTONE

Phase 18.4
UX Strategy

Objectives:

- define page inventory
- define navigation hierarchy
- define route structure
- define Search page composition
- define Carrier Accounts access relationship
- define Search and Map relationship
- define pickup point detail drawer placement
- document information architecture decisions
- preserve personas and journeys defined in Phase 18.2

Out Of Scope:

- frontend implementation
- final UI design
- design system
- frontend state management
- frontend data fetching
- address search implementation decision
- backend redesign
- database changes
- Universal PUDO Engine modifications

---

# FUTURE MILESTONES

Phase 18 Frontend MVP
↓
Phase 19 Administration Portal
↓
Phase 20 Public API
↓
Phase 21 Observability And Audit
↓
Phase 22 Export Platform
↓
Phase 23 Security Hardening
↓
Phase 24 Universal PUDO Engine Upgrade Strategy
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

---

2026-07-27

Search Platform Models Foundation completed.

Implemented:

- search_platform/models.py
- SearchRequest
- SearchResult
- test_search_platform_models.py

Validated:

- Search request DTO
- Search result DTO
- Default list isolation
- No persistence
- No migration
- No database impact

Result:

142 passed

0 failed

---

2026-07-28

Search Platform Service Foundation completed.

Implemented:

- search_platform/service.py
- SearchPlatformService
- test_search_platform_service.py

Validated:

- SearchRequest consumption
- MultiCarrierSearchService delegation
- SearchResult generation
- No persistence
- No migration
- No database impact
- No Universal PUDO Engine modification

Result:

145 passed
0 failed

---

2026-07-28

Search Result Enrichment Foundation completed.

Implemented:

- SearchExecutionMetadata
- SearchResult enrichment

Validated:

- execution metadata
- duration measurement
- applied filters

Result:

150 passed
0 failed

---

2026-07-28

Search Platform Validation completed.

Validated:

- SearchRequest lifecycle
- SearchResult lifecycle
- SearchExecutionMetadata
- SearchPlatformService
- Search Platform boundaries
- MultiCarrierSearchService integration

Result:

150 passed
0 failed

---

2026-07-28

Phase 17 Map Experience Planning Freeze completed.

Validated:

- SearchResult remains the unique business contract
- Map Experience is a presentation layer
- No MapSearchResult model
- No MapPickupPoint model
- Carrier branding is consumed by Map Experience
- Carrier branding administration belongs to Phase 19 Administration Portal

Next execution step:

Phase 17.1 Map Domain Design

---

2026-07-30

Phase 17.1 Map Domain Design completed.

Implemented:

- docs/map-experience-design.md

Validated:

- SearchResult remains the unique business contract
- No MapSearchResult model
- No MapPickupPoint model
- Single pickup point selection
- Selection reset on new SearchResult
- Carrier visibility strategy
- Carrier branding ownership strategy
- Analytics-ready map design
- No persistence introduced

Result:

Phase 17.1 completed.
Phase 17.2 designated as next milestone.

---

2026-07-30

Phase 17.2 Map Models Foundation completed.

Implemented:

- docs/map-models-foundation.md

Validated:

- Map state model
- Marker projection model
- Popup projection model
- Carrier visibility model
- Pickup point selection model
- SearchResult reset strategy
- Analytics boundary
- No MapSearchResult
- No MapPickupPoint
- No persistence
- No SQLAlchemy model
- No migration
- No Engine modification

Result:

Phase 17.2 completed.
Phase 17.3 designated as next milestone.

---

2026-07-30
Phase 17.3 Map Service Foundation completed.

Implemented:

- map_service/**init**.py
- map_service/models.py
- map_service/service.py
- test_map_models.py
- test_map_service.py

Validated:

- MapService
- MapProjectionResult
- MapMarker projection
- MapPopup projection
- Carrier visibility filtering
- Pickup point selection validation
- Branding projection support

Result:
166 passed
0 failed

Next milestone:
Phase 17.4 Leaflet Integration Foundation

---

2026-07-30

Phase 17.4 Leaflet Integration Planning Freeze completed.

Implemented:

- docs/leaflet-integration-design.md

Defined:

- Leaflet architectural position
- MapProjectionResult consumption rule
- Marker lifecycle
- Popup lifecycle
- Carrier logo strategy
- Carrier color strategy
- Map refresh strategy
- Selection strategy
- Frontend boundary
- Backend boundary
- Out-of-scope implementation rules

Validated:

- Leaflet consumes MapProjectionResult
- Leaflet does not consume SearchResult directly
- Leaflet does not consume Universal PUDO Engine directly
- No persistence
- No SQLAlchemy model
- No migration
- No Engine modification
- No frontend implementation

Result:
Phase 17.4 Planning Freeze completed.

Next milestone:
Phase 17.5 Leaflet Component Foundation

---

2026-08-02

Phase 17.5 Leaflet Component Foundation completed.

Implemented:

- docs/leaflet-component-foundation.md

Defined:

- component responsibilities
- Leaflet adapter boundary
- marker rendering strategy
- popup rendering strategy
- selection strategy
- empty state strategy
- branding rendering strategy
- map refresh strategy

Validated:

- SearchResult remains business contract
- MapProjectionResult remains presentation contract
- No persistence
- No SQLAlchemy model
- No migration
- No Engine modification

Next milestone:
Phase 17.6 Map Experience Validation

---

2026-08-02

Phase 17.6 Map Experience Validation completed.

Implemented:

- docs/map-experience-validation.md

Validated:

- SearchResult boundary
- MapService boundary
- MapProjectionResult consumption
- marker lifecycle
- popup lifecycle
- selection lifecycle
- frontend responsibility boundary
- Engine boundary
- carrier branding boundary
- persistence boundary

Next milestone:
Phase 17.7 Map Experience Closure

---

2026-08-02

Phase 17.7 Map Experience Closure started.

Status:
In Progress

Objectives:

- confirm Phase 17 completion
- confirm architecture stability
- confirm documentation synchronization
- prepare transition to Phase 18
- freeze Map Experience foundation

---

2026-08-02

Phase 17.7 Map Experience Closure completed.

Validated:

- architecture stability
- documentation synchronization
- SearchResult boundary preservation
- MapService boundary preservation
- MapProjectionResult boundary preservation
- carrier branding boundary preservation
- persistence boundary preservation

Result:

Phase 17 closed.

Next milestone:

Phase 18 Frontend MVP

---

2026-08-03  
Phase 18.2 User Personas And User Journeys completed.  
Implemented:

- docs/user-personas-and-user-journeys.md

Validated:

- technical roles
- business personas
- role-to-persona mapping
- Operations User journey
- Transport Configuration Manager journey
- Platform Administrator MVP relevance
- search independence from orders
- required address input
- optional carrier filter
- default carrier value as All available carriers
- pickup point selection as final MVP action
- non-persistent selection
- no reservation, shipment, label or carrier workflow attached to selection
- address search nature documented as unresolved future decision

Next milestone:
Phase 18.3 Information Architecture

---

2026-08-04

Phase 18.3 Information Architecture completed.

Implemented:

- docs/information-architecture.md

Validated:

- navigation hierarchy
- route structure
- page inventory
- Search page architecture
- Carrier Accounts architecture
- Search / Results / Map relationship
- Pickup Point Detail drawer strategy
- left sidebar navigation strategy
- Search homepage strategy
- non-persistent selection strategy
- responsive-ready architecture

Next milestone:
Phase 18.4 UX Strategy
