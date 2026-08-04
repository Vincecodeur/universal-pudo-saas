# Universal PUDO SaaS - Roadmap

Version: 2.4.0
Status: Phase 18.3 Information Architecture Ready To Start
Last Updated: 2026-08-03

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

Completed

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

Completed

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

✅ multi_carrier_search/
✅ MultiCarrierSearchService
✅ test_multi_carrier_search_service.py

Validation:

✅ MultiCarrierSearchService implemented
✅ MultiCarrierSearchService uses OrganisationSearchService
✅ PickupPoint results returned
✅ No Engine modification
✅ No SQLAlchemy model
✅ No Alembic migration
✅ test_multi_carrier_search_service.py passing
✅ 136 automated tests passing

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

Completed

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
Completed

## Phase 16.1

Search Domain Design

Objectives:

- Define Search Platform scope
- Define SearchRequest concept
- Define SearchResult concept
- Define Search Platform boundaries
- Confirm persistence boundaries
- Prepare Phase 16.2

Out of Scope:

- Search persistence
- SearchHistory table
- SearchResult table
- Alembic migration

## Phase 16.2

Search Platform Models Foundation

Status:

Completed ✅

Deliverables Completed

✅ SearchRequest
✅ SearchResult
✅ tests/test_search_platform_models.py
✅ 142 tests passing

## Phase 16.3

Search Platform Service Foundation

Status:

Completed ✅

Deliverables Completed:

✅ search_platform/service.py
✅ SearchPlatformService
✅ test_search_platform_service.py

Validated:

✅ SearchRequest consumed
✅ MultiCarrierSearchService delegation
✅ SearchResult produced
✅ No persistence
✅ No SQLAlchemy model
✅ No Alembic migration
✅ No Engine modification

Result:

145 passed
0 failed

## Phase 16.4

Search Result Enrichment Foundation

Status:

Completed ✅

Objectives:

- enrich SearchResult output
- define search execution metadata
- prepare future API response format
- keep Search Platform non-persistent
- preserve Universal PUDO Engine boundaries

Deliverables:

- SearchResult enrichment fields
- Search Platform service enrichment logic
- Dedicated tests

Out of Scope:

- FastAPI routes
- SQLAlchemy models
- Alembic migrations
- Search persistence
- Export generation
- Ranking

Result:

150 passed
0 failed

## Phase 16.5

Search Platform Validation

Status:

Completed ✅

Objectives:

- Validate complete Search Platform workflow
- Validate SearchRequest lifecycle
- Validate SearchResult lifecycle
- Validate metadata enrichment
- Prepare Phase 16.6 closure

Validation Criteria:

✅ SearchRequest validated

✅ SearchResult validated

✅ SearchExecutionMetadata validated

✅ SearchPlatformService validated

✅ MultiCarrierSearchService integration validated

✅ No persistence introduced

✅ No migration introduced

✅ No Universal PUDO Engine modification

✅ Tests passing

## Phase 16.6

Search Platform Closure

Status:

Completed

Objectives:

- Freeze Search Platform contract
- Validate final architecture boundaries
- Confirm non-persistence strategy
- Synchronize documentation
- Prepare Phase 16 completion
- Prepare Phase 17 Planning Freeze

---

# PHASE 17

Map Experience

Status:  
Completed

Objective

Allow users to visualize, explore and select PickupPoints from SearchResult through an interactive map experience.

Scope

- Leaflet integration
- OpenStreetMap integration
- Marker rendering
- Carrier logo display
- Carrier name display
- Carrier color display
- Popup display
- PickupPoint selection
- SearchResult visualization
- Clustering
- User geolocation
- Auto fit bounds
- Search filtering

Out of Scope

- Search persistence
- Search history
- Carrier branding administration
- Carrier publication management
- Engine modifications
- Search contract modifications

## 17.1 Map Domain Design

Status:

Completed

Deliverables:

✅ docs/map-experience-design.md

Validated:

✅ SearchResult remains the unique business contract
✅ No MapSearchResult
✅ No MapPickupPoint
✅ Single pickup point selection
✅ Selection reset on new SearchResult
✅ Carrier visibility strategy
✅ Carrier branding ownership
✅ Analytics-ready map design
✅ No persistence introduced

## 17.2 Map Models Foundation

Status:

Completed

Deliverables:

✅ docs/map-models-foundation.md

Validated:

✅ Map state model defined
✅ Marker projection model defined
✅ Popup projection model defined
✅ Carrier visibility model defined
✅ Pickup point selection model defined
✅ SearchResult reset strategy defined
✅ Analytics boundary defined
✅ SearchResult remains unchanged
✅ No MapSearchResult introduced
✅ No MapPickupPoint introduced
✅ No persistence introduced
✅ No SQLAlchemy model introduced
✅ No migration introduced
✅ No Engine modification introduced

## 17.3 Map Service Foundation

Status:
Completed

Deliverables:
✅ map_service/**init**.py
✅ map_service/models.py
✅ map_service/service.py
✅ test_map_models.py
✅ test_map_service.py

Validated:
✅ SearchResult projection
✅ MapProjectionResult
✅ MapMarker projection
✅ MapPopup projection
✅ Carrier visibility filtering
✅ Selection validation
✅ Branding projection
✅ No persistence
✅ No SQLAlchemy
✅ No migration
✅ No Engine modification

Result:
166 passed
0 failed

### 17.4 Leaflet Integration Foundation

Status:
Planning Freeze Completed

Deliverables:
✅ docs/leaflet-integration-design.md

Validated:
✅ Leaflet architectural position defined
✅ MapProjectionResult consumption rule defined
✅ Marker lifecycle defined
✅ Popup lifecycle defined
✅ Carrier logo strategy defined
✅ Carrier color strategy defined
✅ Map refresh strategy defined
✅ Selection strategy defined
✅ Frontend boundary defined
✅ Backend boundary preserved
✅ Out-of-scope rules documented
✅ No persistence introduced
✅ No SQLAlchemy model introduced
✅ No migration introduced
✅ No Engine modification introduced
✅ Phase 17.5 identified

### 17.5 Leaflet Component Foundation

Status: Completed

Deliverables:
✅ docs/leaflet-component-foundation.md

Validated:
✅ component responsibilities defined
✅ adapter boundary defined
✅ marker rendering strategy defined
✅ popup rendering strategy defined
✅ selection lifecycle defined
✅ empty state strategy defined
✅ branding rendering strategy defined
✅ map refresh strategy defined

### 17.6 Map Experience Validation

Status: Completed

Validated:
✅ SearchResult boundary
✅ MapService boundary
✅ MapProjectionResult consumption
✅ marker lifecycle
✅ popup lifecycle
✅ selection lifecycle
✅ frontend boundary
✅ Engine boundary
✅ carrier branding boundary
✅ persistence boundary

### 17.7 Map Experience Closure

Status:
Completed

Objectives:

- confirm Phase 17 completion
- confirm architecture stability
- confirm documentation synchronization
- prepare transition to Phase 18
- freeze Map Experience foundation

Validated:
✅ architecture stability
✅ documentation synchronization
✅ SearchResult boundary preservation
✅ MapService boundary preservation
✅ MapProjectionResult boundary preservation
✅ carrier branding boundary preservation
✅ persistence boundary preservation

Result:
Phase 17 completed.

---

# PHASE 18

Frontend MVP

Current Active Subphase:
18.3 Information Architecture

Status:
In Progress

Objectives:

- create frontend application foundation
- create authentication-aware frontend shell
- prepare pickup point search interface
- consume MapProjectionResult
- prepare map display foundation
- prepare marker rendering
- prepare popup rendering
- prepare pickup point selection interaction
- preserve SearchResult boundary
- preserve MapService boundary
- avoid backend persistence changes
- avoid Universal PUDO Engine modifications

Expected Deliverables:

- frontend application structure
- frontend routing foundation
- authentication-aware layout
- search view foundation
- map view foundation
- frontend map consumption contract
- documentation update

### 18.1 Frontend Product Vision

Status:
Completed

Deliverables:
✅ docs/frontend-mvp-vision.md

Validated:
✅ Search Driven strategy
✅ Map Enhanced strategy
✅ Desktop First approach
✅ Carrier Accounts page identified
✅ Search as primary entry point
✅ Frontend MVP scope frozen

### 18.2 User Personas & User Journeys

Status:
Completed

Objectives:

- define technical roles
- define business personas
- map technical roles to business personas
- define primary user journeys
- define secondary user journeys
- clarify pickup point selection meaning
- clarify search independence from orders
- clarify carrier filter optionality
- document unresolved address search decision

Deliverables:
✅ docs/user-personas-and-user-journeys.md

Validated:
✅ Viewer mapped to Operations User
✅ Owner mapped to Transport Configuration Manager
✅ SaaS Administrator mapped to Platform Administrator
✅ Search remains independent from orders
✅ Address is required
✅ Carrier is optional
✅ Default carrier value is "All available carriers"
✅ Pickup point selection is the final MVP action
✅ Selection is non-persistent
✅ Selection triggers no reservation, shipment, label or carrier workflow
✅ Address search nature remains unresolved for later phases
✅ Phase 18.3 Information Architecture identified as next phase

### 18.3 Information Architecture

Status:
Ready To Start

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

Known Open Decision:
UX-D001 - Address Search Strategy

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

### 18.4 UX Strategy

### 18.5 UI Strategy & Design System

### 18.6 Accessibility Strategy

### 18.7 Responsive Strategy

### 18.8 Security UX Strategy

### 18.9 Frontend Architecture Design

### 18.10 Data Fetching & State Strategy

### 18.11 Frontend Quality Strategy

### 18.12 Error Handling Strategy

### 18.13 Frontend Observability Strategy

### 18.14 Frontend Planning Freeze

### 18.15 Frontend Foundation

### 18.16 Authentication UX Foundation

### 18.17 Application Shell Foundation

### 18.18 Search Experience Foundation

### 18.19 Search Results Foundation

### 18.20 Map Experience Integration

### 18.21 Frontend Validation

### 18.22 Frontend Closure

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

ADR-0011 Public API Strategy

---

# PHASE 21

Observability And Audit

Status:

Planned

---

# PHASE 22

Export Platform

Status:
Deferred

Reason:
Export Platform is deferred until after Observability And Audit.

Export Platform will be revisited when the platform has validated data sources for operational exports, such as:

- usage metrics
- search history
- audit events
- dashboard data
- carrier performance data
- reporting data

Objectives:

- define export use cases
- define export consumers
- define exportable data
- define export formats
- define export persistence strategy if required
- preserve platform boundaries

# PHASE 23

Security Hardening

Status:

Planned

Objectives:

- Credential Encryption
- MFA Preparation
- Security Review

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

✅ Phase 15.1 Engine Catalog Foundation

✅ Phase 15.2 Carrier Catalog Integration Service

✅ Phase 15.3 Engine Search Foundation

✅ Phase 15.4 Organisation Search Foundation

✅ Phase 15.5 Multi-Carrier Execution Foundation

✅ Phase 15.6 Universal PUDO Engine Integration Closure

✅ Organisation Search Foundation

✅ Multi-Carrier Execution Foundation

✅ Universal PUDO Engine Integration Closure

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

Current Focus:

Phase 18.3
Information Architecture

Status:
Ready To Start

---

Next Validation Gate:  
Phase 18.14 Frontend Planning Freeze

---

# CURRENT TECHNICAL BASELINE

Validated:

✅ Search Platform Enrichment Tests

✅ Search Result Enrichment

✅ SearchExecutionMetadata

✅ Organisation Search Service

✅ MultiCarrierSearchService

✅ Multi-Carrier Search Tests

✅ Organisation Search Tests

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

✅ SearchRequest

✅ SearchResult

✅ SearchPlatformService

✅ Search Platform Service Tests

✅ 166 Automated Tests

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

---

2026-07-27

Organisation Search Foundation completed.

Implemented:

- organisation_search/service.py
- test_organisation_search_service.py

Validated:

- organisation-based pickup point search
- carrier filtering through organisation carriers
- pickup point result aggregation

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

Search Platform Models Foundation completed.

Implemented:

- search_platform/models.py
- SearchRequest
- SearchResult
- test_search_platform_models.py

Validated:

- Search request DTO
- Search result DTO
- Independent list defaults
- No persistence
- No migration

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

2026-07-30

Phase 17.4 Leaflet Integration Planning Freeze completed.

Implemented:

- docs/leaflet-integration-design.md

Validated:

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
- No persistence
- No SQLAlchemy model
- No migration
- No Engine modification

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
