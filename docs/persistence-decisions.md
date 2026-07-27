# Universal PUDO SaaS - Persistence Decisions

Version: 0.2.0

Status: Updated After Universal PUDO Engine Integration

Last Updated: 2026-07-27

---

# PURPOSE

This document captures persistence decisions that affect the Universal PUDO SaaS data model.

Its purpose is to avoid making structural persistence decisions directly in implementation.

These decisions apply across current and future SaaS-owned entities.

Universal PUDO Engine has its own database and persistence lifecycle.

---

# SOURCE OF TRUTH

Persistence decisions must remain aligned with:

1. Source code
2. Tests
3. Database schema
4. Approved ADRs
5. Architecture documents
6. Roadmap
7. Project documentation

When conflicts exist, source code and database schema win.

---

# CURRENT DATABASES

## Universal PUDO SaaS

Database:

```text
universal_pudo_saas
```

Owner:

```text
Universal PUDO SaaS
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

---

## Universal PUDO Engine

Database:

```text
universal_pudo
```

Owner:

```text
Universal PUDO Engine
```

Universal PUDO SaaS does not own this database.

---

# DECISION 001

Identifier Strategy

Status:

Accepted

---

## Decision

Use UUID identifiers for all SaaS business entities.

Examples:

```text
Organisation
User
Membership
CarrierAccount
CarrierCredential
Future Search
Future Export
Future AuditEvent
```

---

## Reasoning

UUID identifiers support:

```text
Globally unique identifiers
Distributed-system compatibility
Self-hosted compatibility
API compatibility
Reduced predictability compared to sequential identifiers
```

---

## Consequences

All primary SaaS-owned entities should use:

```text
UUID
```

as their business identifier.

---

# DECISION 002

Base Entity Strategy

Status:

Accepted

---

## Decision

Persisted business entities inherit or align with a common base entity strategy.

Current common attributes:

```text
id
created_at
updated_at
```

---

## Goal

Provide consistency across the data model.

---

# DECISION 003

Timestamp Strategy

Status:

Accepted

---

## Decision

Persisted entities should contain:

```text
created_at
updated_at
```

---

## Reasoning

Timestamps support:

```text
Auditing
Diagnostics
Debugging
Operational tracking
```

---

## Future Possibility

Additional timestamps may be introduced when required:

```text
deleted_at
last_accessed_at
last_validated_at
last_executed_at
```

---

# DECISION 004

Soft Delete Strategy

Status:

Accepted

---

## Decision

Business entities should support soft delete where operationally required.

---

## Applicability

Potential examples:

```text
Organisation
CarrierAccount
Future Search History
Future Export
```

---

## Implementation Principle

Entities should be marked inactive rather than physically removed when business recovery or auditability is required.

Future common attribute:

```text
deleted_at
```

---

## Current Status

Soft delete strategy is accepted as a long-term persistence direction.

Not every current entity has implemented a dedicated soft delete field yet.

---

# DECISION 005

Audit Strategy

Status:

Accepted

---

## Decision

A centralized audit model should be introduced in a future phase.

---

## Future Entity

```text
AuditEvent
```

---

## Examples

```text
User Login
Password Reset
Credential Update
Carrier Account Change
Search Execution
Export Creation
```

---

## Current Status

Deferred.

No current audit table has been implemented.

---

# DECISION 006

Organisation Settings

Status:

Accepted

---

## Decision

Organisation-specific settings are supported in the target architecture.

---

## Future Entity

```text
OrganisationSettings
```

---

## Examples

```text
Language
Timezone
Default Export Options
Future Preferences
```

---

## Ownership

```text
Organisation
    1
    │
    ▼
OrganisationSettings
    1
```

---

## Current Status

Deferred.

No organisation settings table has been implemented.

---

# DECISION 007

Role Ownership Strategy

Status:

Accepted

---

## Decision

Organisation-scoped roles belong to Membership.

They do not belong directly to User.

---

## Example

```text
User A
 ├── Organisation X
 │      └── OWNER
 │
 └── Organisation Y
        └── VIEWER
```

---

## Implemented Strategy

```text
SAAS_ADMIN -> users.is_platform_admin
OWNER      -> memberships.role
VIEWER     -> memberships.role
```

---

## Current Status

Implemented.

---

# DECISION 008

Search Result Persistence

Status:

Deferred

---

## Previous Decision

The previous persistence design stated:

```text
Search Results are persisted.
```

and:

```text
SearchResult becomes a persistent business entity.
```

---

## Updated Decision

Search result persistence is deferred until after Search Platform Foundation.

Phase 16 introduces Search Platform business models and service boundaries only.

Phase 16 does not introduce:

```text
Search persistence
Search history table
SearchResult SQLAlchemy model
Alembic migration
Search retention policy
```

---

## Reason

The project must first establish the Search Platform domain contract before deciding persistence.

Current confirmed phases:

```text
Phase 16.1 Search Domain Design
Phase 16.2 Search Platform Models Foundation
Phase 16.3 Search Platform Service Foundation
Phase 16.4 Search Result Enrichment Foundation
Phase 16.5 Search Platform Validation
Phase 16.6 Search Platform Closure
```

Persistence is intentionally out of scope for Phase 16.

---

## Future Decision Required

A future phase must decide whether to persist:

```text
SearchRequest
SearchResult
SearchHistory
SearchExecution
```

Future decision must define:

```text
Retention duration
Storage format
Tenant ownership
Audit requirements
Export dependency
Analytics dependency
Privacy constraints
```

---

# DECISION 009

Credential Persistence Model

Status:

Accepted

---

## Decision

Carrier credentials remain:

```text
Tenant-owned
CarrierAccount-owned
Sensitive
```

---

## Current Model

Implemented entity:

```text
CarrierCredential
```

Relationship:

```text
CarrierAccount
    1
    │
    ▼
CarrierCredential
    N
```

---

## Constraint

Plain text credential storage is not acceptable for production.

Credential encryption remains a required future hardening topic.

---

## Current Status

Persistence implemented.

Encryption hardening deferred.

---

# DECISION 010

Tenant Ownership Rule

Status:

Accepted

---

## Decision

Every tenant-owned entity must reference an Organisation directly or indirectly.

Examples:

```text
Membership
CarrierAccount
CarrierCredential
Future Search
Future Export
Future OrganisationSettings
```

---

## Current Implementation

Direct organisation ownership:

```text
CarrierAccount.organisation_id
Membership.organisation_id
```

Indirect organisation ownership:

```text
CarrierCredential
    -> CarrierAccount
    -> Organisation
```

---

## Goal

Guarantee tenant isolation.

---

# DECISION 011

Carrier Catalog Persistence

Status:

Accepted

---

## Decision

Universal PUDO SaaS does not persist carrier definitions.

Universal PUDO Engine owns the carrier catalog.

Universal PUDO SaaS references carriers through:

```text
carrier_code
```

---

## Current Implementation

Implemented entity:

```text
CarrierAccount
```

Implemented field:

```text
carrier_code
```

Mapping:

```text
CarrierAccount.carrier_code
        ↓
Engine Carrier.code
```

---

## Consequences

The SaaS must not introduce:

```text
CarrierIntegration table
CarrierDefinition table
CarrierCatalog table
CarrierCapability table
```

unless a future ADR explicitly changes the ownership model.

---

# DECISION 012

Search Platform Persistence Boundary

Status:

Accepted

---

## Decision

Phase 16 Search Platform is a non-persistent domain foundation.

---

## Phase 16 May Introduce

```text
SearchRequest
SearchResult
SearchPlatformService
```

as business models or DTOs.

---

## Phase 16 Must Not Introduce

```text
Search SQLAlchemy model
SearchResult table
SearchHistory table
Alembic migration
Retention policy
```

---

## Reason

Search persistence must be designed separately from Search Platform execution.

Search Platform should first define:

```text
What is searched
How a search request is represented
How a search result is returned
How the Search Platform consumes MultiCarrierSearchService
```

Persistence can be decided after the domain boundary is stable.

---

# ENTITY CLASSIFICATION

## Global Entities

Implemented:

```text
User
```

Future:

```text
Future PlatformSettings
Future AuditEvent
```

---

## Tenant-Owned Entities

Implemented:

```text
Organisation
Membership
CarrierAccount
CarrierCredential
```

Future:

```text
Future Search
Future SearchRequest
Future SearchResult
Future Export
Future ExportFile
Future OrganisationSettings
```

---

## Engine-Owned Entities

Owned by Universal PUDO Engine:

```text
Carrier
CarrierCapability
CarrierLifecycle
PickupPoint normalization
Provider execution
Carrier metadata
Carrier catalog implementation
```

Universal PUDO SaaS may consume SaaS-side projections of these concepts, but it does not persist Engine-owned definitions.

---

# CURRENT IMPLEMENTED TABLES

```text
alembic_version
organisations
users
memberships
carrier_accounts
carrier_credentials
```

---

# CURRENT NON-PERSISTENT FOUNDATIONS

Implemented without database persistence:

```text
Engine Catalog Foundation
Carrier Catalog Integration Service
Engine Search Foundation
Organisation Search Foundation
Multi-Carrier Execution Foundation
```

No tables were introduced for these foundations.

---

# FUTURE DECISIONS

## Search Persistence

Status:

Deferred

Questions:

```text
Should SearchResult be persisted?
Should SearchRequest be persisted?
Should SearchHistory be persisted?
How long should searches remain available?
Should exports depend on persisted search results?
```

---

## Export Persistence

Status:

Deferred

Questions:

```text
How long should ExportFiles remain available?
Should generated files be stored?
Should exports reference SearchResults?
```

---

## Audit Retention

Status:

Deferred

Questions:

```text
How long should AuditEvents remain stored?
Which actions require audit?
```

---

## API Key Strategy

Status:

Deferred

Questions:

```text
How should public API credentials be stored?
How should API keys be rotated?
How should organisation-level API access be scoped?
```

---

# NEXT STEP

Current next persistence-related action:

```text
No persistence action required for Phase 16.
```

Phase 16 Search Platform must remain non-persistent.

Future persistence decisions should be revisited after Search Platform Foundation is complete.

---

# CHANGE HISTORY

2026-07-22

Initial persistence decisions created.

---

2026-07-27

Persistence decisions updated after Universal PUDO Engine Integration.

Updated decisions:

- Search Result Persistence deferred
- Carrier Catalog Persistence clarified
- Search Platform Persistence Boundary added
- Engine-owned entities separated from SaaS-owned entities
- Phase 16 confirmed as non-persistent Search Platform Foundation
