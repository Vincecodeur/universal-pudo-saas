# Universal PUDO SaaS - Architecture

Version: 2.5.0

Status: Phase 17.7 Closure In Progress

Last Updated: 2026-08-02

---

# PURPOSE

This document defines the target architecture of Universal PUDO SaaS.

The objective is to:

- isolate business responsibilities
- separate SaaS concerns from carrier intelligence
- support multi-tenancy
- support future self-hosted deployments
- preserve long-term maintainability
- keep the product focused on PUDO information access and consumption
- prevent architectural confusion between Universal PUDO SaaS and Universal PUDO Engine

This document describes the target architecture, validated implementation decisions, current architectural state, and next architectural direction.

---

# SOURCE OF TRUTH

Architecture decisions must remain aligned with:

1. Source code
2. Tests
3. Database schema
4. Approved ADRs
5. Architecture documents
6. Roadmap
7. Project documentation

When conflicts exist, source code and tests win.

---

# SOLUTION OVERVIEW

Universal PUDO SaaS is a multi-tenant application built on top of Universal PUDO Engine.

Universal PUDO SaaS owns:

- authentication
- organisations
- users
- memberships
- tenant access model
- carrier accounts
- carrier credentials
- organisation carrier activation
- search consumption experience
- multi-carrier search entry point
- dashboard configuration
- exports
- administration
- SaaS-level access control
- future frontend

Universal PUDO Engine owns:

- carrier provider implementations
- carrier integrations
- carrier clients
- carrier response parsing
- carrier mapping
- pickup point retrieval
- pickup point normalization
- carrier abstraction
- provider execution
- provider health
- carrier lifecycle
- carrier capabilities
- carrier catalog implementation
- carrier intelligence related to PUDO search

The SaaS consumes Universal PUDO Engine.

The SaaS must never duplicate Engine responsibilities.

---

# PRODUCT ARCHITECTURE PRINCIPLE

Universal PUDO SaaS is not a generic logistics platform.

Universal PUDO SaaS exists to provide access to PUDO information.

The platform must remain focused on:

- pickup point access
- pickup point search
- pickup point visualization
- pickup point analytics
- pickup point consumption
- pickup point data export

The following concepts are out of scope unless directly required for PUDO access or PUDO consumption:

- shipment creation
- label generation
- tracking management
- delivery orchestration
- transport rating
- transport execution
- carrier product catalog management
- carrier service catalog management
- non-PUDO carrier capabilities

This rule protects the product from drifting toward a generic OMS, WMS, TMS, or shipping platform.

---

# HIGH LEVEL ARCHITECTURE

```text
+-----------------------------+
| Frontend                    |
| Next.js / React             |
+-------------+---------------+
              |
              v
+-----------------------------+
| FastAPI Backend             |
| Universal PUDO SaaS         |
+-------------+---------------+
              |
              v
+-----------------------------+
| PostgreSQL                  |
| universal_pudo_saas         |
+-------------+---------------+
              |
              v
+-----------------------------+
| Universal PUDO Engine       |
| PUDO Carrier Core           |
+-------------+---------------+
              |
              v
+-----------------------------+
| Carrier APIs                |
+-----------------------------+
```

---

# ARCHITECTURAL PRINCIPLES

## P001 - Single Responsibility

Each module owns a specific business domain.

---

## P002 - Clear Separation

Universal PUDO SaaS manages users, tenants, access, credentials, accounts, and customer-facing workflows.

Universal PUDO Engine manages carrier-specific PUDO retrieval, provider execution, carrier metadata, and normalization.

---

## P003 - Independent Databases

Each product owns its own database lifecycle.

Universal PUDO SaaS uses:

```text
universal_pudo_saas
```

Universal PUDO Engine uses:

```text
universal_pudo
```

---

## P004 - Security First

Authentication, tenant access, and credential ownership must be designed before carrier account management and operational search usage.

---

## P005 - Documentation Driven Development

Documentation must be synchronized before phase closure.

---

## P006 - Product Scope Discipline

The SaaS must only model carrier concepts required for PUDO information access and consumption.

---

## P007 - Phase Planning Freeze

Before starting a new phase, sub-phases, objectives, deliverables, validation criteria, and exit criteria must be frozen.

No phase implementation may start until phase planning is completed.

---

# REPOSITORY OWNERSHIP

The ecosystem follows this ownership principle:

```text
Engine owns implementation.
Consumer owns consumption.
Consumer owns its contract documentation.
```

For the current SaaS implementation:

```text
universal-pudo-engine
    owns carrier functionality

universal-pudo-saas
    owns SaaS consumption and user-facing workflows
```

Universal PUDO SaaS owns the Engine ↔ SaaS consumption contract documentation.

Universal PUDO SaaS must not implement carrier-specific provider logic.

---

# DEPLOYMENT STRATEGY

Current Strategy:

```text
SaaS-first
```

Future Strategy:

```text
Self-host-ready
```

Status:

```text
Validated
```

ADR:

```text
ADR-0006
```

---

# REPOSITORY STRATEGY

Decision:

```text
Monorepo
```

Status:

```text
Validated
```

ADR:

```text
ADR-0001
```

---

# MULTI-TENANT STRATEGY

Decision:

```text
Tenant = Organisation
```

Status:

```text
Validated
```

ADR:

```text
ADR-0004
```

Relationship:

```text
Organisation
    ▲
    │
Membership
    │
    ▼
User
```

---

# ACCESS MODEL ARCHITECTURE

The access model is business-driven.

The platform supports three user types in V1:

```text
SAAS_ADMIN
OWNER
VIEWER
```

---

## SaaS Administrator

Scope:

```text
Platform
```

Storage Strategy:

```text
users.is_platform_admin
```

Responsibilities:

- create organisations
- suspend organisations
- manage subscriptions
- manage quotas
- manage billing
- manage platform operations
- manage carrier accounts when required for support or administration
- manage carrier credential visibility rules when required
- monitor platform usage

The SaaS Administrator is not scoped to a single organisation.

---

## Owner

Scope:

```text
Organisation
```

Storage Strategy:

```text
memberships.role = OWNER
```

Responsibilities:

- create Viewer users
- remove Viewer users
- connect carrier accounts
- configure carrier credentials
- test carrier connectivity when available
- enable or disable organisation carrier accounts
- configure dashboards
- configure API access
- manage organisation analytics

The Owner uses carriers exposed by Universal PUDO Engine and referenced through SaaS Carrier Accounts.

---

## Viewer

Scope:

```text
Organisation
```

Storage Strategy:

```text
memberships.role = VIEWER
```

Responsibilities:

- search pickup points
- view dashboards
- view analytics
- export search results
- consume PUDO data

Viewer users cannot modify tenant configuration.

---

# ROLE STORAGE STRATEGY

Official decision:

```text
SAAS_ADMIN -> users.is_platform_admin
OWNER      -> memberships.role
VIEWER     -> memberships.role
```

Rejected strategy:

```text
roles table
permissions table
role_permissions table
dynamic RBAC
```

Reason:

The product currently needs a simple, business-aligned access model.

The V1 roles are fixed and known in advance.

A dynamic RBAC model would introduce unnecessary complexity.

---

# DOMAIN ARCHITECTURE

## Implemented Domains

```text
Organisation
User
Membership
Authentication Model
Authentication Service
Authentication API
User Lookup Foundation
Persistence Test Foundation
CarrierAccount
CarrierCredential
Engine Catalog Consumption
Carrier Catalog Integration
Engine Search Consumption
Organisation Search
Multi-Carrier Search
Search Platform Models
Search Platform Service
Search Result Enrichment
Map Service
Map Projection Models

```

## Future Domains

Frontend
Administration
Public API
Observability And Audit
Exports
Security Hardening

## Phase 16 Search Platform Sub-Phases

```text
16.1 Search Domain Design
16.2 Search Platform Models Foundation
16.3 Search Platform Service Foundation
16.4 Search Result Enrichment Foundation
16.5 Search Platform Validation
16.6 Search Platform Closure
```

# PHASE 17 MAP EXPERIENCE ARCHITECTURE

SearchResult remains the business contract.

Map Experience is a presentation layer.

Map Experience must not introduce:

- MapSearchResult
- MapPickupPoint
- duplicated search contracts

Carrier branding is consumed by Map Experience.

Branding includes:

- logo
- display_name
- color

Carrier branding administration belongs to Administration Portal.

Map Experience is read-only regarding branding configuration.

Design Reference:

docs/map-experience-design.md

Status:
Phase 17.1 Completed

Validated Decisions:

- SearchResult remains the unique business contract.
- No MapSearchResult model.
- No MapPickupPoint model.
- Single pickup point selection.
- Selection reset on new SearchResult.
- Carrier visibility separated from carrier availability.
- Carrier branding owned by SaaS Administration.
- Future analytics enabled without introducing persistence.

Phase 17.2 Map Models Foundation:

docs/map-models-foundation.md

Validated Decisions:

- Map state is UI state.
- Marker projection is derived from SearchResult.
- Popup projection is derived from SearchResult.
- Carrier visibility is a user preference.
- Pickup point selection is UI state.
- New SearchResult resets current selection.
- Analytics boundary is documented without persistence.
- No MapSearchResult introduced.
- No MapPickupPoint introduced.
- No persistence introduced.

Phase 17.3 Map Service Foundation

Validated:

- MapService implemented
- SearchResult remains the business contract
- Marker projection implemented
- Popup projection implemented
- Carrier visibility filtering implemented
- Branding projection implemented
- No persistence introduced
- No SQLAlchemy model introduced
- No migration introduced

Phase 17.4 Leaflet Integration Foundation

Design Reference:
docs/leaflet-integration-design.md

Validated:

- Leaflet consumes MapProjectionResult
- Leaflet does not consume SearchResult directly
- Leaflet does not consume Universal PUDO Engine directly
- Marker lifecycle defined
- Popup lifecycle defined
- Carrier logo strategy defined
- Carrier color strategy defined
- Map refresh strategy defined
- Selection strategy defined
- Frontend boundary defined
- Backend boundary preserved
- Out-of-scope implementation rules documented
- No persistence introduced
- No SQLAlchemy model introduced
- No migration introduced
- No Engine modification introduced
- No frontend implementation introduced

Phase 17.5 Leaflet Component Foundation

Design Reference:
docs/leaflet-component-foundation.md

Validated:

- Leaflet component responsibility defined
- Leaflet adapter responsibility defined
- Marker rendering strategy defined
- Popup rendering strategy defined
- Selection strategy defined
- Empty state strategy defined
- Branding rendering strategy defined
- Map refresh strategy defined
- SearchResult boundary preserved
- MapProjectionResult boundary preserved
- No persistence introduced
- No SQLAlchemy model introduced
- No migration introduced
- No Engine modification introduced

Phase 17.6 Map Experience Validation

Design Reference:
docs/map-experience-validation.md

Validated:

- SearchResult boundary validated
- MapService boundary validated
- MapProjectionResult consumption validated
- marker lifecycle validated
- popup lifecycle validated
- selection lifecycle validated
- frontend responsibility boundary validated
- Engine boundary validated
- carrier branding boundary validated
- persistence boundary validated

Result:
Architecture validated without introducing:

- persistence
- SQLAlchemy models
- migrations
- Engine modifications

---

# CURRENT DOMAIN MODEL

## Organisation

Purpose:

```text
Business tenant.
```

Status:

```text
Implemented
Persisted
Persistence Validated
```

Responsibilities:

- owns memberships
- owns carrier accounts
- owns future dashboard configuration
- owns future search platform usage
- owns future API credentials

---

## User

Purpose:

```text
Platform identity.
```

Status:

```text
Implemented
Persisted
Authentication Ready
Persistence Validated
```

Validated fields:

```text
email
first_name
last_name
password_hash
is_active
is_verified
last_login_at
is_platform_admin
```

---

## Membership

Purpose:

```text
Connect users to organisations.
```

Status:

```text
Implemented
Persisted
Persistence Validated
```

Current fields:

```text
organisation_id
user_id
role
```

Role strategy:

```text
OWNER
VIEWER
```

Membership owns organisation-level role assignment.

---

## Engine Carrier Catalog

Purpose:

```text
Represents carriers exposed by Universal PUDO Engine.
```

Scope:

```text
Universal PUDO Engine
```

Owner:

```text
Universal PUDO Engine
```

Status in SaaS:

```text
Consumed
Not Persisted
Read Model Only
```

Examples:

```text
COLISSIMO
MONDIAL_RELAY
CHRONOPOST
DPD
GLS
UPS
```

Important boundary:

Universal PUDO SaaS does not persist carrier definitions.

---

## CarrierAccount

Purpose:

```text
Represents an organisation-specific carrier account.
```

Scope:

```text
Organisation
```

Owner:

```text
Organisation Owner
```

Status:

```text
Implemented
Persisted
Persistence Validated
Repository Implemented
Service Implemented
API Implemented
```

Current fields:

```text
id
organisation_id
carrier_code
name
is_active
created_at
updated_at
```

Boundary:

```text
CarrierAccount.carrier_code
        ↓
Engine Carrier.code
```

---

## CarrierCredential

Purpose:

```text
Stores carrier authentication values attached to a CarrierAccount.
```

Scope:

```text
CarrierAccount
```

Owner:

```text
Organisation Owner
```

Status:

```text
Implemented
Persisted
Persistence Validated
Repository Implemented
Service Implemented
API Implemented
```

Current fields:

```text
id
carrier_account_id
credential_key
credential_value
created_at
updated_at
```

Security boundary:

Credential encryption is required before production usage.

---

## DashboardConfiguration

Purpose:

```text
Represents dashboard configuration for an organisation.
```

Scope:

```text
Organisation
```

Status:

```text
Future
```

---

## ApiCredential

Purpose:

```text
Represents organisation API access configuration.
```

Scope:

```text
Organisation
```

Status:

```text
Future
```

---

## Search Platform

Purpose:

```text
Represents the customer-facing search capability.
```

Scope:

```text
Organisation
```

Status:
Implemented

✅ SearchRequest
✅ SearchResult
✅ SearchPlatformService

✅ Search Enrichment
✅ SearchExecutionMetadata

Persistence:

```text
Deferred
No database table in Phase 16
```

---

# VALIDATED ENGINE INTEGRATION ARCHITECTURE

The Phase 15 Engine integration is completed.

Validated search architecture:

```text
MultiCarrierSearchService
        ↓
OrganisationSearchService
        ↓
CarrierCatalogService
        ↓
EngineSearchService
        ↓
Universal PUDO Engine
```

Validated services:

```text
engine_catalog/
├── client.py
├── models.py
└── service.py

carrier_catalog/
└── service.py

engine_search/
├── client.py
├── models.py
└── service.py

organisation_search/
└── service.py

multi_carrier_search/
└── service.py

search_platform/
├── models.py
└── service.py

```

Validation:

```text
Engine Catalog consumed
Carrier Catalog integrated with CarrierAccount
Engine Search consumed
Organisation Search implemented
MultiCarrierSearchService implemented
No SaaS carrier catalog persistence
No Engine modification
```

---

# TARGET DOMAIN RELATIONSHIP MODEL

Engine and search relationship:

```text
Universal PUDO Engine
│
├── Carrier Catalog
│
├── Provider Implementations
│
└── Pickup Point Search
        ▲
        │
EngineSearchService
        ▲
        │
CarrierCatalogService
        ▲
        │
OrganisationSearchService
        ▲
        │
MultiCarrierSearchService
        ▲
        │
Search Platform
```

Organisation relationship:

```text
Organisation
│
├── Membership
│       │
│       ▼
│      User
│
├── CarrierAccount
│       │
│       ▼
│      CarrierCredential
│
├── Future DashboardConfiguration
│
├── Future ApiCredential
│
└── Future Search Platform
```

---

# BACKEND ARCHITECTURE

Technology:

```text
FastAPI
Python 3.14
```

Status:

```text
Validated
```

Current structure:

````text
src/universal_pudo_saas/
├── auth/
│   ├── __init__.py
│   ├── routes.py
│   ├── schemas.py
│   └── service.py
├── carrier_accounts/
│   ├── models.py
│   ├── repository.py
│   ├── router.py
│   ├── schemas.py
│   └── service.py
├── carrier_catalog/
│   └── service.py
├── carrier_credentials/
│   ├── models.py
│   ├── repository.py
│   ├── router.py
│   ├── schemas.py
│   └── service.py
├── core/
├── database/
│   ├── base.py
│   ├── metadata.py
│   └── session.py
├── engine_catalog/
│   ├── __init__.py
│   ├── client.py
│   ├── models.py
│   └── service.py
├── engine_search/
│   ├── __init__.py
│   ├── client.py
│   ├── models.py
│   └── service.py
├── memberships/
│   └── models.py
├── multi_carrier_search/
│   └── service.py
├── organisation_search/
│   └── service.py
├── organisations/
│   └── models.py
├── security/
│   ├── passwords.py
│   └── tokens.py
├── shared/
│   └── entities.py
├── users/
│   ├── models.py
│   └── repository.py
├── search_platform/
│   ├── models.py
│   └── __init__.py
│   └── service.py
├── map_service/
│   ├── __init__.py
│   ├── models.py
│   └── service.py
└── main.py

Implemented structure:
search_platform/
├── __init__.py
├── models.py
└── service.py


Planned structure:

exports/
administration/
frontend/
public_api/


No planned SaaS `carrier_integrations/` module exists under the current Engine-owned carrier catalog strategy.

---

# DATABASE ARCHITECTURE

Technology:

```text
PostgreSQL 17
SQLAlchemy
Alembic
````

Status:

```text
Validated
```

Database:

```text
universal_pudo_saas
```

Current tables:

```text
alembic_version
organisations
users
memberships
carrier_accounts
carrier_credentials
```

No SaaS carrier catalog table exists.

No SaaS carrier integration table exists.

No search persistence table exists for Phase 16.

Future possible tables:

```text
dashboard_configurations
api_credentials
future_search_history
future_exports
future_audit_events
future_observability_events
future_usage_metrics
```

---

# DATABASE OWNERSHIP

## universal_pudo_saas

Owner:

```text
Universal PUDO SaaS
```

Responsibilities:

- identities
- organisations
- memberships
- tenant access
- carrier accounts
- carrier credentials
- future dashboard configuration
- future API credentials
- future search history
- future administration data

---

## universal_pudo

Owner:

```text
Universal PUDO Engine
```

Responsibilities:

- carrier provider implementations
- carrier catalog implementation
- carrier metadata
- carrier lifecycle
- carrier capabilities
- PUDO search execution
- pickup point normalization
- provider-specific carrier logic

---

# TEST ARCHITECTURE

Current validated test coverage includes:

```text
authentication tests
settings tests
entity tests
organisation tests
user tests
membership tests
persistence tests
carrier account tests
carrier credential tests
carrier catalog tests
engine catalog tests
engine search tests
organisation search tests
multi-carrier search tests
search platform model tests
search platform service tests

```

Current latest known result:

```text
166 passed
0 failed
```

Known warning:

```text
StarletteDeprecationWarning
```

---

# TESTING STRATEGY

## Level 1

Model Tests

Status:

```text
Implemented
```

---

## Level 2

Persistence Tests

Status:

```text
Implemented
```

Validated:

```text
session.add()
session.commit()
session.refresh()
session.get()
session.delete()
```

---

## Level 3

Service Tests

Status:

```text
Implemented
```

---

## Level 4

API Tests

Status:

```text
Implemented for current carrier and auth APIs
```

---

## Level 5

Permission Tests

Status:

```text
Planned
```

---

## Level 6

Integration Tests

Status:

```text
Planned
```

---

# PERSISTENCE ARCHITECTURE

Validated operations:

```text
session.add()
session.commit()
session.refresh()
session.get()
session.delete()
```

Validated persistence layers:

```text
Organisation Persistence
User Persistence
Membership Persistence
CarrierAccount Persistence
CarrierCredential Persistence
CarrierAccount Repository
CarrierCredential Repository
```

Validated database operations:

```text
PostgreSQL Write
PostgreSQL Read
Entity Retrieval
Entity Deletion
Foreign Key Persistence
```

Search Platform persistence is deferred.

---

# SECURITY ARCHITECTURE

Validated dependencies:

```text
passlib 1.7.4
bcrypt 4.3.0
python-jose
cryptography
```

Implemented:

```text
Password Hashing Service
hash_password()
verify_password()
JWT Service
create_access_token()
decode_access_token()
Authentication Service
authenticate_user()
create_user_token()
Authentication API
POST /auth/login
GET /auth/me
JWT Authentication Flow
User Lookup Foundation
Repository-Based Authentication
```

Not yet implemented:

```text
Role Enforcement
Permission Enforcement
Refresh Tokens
Password Reset
Email Verification
Credential Encryption Hardening
```

---

# AUTHENTICATION ARCHITECTURE

```text
security/
├── passwords.py
└── tokens.py

auth/
├── __init__.py
├── schemas.py
├── routes.py
└── service.py

users/
└── repository.py
```

Endpoints:

```text
POST /auth/login
GET /auth/me
```

Flow:

```text
Login Request
        ↓
Repository Lookup
        ↓
authenticate_user()
        ↓
create_user_token()
        ↓
JWT
        ↓
GET /auth/me
        ↓
decode_access_token()
        ↓
CurrentUserResponse
```

---

# ACCESS CONTROL ARCHITECTURE

Current status:

```text
Documented
Partially implemented
```

Implemented in code:

```text
users.is_platform_admin
memberships.role strategy
```

Permission enforcement remains planned.

Validated documents:

```text
product-vision.md
access-model.md
permission-matrix.md
carrier-integration-model.md
role-strategy.md
```

---

# CARRIER ARCHITECTURE

The active carrier architecture separates:

```text
Engine Carrier Catalog
CarrierAccount
CarrierCredential
```

The SaaS does not own CarrierIntegration as an active persisted entity.

---

## Engine Carrier Catalog

Scope:

```text
Universal PUDO Engine
```

Owner:

```text
Universal PUDO Engine
```

Status in SaaS:

```text
Consumed
Not Persisted
```

SaaS consumption:

```text
engine_catalog/models.py
engine_catalog/client.py
engine_catalog/service.py
```

---

## CarrierAccount

Status:

```text
Implemented
Persisted
Persistence Validated
```

Purpose:

```text
Organisation-specific carrier configuration.
```

Reference:

```text
carrier_code
```

Boundary:

```text
Carrier catalog remains owned by Universal PUDO Engine.
```

---

## CarrierCredential

Status:

```text
Implemented
Persisted
Persistence Validated
```

Purpose:

```text
Stores carrier authentication values attached to a CarrierAccount.
```

Security boundary:

```text
Encryption hardening remains future work.
```

---

# SEARCH ARCHITECTURE

Search is a primary platform capability.

The goal is to expose an organisation-facing search capability without duplicating Engine search responsibilities.

Validated Phase 15 chain:

```text
MultiCarrierSearchService
        ↓
OrganisationSearchService
        ↓
CarrierCatalogService
        ↓
EngineSearchService
        ↓
Universal PUDO Engine
```

Validated Phase 16 chain:

```text
SearchPlatformService
        ↓
SearchExecutionMetadata
        ↓
SearchResult
        ↓
MultiCarrierSearchService
        ↓
OrganisationSearchService
        ↓
CarrierCatalogService
        ↓
EngineSearchService
        ↓
Universal PUDO Engine
```

Phase 16 is non-persistent.

Search persistence is deferred.

---

# PHASE 16 SEARCH PLATFORM ARCHITECTURE

Phase 16 introduces the Search Platform foundation.

Sub-phases:

```text
16.1 Search Domain Design
16.2 Search Platform Models Foundation
16.3 Search Platform Service Foundation
16.4 Search Result Enrichment Foundation
16.5 Search Platform Validation
16.6 Search Platform Closure
```

Phase 16 may introduce:

```text
SearchRequest
SearchResult
SearchExecutionMetadata
SearchPlatformService
```

Phase 16 must not introduce:

```text
Search SQLAlchemy model
SearchResult table
SearchHistory table
Alembic migration
Search persistence
Search retention policy
```

---

# ROADMAP ALIGNMENT

Completed:

```text
Documentation Foundation
Repository Foundation
Architecture Foundation
ADR Foundation
Domain Model Design
Database Model Design
Persistence Decisions
Backend Foundation
Database Configuration Foundation
Alembic Foundation
Organisation Foundation
Users Foundation
Membership Foundation
Authentication Model Foundation
Password Hashing Foundation
JWT Foundation
Authentication Service Foundation
Authentication API Foundation
Persistence Test Foundation
Tenant Access Foundation
Role Persistence Foundation
Carrier Account Management
Carrier Account SQLAlchemy Foundation
Carrier Credential Foundation
Carrier Account Repository Foundation
Carrier Credential Repository Foundation
Carrier Account Service Foundation
Carrier Credential Service Foundation
Carrier Account API Foundation
Carrier Credential API Foundation
Engine Catalog Foundation
Carrier Catalog Integration Service
Engine Search Foundation
Organisation Search Foundation
Multi-Carrier Execution Foundation
Universal PUDO Engine Integration Closure
16.1 Search Domain Design
16.2 Search Platform Models Foundation
16.3 Search Platform Service Foundation
16.4 Search Result Enrichment Foundation
16.5 Search Platform Validation
16.6 Search Platform Closure
17.1 Map Domain Design
17.2 Map Models Foundation
17.3 Map Service Foundation
17.4 Leaflet Integration Planning Freeze
17.5 Leaflet Component Foundation
17.6 Map Experience Validation
17.7 Map Experience Closure

```

Current:

Phase 17.7

Status :
Closure In Progress

Future:

18 Frontend MVP
19 Administration Portal
20 Public API
21 Observability And Audit
22 Export Platform
23 Security Hardening
24 Core Upgrade Strategy
25 Release Preparation
26 Universal PUDO SaaS v1.0.0

````

---

# CURRENT STATE

Architecture Status:

```text
Stable after Phase 15
````

Database Status:

```text
Stable
```

Authentication Status:

```text
Completed
```

Persistence Status:

```text
Completed for current entities
```

Access Model Status:

```text
Documented
Partially implemented
```

Role Storage Strategy:

```text
Approved
```

Engine Integration Status:

```text
Completed
```

Search Platform Status:
Phase 16 Completed

✅ SearchRequest
✅ SearchResult
✅ SearchPlatformService

Phase 17.6
Validation Completed

Testing Status:
166 passed
0 failed

Documentation Status:

```text
Realigned through Phase 17.7
```

---

# NEXT ARCHITECTURAL MILESTONE

Phase 18 Frontend MVP

Objectives:

- create frontend application foundation
- create authentication-aware frontend shell
- consume Search Platform through existing backend boundaries
- consume MapProjectionResult through existing map boundaries
- validate first user-facing product experience
- preserve backend responsibilities
- avoid Engine modifications

Success Criteria:

- frontend foundation defined
- app shell defined
- authentication-aware navigation defined
- pickup point search UI prepared
- map view consumption prepared
- SearchResult boundary preserved
- MapService boundary preserved
- MapProjectionResult boundary preserved
- no database change introduced
- no Engine modification introduced

---

# ARCHITECTURAL DECISIONS

## AD-001

SaaS Administrator storage

Decision:

```text
users.is_platform_admin
```

Reason:

SaaS Administrator is platform-scoped and not organisation-scoped.

---

## AD-002

Owner and Viewer storage

Decision:

```text
memberships.role
```

Reason:

Owner and Viewer roles are organisation-specific.

---

## AD-003

No dynamic RBAC for V1

Decision:

```text
No role table, permission table, or role-permission table for V1.
```

Reason:

The platform currently supports fixed business roles.

---

## AD-004

Engine-owned carrier catalog

Decision:

```text
Universal PUDO Engine owns carrier catalog.
Universal PUDO SaaS does not persist carrier definitions.
```

Reason:

The Engine is the single source of truth for carrier functionality.

---

## AD-005

PUDO scope guardrail

Decision:

```text
The SaaS only models carrier concepts required for PUDO access and consumption.
```

Reason:

Avoid drifting toward a generic shipping, OMS, WMS, TMS, or carrier capability platform.

---

## AD-006

Phase 16 non-persistent search foundation

Decision:

```text
Phase 16 introduces Search Platform models and services without SQL persistence.
```

Reason:

Search persistence must be decided after the Search Platform domain contract is stable.

---

# ROADMAP REPRIORITIZATION

## ADR-0010 - Frontend Before Export Platform

Decision:

Frontend MVP is prioritized before Export Platform.

Export Platform is deferred to Phase 22.

Reason:

Frontend MVP provides immediate user-facing value.

Export Platform does not yet have a validated business use case.

Export Platform becomes more relevant after Observability And Audit.

Updated sequence:

- Phase 18 Frontend MVP
- Phase 19 Administration Portal
- Phase 20 Public API
- Phase 21 Observability And Audit
- Phase 22 Export Platform
- Phase 23 Security Hardening

Architectural Impact:

No backend boundary changes.

No Engine boundary changes.

No SearchResult change.

No MapProjectionResult change.

Export remains a SaaS-owned future capability.

# CHANGE HISTORY

2026-07-25

Authentication API Foundation completed.

Implemented:

```text
POST /auth/login
GET /auth/me
JWT Authentication Flow
User Lookup Foundation
Repository-Based Authentication
```

Result:

```text
42 automated tests passing.
```

---

2026-07-25

Persistence Test Foundation completed.

Implemented:

```text
test_organisation_persistence.py
test_user_persistence.py
test_membership_persistence.py
```

Validated:

```text
session.add()
session.commit()
session.refresh()
session.get()
session.delete()
PostgreSQL reads
PostgreSQL writes
Foreign key persistence
```

Result:

```text
52 automated tests passing.
```

---

2026-07-25

Carrier Account Persistence Foundation completed.

Implemented:

```text
carrier_accounts/models.py
carrier_credentials/models.py
carrier_accounts table
carrier_credentials table
Carrier Account persistence tests
Carrier Credential persistence tests
```

Validated:

```text
carrier_code strategy
Engine-owned Carrier Catalog
SaaS-owned Carrier Accounts
SaaS-owned Carrier Credentials
```

Result:

```text
73 automated tests passing.
```

---

2026-07-25

Carrier Account Repository Foundation completed.

Implemented:

```text
carrier_accounts/repository.py
test_carrier_account_repository.py
```

Validated:

```text
get_carrier_account()
list_carrier_accounts_by_organisation()
```

Result:

```text
75 passed
0 failed
```

---

2026-07-25

Carrier Credential Repository Foundation completed.

Implemented:

```text
carrier_credentials/repository.py
test_carrier_credential_repository.py
```

Validated:

```text
get_carrier_credential()
list_credentials_by_carrier_account()
```

Result:

```text
77 passed
0 failed
```

---

2026-07-27

Architecture updated after Universal PUDO Engine Integration.

Updated decisions:

- Universal PUDO Engine owns carrier catalog
- Universal PUDO SaaS does not persist carrier definitions
- CarrierIntegration is no longer an active SaaS persistence model
- Phase 15 Engine integration chain documented
- Search Platform Phase 16 structure documented
- Search persistence deferred

Current validated result:

```text
166 passed
0 failed
```

---

---

2026-07-27

Search Platform Models Foundation completed.

Implemented:

search_platform/models.py

SearchRequest

SearchResult

test_search_platform_models.py

Validated:

DTO boundary

Request abstraction

Result abstraction

No persistence

No migration

No database impact

Result:

142 passed
0 failed

---

2026-07-28

Search Platform Service Foundation completed.

Implemented:

search_platform/service.py
SearchPlatformService
test_search_platform_service.py

Validated:

SearchRequest consumption
MultiCarrierSearchService delegation
SearchResult generation
No persistence
No migration
No database impact
No Universal PUDO Engine modification

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

Result:
Architecture validated.

Next milestone:
Phase 17.7 Map Experience Closure
