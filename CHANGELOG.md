# Changelog

All notable changes to this project will be documented in this file.

The format follows a milestone-based approach.

---

## [2.5.0] - 2026-08-02

### Phase 17.5 - Leaflet Component Foundation

Validated:

- frontend Leaflet foundation
- MapProjectionResult presentation contract
- marker rendering strategy
- popup rendering strategy
- selection lifecycle
- empty state strategy

Next milestone:
Phase 17.6 Map Experience Validation

#### [2.4.0] - 2026-07-30

##### Phase 17.4 - Leaflet Integration Foundation

Added:

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

Validation:

- Leaflet consumes MapProjectionResult
- Leaflet does not consume SearchResult directly
- Leaflet does not consume Universal PUDO Engine directly
- No persistence introduced
- No SQLAlchemy model introduced
- No Alembic migration introduced
- No Universal PUDO Engine modification introduced
- No frontend implementation introduced

Status:
Phase 17.4 Planning Freeze completed

Next milestone:
Phase 17.5 Leaflet Component Foundation

---

### [2.3.0] - 2026-07-30

#### Phase 17.3 - Map Service Foundation

Added:

- src/universal_pudo_saas/map_service/**init**.py
- src/universal_pudo_saas/map_service/models.py
- src/universal_pudo_saas/map_service/service.py
- tests/test_map_models.py
- tests/test_map_service.py

Implemented:

- MapService
- MapProjectionResult
- MapMarker projection
- MapPopup projection
- Carrier visibility filtering
- Pickup point selection validation
- Branding projection support

Validation:

- SearchResult remains unchanged
- No persistence introduced
- No SQLAlchemy model introduced
- No Alembic migration introduced
- No Universal PUDO Engine modification introduced

Result:
166 passed
0 failed

Status:
Map Service Foundation completed

Next milestone:
Phase 17.4 Leaflet Integration Foundation

---

## [2.2.0] - 2026-07-30

### Phase 17.2 - Map Models Foundation

Added:

- docs/map-models-foundation.md

Implemented:

- Map state model
- Marker projection model
- Popup projection model
- Carrier visibility model
- Pickup point selection model
- SearchResult reset strategy
- Analytics boundary

Validation:

- SearchResult remains the unique business contract
- No MapSearchResult introduced
- No MapPickupPoint introduced
- No persistence introduced
- No SQLAlchemy model introduced
- No Alembic migration introduced
- No Universal PUDO Engine modification introduced

Architecture:

- Map Experience remains a presentation layer
- Marker projections are derived from SearchResult
- Popup projections are derived from SearchResult
- Carrier visibility is separated from carrier availability
- Selection lifecycle documented
- Analytics boundary documented without persistence

Status:
Map Models Foundation completed.

Next milestone:
Phase 17.3 Map Service Foundation.

---

## [2.1.0] - 2026-07-28

## Phase 16.5 - Search Platform Validation

Validated:

- SearchRequest lifecycle
- SearchResult lifecycle
- SearchExecutionMetadata
- SearchPlatformService
- Search Platform boundaries
- MultiCarrierSearchService integration

Validation:

150 passed
0 failed

Architecture:

Search Platform contract validated.

No persistence introduced.

No SQLAlchemy model introduced.

No Alembic migration introduced.

No Universal PUDO Engine modification introduced.

Status:

Search Platform Validation completed.

Next milestone:

Phase 16.6 Search Platform Closure.

---

## [2.0.0] - 2026-07-28

## Phase 16.4 - Search Result Enrichment Foundation

Added:

- SearchExecutionMetadata

Implemented:

- SearchResult enrichment
- duration tracking
- applied filter tracking
- execution metadata support

Validation:

150 passed
0 failed

Architecture:

SearchResult now carries execution metadata.

No persistence introduced.

No migration introduced.

No Universal PUDO Engine modification introduced.

Status:

Search Result Enrichment Foundation completed.

Next milestone:

Phase 16.5 Search Platform Validation.

## [1.9.0] - 2026-07-28

## Phase 16.3 - Search Platform Service Foundation

Added:

- src/universal_pudo_saas/search_platform/service.py
- tests/test_search_platform_service.py

Implemented:

- SearchPlatformService
- SearchRequest consumption
- SearchResult generation
- MultiCarrierSearchService delegation

Validation:

145 passed
0 failed

Architecture:

SearchPlatformService is now the SaaS-owned Search Platform service boundary.

The service delegates search execution to MultiCarrierSearchService.

No persistence introduced.

No SQLAlchemy model introduced.

No Alembic migration introduced.

No Universal PUDO Engine modification introduced.

Status:

Search Platform Service Foundation completed.

Next milestone:

Phase 16.4 Search Result Enrichment Foundation.

---

## [1.8.0] - 2026-07-27

## Phase 16.2 - Search Platform Models Foundation

Added:

- src/universal_pudo_saas/search_platform/models.py
- tests/test_search_platform_models.py

Implemented:

- SearchRequest
- SearchResult

Validation:

142 passed
0 failed

Architecture:

Introduced the Search Platform domain models.

SearchRequest now represents the SaaS search contract.

SearchResult now represents the SaaS search response contract.

No persistence introduced.

No SQLAlchemy model introduced.

No Alembic migration introduced.

No Universal PUDO Engine modification introduced.

Status:

Search Platform Models Foundation completed.

Next milestone:

Phase 16.3 Search Platform Service Foundation.

## Phase 15.5 - Multi-Carrier Execution Foundation

Added:

- multi_carrier_search/service.py
- test_multi_carrier_search_service.py

Implemented:

- MultiCarrierSearchService
- OrganisationSearchService integration
- Dedicated SaaS search orchestration boundary

Validation:

136 passed
0 failed

## Phase 15.4 - Organisation Search Foundation

Added:

- organisation_search/service.py
- test_organisation_search_service.py

Implemented:

- organisation-based pickup point search
- carrier filtering based on organisation activation
- PickupPoint aggregation across organisation carriers

Validation:

133 passed
0 failed

### Documentation

Phase 15 roadmap finalized.

Updated:

- Phase 15.4 Organisation Search Foundation
- Phase 15.5 Multi-Carrier Execution Foundation
- Phase 15.6 Universal PUDO Engine Integration Closure

Decision:

The primary SaaS use case is organisation-based pickup point search using activated carriers.

The SaaS owns orchestration.

Universal PUDO Engine owns carrier integrations.

### Added

Engine Search Foundation.

Created:

- src/universal_pudo_saas/engine_search/**init**.py
- src/universal_pudo_saas/engine_search/models.py
- src/universal_pudo_saas/engine_search/client.py
- src/universal_pudo_saas/engine_search/service.py
- tests/test_engine_search_models.py
- tests/test_engine_search_client.py
- tests/test_engine_search_service.py

### Validation

Validated:

- PickupPoint SaaS read model
- Address SaaS projection
- GeoLocation SaaS projection
- PickupType SaaS enum
- EngineSearchClient
- InMemoryEngineSearchClient
- EngineSearchService
- search_pickup_points()
- search_pickup_points_by_radius()
- get_pickup_point()
- list_carrier_pickup_points()

Result:
130 passed
0 failed

### Architecture

Universal PUDO SaaS now has a read-only Engine Search Foundation for consuming pickup point search capabilities exposed by Universal PUDO Engine.

No search persistence was introduced.

No SQLAlchemy model was introduced.

No Alembic migration was introduced.

No Universal PUDO Engine modification was introduced.

### Status

Engine Search Foundation completed.

## [1.7.0-draft] - 2026-07-26

### Added

Carrier Catalog Integration Service.

Created:

- src/universal_pudo_saas/carrier_catalog/**init**.py
- src/universal_pudo_saas/carrier_catalog/service.py
- tests/test_carrier_catalog_service.py

### Validation

Validated:

- list_available_carriers()
- list_organisation_carriers()
- list_activatable_carriers_for_organisation()
- Carrier.code to CarrierAccount.carrier_code mapping
- Engine Catalog to CarrierAccount crossing

Result:
118 passed
0 failed

### Architecture

The SaaS can now derive organisation-specific carrier catalogue views by crossing Engine carrier metadata with SaaS CarrierAccount records.

No carrier catalog is persisted by the SaaS.

No Engine modification was introduced.

No Alembic migration was introduced.

### Status

Carrier Catalog Integration Service completed.

---

## [1.6.0-draft] - 2026-07-26

### Added

Engine Catalog Foundation

Created:

- src/universal_pudo_saas/engine_catalog/**init**.py
- src/universal_pudo_saas/engine_catalog/models.py
- src/universal_pudo_saas/engine_catalog/client.py
- src/universal_pudo_saas/engine_catalog/service.py

- tests/test_engine_catalog_models.py
- tests/test_engine_catalog_client.py
- tests/test_engine_catalog_service.py

### Validation

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

### Architecture

Universal PUDO SaaS now consumes Engine carrier metadata through dedicated DTOs and services without persisting the carrier catalog.

### Status

Engine Catalog Foundation completed.

Next milestone:

Carrier Catalog Integration Service.

---

2026-07-26

Carrier Account API Foundation completed.

Implemented:

- carrier_accounts/router.py
- carrier_credentials/router.py
- test_carrier_account_api.py
- test_carrier_credential_api.py

Validated:

- GET carrier account
- GET carrier accounts by organisation
- GET carrier credential
- GET credentials by carrier account

Result:
93 passed
0 failed

---

# [1.3.0-draft] - 2026-07-25

## Added

Carrier Account Persistence Foundation.

Created:

- src/universal_pudo_saas/carrier_accounts/models.py
- src/universal_pudo_saas/carrier_credentials/models.py
- tests/test_carrier_account.py
- tests/test_carrier_account_persistence.py
- tests/test_carrier_credential.py
- tests/test_carrier_credential_persistence.py

## Database

Added migrations:

- 3fb1f82a4474_create_carrier_accounts_table
- 2bc5746479e6_create_carrier_credentials_table

Created tables:

- carrier_accounts
- carrier_credentials

## Architecture

Validated Option B:

- Universal PUDO Engine owns the carrier catalog
- Universal PUDO SaaS does not persist carrier definitions
- Universal PUDO SaaS references carriers through carrier_code
- Universal PUDO SaaS owns Carrier Accounts
- Universal PUDO SaaS owns Carrier Credentials

## Validation

Result:

73 passed

0 failed

Known warning:

- StarletteDeprecationWarning from FastAPI TestClient dependency chain

## Lessons Learned

SQLAlchemy Python-side defaults should be validated through persistence tests, not object creation tests.

When no cascade strategy is defined, child records must be deleted before parent records in persistence tests.

## Status

Carrier Account Persistence Foundation completed.

Next milestone:

Carrier Account Repository Foundation.

---

# [1.4.0-draft] - 2026-07-25

## Added

Carrier Account Repository Foundation.

Created:

- src/universal_pudo_saas/carrier_accounts/repository.py
- tests/test_carrier_account_repository.py

## Validation

Validated:

- get_carrier_account()
- list_carrier_accounts_by_organisation()

Result:

75 passed

0 failed

## Status

Carrier Account Repository Foundation completed.

Next milestone:

Carrier Credential Repository Foundation.

---

# [1.5.0-draft] - 2026-07-25

## Added

Carrier Credential Repository Foundation.

Created:

- src/universal_pudo_saas/carrier_credentials/repository.py
- tests/test_carrier_credential_repository.py

## Validation

Validated:

- get_carrier_credential()
- list_credentials_by_carrier_account()

Result:

77 passed

0 failed

## Status

Carrier Credential Repository Foundation completed.

Next milestone:

Carrier Account Service Foundation.

---

# [1.2.1-draft] - 2026-07-25

## Added

- users.is_platform_admin
- test_user_platform_admin.py

## Database

- migration 2270054c9c72_add_platform_admin_to_users

## Validation

54 passed
0 failed

## Access Model

- SAAS_ADMIN persistence
- OWNER role alignment
- VIEWER role alignment

---

# [1.2.0-draft] - 2026-07-25

## Added

Persistence Test Foundation

Created:

tests/test_organisation_persistence.py

tests/test_user_persistence.py

tests/test_membership_persistence.py

## Implemented

Organisation Persistence Tests

User Persistence Tests

Membership Persistence Tests

CRUD Persistence Validation

PostgreSQL Persistence Validation

Foreign Key Persistence Validation

## Validation

Validated:

- session.add()
- session.commit()
- session.refresh()
- session.get()
- session.delete()

- PostgreSQL reads
- PostgreSQL writes
- CRUD persistence
- Membership foreign keys

Result:

52 passed

0 failed

## Architecture

Persistence Layer validated.

Validated Flow:

Create Entity

↓

Persist Entity

↓

Refresh Entity

↓

Retrieve Entity

↓

Delete Entity

↓

Validate Persistence

## Lessons Learned

Model tests and persistence tests validate different concerns.

Persistence tests provide significantly higher confidence than model-only tests.

Foreign key validation should be tested through persistence workflows.

## Status

Persistence Test Foundation implemented.

Roles & Permissions selected as next milestone.

Documentation synchronization in progress.

---

# [1.1.0-draft] - 2026-07-25

## Added

Authentication API Foundation

Created:

auth/routes.py

auth/schemas.py

users/repository.py

Implemented:

- POST /auth/login
- GET /auth/me

Authentication Flow:

- authenticate_user()
- create_user_token()
- decode_access_token()

User Lookup Foundation

Repository-Based Authentication

JWT Authentication Flow

Current User Endpoint

## Validation

Validated:

- Authentication API available
- JWT generation
- JWT decoding
- Authentication workflow
- Current user retrieval
- User repository lookup

Result:

42 passed

0 failed

## Architecture

Authentication Layer completed.

Current Authentication Flow:

User Login Request

↓

User Repository Lookup

↓

Password Verification

↓

JWT Creation

↓

JWT Validation

↓

Current User Retrieval

## Status

Authentication API Foundation completed.

Persistence Test Foundation implemented.

Documentation synchronization in progress.

---

# [1.0.0-draft] - 2026-07-25

## Added

Authentication Service Foundation

Created:

auth/service.py

Functions:

- authenticate_user()
- create_user_token()

## Validation

35 tests passing

0 failed

## Status

Authentication API Foundation selected as next milestone.

---

# [0.9.0-draft] - 2026-07-23

## Added

JWT Foundation

Created:

security/tokens.py

Functions:

- create_access_token()
- decode_access_token()

## Validation

30 tests passing

0 failed

## Status

Authentication Service Foundation selected as next milestone.

---

# [0.8.0-draft] - 2026-07-23

## Added

Password Hashing Foundation

Created:

security/passwords.py

Functions:

- hash_password()
- verify_password()

## Validation

bcrypt 4.3.0 validated

passlib 1.7.4 validated

26 tests passing

0 failed

## Lessons Learned

bcrypt 5.0.0 is not compatible with the current stack.

bcrypt 4.3.0 adopted as validated version.

## Status

JWT Foundation selected as next milestone.

---

# [0.7.0-draft] - 2026-07-23

## Added

Authentication Model Foundation

Added authentication fields to User:

- password_hash
- is_active
- is_verified
- last_login_at

Added dependencies:

- passlib
- bcrypt
- python-jose
- cryptography

Created:

backend/alembic/versions/2871e90d88b8_add_authentication_fields_to_users.py

## Implemented

Authentication-ready User model

User authentication state management

Authentication migration workflow

Authentication test expansion

## Validation

Validated:

- Authentication migration generation
- Authentication migration audit
- PostgreSQL upgrade
- Authentication field persistence

Result:

19 passed

0 failed

## Database

Updated table:

users

Added columns:

- password_hash
- is_active
- is_verified
- last_login_at

Migration:

2871e90d88b8_add_authentication_fields_to_users.py

## Lessons Learned

Autogenerated Alembic migrations must always be audited before execution.

Authentication model implementation should precede password services and JWT implementation.

Model-level tests should be completed before moving to service-level development.

## Commit

d4bb589

feat(auth): add authentication model and security foundation

## Status

Authentication Foundation

In Progress

Completed:

✅ Authentication Model

✅ Migration

✅ Tests

Remaining:

⏳ Password Hashing Foundation

⏳ JWT Foundation

⏳ Authentication Service

⏳ Login Endpoint

⏳ Current User Endpoint

## Next Milestone

Password Hashing Foundation

Objectives:

- Create security/passwords.py
- Implement hash_password()
- Implement verify_password()
- Create dedicated password tests

---

# [0.6.0-draft] - 2026-07-23

## Added

Users Foundation

Membership Foundation

Created:

users/models.py

memberships/models.py

User migration

Membership migration

## Implemented

User ORM Model

Membership ORM Model

Organisation ↔ Membership ↔ User relationship

## Validation

Validated:

- User table creation
- Membership table creation
- Foreign keys validation

6 tests passing

0 failed

## Milestone

Users Foundation Completed

Membership Foundation Completed

Next Milestone:

Authentication Foundation

---

# [0.5.0-draft] - 2026-07-23

## Added

Organisation Foundation

Created:

backend/src/universal_pudo_saas/organisations/

backend/src/universal_pudo_saas/organisations/models.py

backend/tests/test_organisation.py

backend/alembic/versions/88198ca0d827_create_organisations_table.py

## Implemented

Organisation ORM Model

First Business Entity

First Business Table

First Business Migration

## Validation

Validated:

- alembic revision --autogenerate
- alembic upgrade head
- PostgreSQL table creation
- Organisation automated test

Result:

4 passed

0 failed

## Lessons Learned

Autogenerated migrations must be audited before execution.

Model imports must be registered in metadata.

## Milestone

Organisation Foundation Completed

Architecture Adjustment:

Users Foundation moved before Membership Foundation.

Reason:

Membership depends on User and Organisation relationships.

---

# [0.4.0-draft] - 2026-07-23

## Added

Alembic Foundation

Created:

backend/alembic/

backend/alembic/env.py

backend/alembic/README

backend/alembic/script.py.mako

backend/alembic/versions/

backend/alembic.ini

## Implemented

Alembic Integration

SQLAlchemy Metadata Integration

Settings Integration

PostgreSQL Connectivity Validation

Dedicated SaaS Database

Migration Infrastructure

## PostgreSQL

Validated:

PostgreSQL 17

Dedicated SaaS Database:

universal_pudo_saas

Dedicated Core Database:

universal_pudo

## Validation

Validated:

- alembic init alembic
- alembic current
- SQLAlchemy Metadata Integration
- PostgreSQL Connectivity
- Database Separation Strategy

## Architectural Decisions Confirmed

Universal PUDO Engine and Universal PUDO SaaS use independent databases.

Validated Structure:

universal_pudo → Universal PUDO Engine

universal_pudo_saas → Universal PUDO SaaS

## Milestone

Alembic Foundation Completed

Next Milestone:

Organisation Foundation

---

# [0.3.0-draft] - 2026-07-22

## Added

Database Configuration Foundation

Created:

backend/.env.example

backend/src/universal_pudo_saas/database/base.py

backend/src/universal_pudo_saas/database/metadata.py

backend/src/universal_pudo_saas/database/session.py

backend/src/universal_pudo_saas/shared/entities.py

backend/tests/test_settings.py

backend/tests/test_entities.py

## Implemented

SQLAlchemy Base

Database Metadata

Database Session

BaseEntity

UUID Strategy

Timestamp Strategy

Soft Delete Strategy

Externalized Database Configuration

## Validation

Result:

3 passed

0 failed

## Milestone

Database Configuration Foundation Completed

Next Milestone:

Alembic Foundation

---

# [0.2.0-draft] - 2026-07-22

## Added

Backend Foundation

Created:

backend/README.md

backend/pyproject.toml

backend/src/universal_pudo_saas/**init**.py

backend/src/universal_pudo_saas/main.py

backend/src/universal_pudo_saas/core/**init**.py

backend/src/universal_pudo_saas/core/settings.py

backend/tests/**init**.py

backend/tests/test_main.py

## Validation

Result:

1 passed

0 failed

## Milestone

Backend Foundation Completed

---

# [0.1.0-draft] - 2026-07-22

## Added

Documentation Foundation

README.md

CHANGELOG.md

docs/project-memory.md

docs/product-vision.md

docs/architecture.md

docs/roadmap.md

docs/project-status.md

## Repository

Git Initialized

GitHub Repository Created

Remote Configured

Main Branch Created

Initial Commit Completed

First Push Completed

## Milestones

Documentation Foundation Completed

Repository Foundation Completed
