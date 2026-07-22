# Universal PUDO SaaS - Database Model

Version: 0.1.0

Status: Database Model Design

Last Updated: 2026-07-22

---

# PURPOSE

This document translates the Domain Model into a persistence model.

It defines:

- persisted entities
- ownership
- relationships
- cardinalities
- tenant boundaries

It does not define:

- SQL syntax
- SQLAlchemy implementation
- Alembic migrations
- indexes
- API contracts

These topics belong to future implementation phases.

---

# DATABASE DESIGN PRINCIPLES

The database model must respect:

- ADR-0002 Authentication Strategy
- ADR-0003 Credential Storage Strategy
- ADR-0004 Multi-Tenant Strategy
- ADR-0005 Module Boundary Strategy
- ADR-0006 Self-Hosted Compatibility Strategy

---

# GLOBAL OWNERSHIP MODEL

```text
Organisation (Tenant)
│
├── Memberships
├── Carrier Accounts
├── Searches
├── Exports
└── Settings

User
│
└── Memberships
```

Organisation remains the primary ownership boundary.

---

# ENTITY: ORGANISATIONS

Purpose:

Represents a tenant.

---

## Ownership

Owns:

```text
Memberships
Carrier Accounts
Searches
Exports
Organisation Settings
```

---

## Cardinalities

```text
Organisation
    ├── 0..N Memberships
    ├── 0..N Carrier Accounts
    ├── 0..N Searches
    ├── 0..N Exports
    └── 0..1 Settings
```

---

# ENTITY: USERS

Purpose:

Represents an authenticated identity.

---

## Ownership

Owns:

```text
User Profile
Preferences
```

---

## Cardinalities

```text
User
    └── 0..N Memberships
```

A user may belong to multiple organisations.

---

# ENTITY: MEMBERSHIPS

Purpose:

Associates users and organisations.

---

## Ownership

Belongs to:

```text
One User
One Organisation
```

---

## Cardinalities

```text
Membership
    ├── 1 User
    └── 1 Organisation
```

---

# ROLE STRATEGY

Decision:

Role is attached to Membership.

Not to User.

---

## Reason

A user may have:

```text
Organisation Admin
```

in one organisation

and

```text
Organisation User
```

in another.

Role therefore belongs to the relationship.

---

## Initial Values

```text
SuperAdmin
OrganisationAdmin
OrganisationUser
```

---

# ENTITY: CARRIER ACCOUNTS

Purpose:

Represents carrier connectivity.

---

## Ownership

Belongs to:

```text
One Organisation
```

---

## Cardinalities

```text
Organisation
    └── 0..N Carrier Accounts
```

---

## Candidate Attributes

```text
Carrier Type
Status
Validation Status
Last Validation Date
```

---

# ENTITY: CREDENTIAL REFERENCES

Purpose:

Represents encrypted credential storage.

---

## Ownership

Belongs to:

```text
One Carrier Account
```

---

## Cardinalities

```text
Carrier Account
    └── 1 Credential Reference
```

Current V1 decision:

```text
One carrier account
One credential set
```

---

# ENTITY: SEARCHES

Purpose:

Represents search activity.

---

## Ownership

Belongs to:

```text
One Organisation
```

---

## Cardinalities

```text
Organisation
    └── 0..N Searches
```

---

# ENTITY: SEARCH REQUESTS

Purpose:

Represents search criteria.

---

## Ownership

Belongs to:

```text
One Search
```

---

## Cardinalities

```text
Search
    └── 1 Search Request
```

---

# ENTITY: SEARCH RESULTS

Purpose:

Represents normalized pickup point responses.

---

# IMPORTANT DECISION

Current Direction:

Persist Search Results.

---

## Reasoning

Benefits:

```text
Auditability
Export Support
Search History
Diagnostics
Future Analytics
```

---

## Cardinalities

```text
Search
    └── 0..N Search Results
```

---

# ENTITY: EXPORTS

Purpose:

Represents export operations.

---

## Ownership

Belongs to:

```text
One Organisation
```

---

## Cardinalities

```text
Organisation
    └── 0..N Exports
```

---

# ENTITY: EXPORT FILES

Purpose:

Represents generated downloadable artifacts.

---

## Ownership

Belongs to:

```text
One Export
```

---

## Cardinalities

```text
Export
    └── 1 Export File
```

---

# ENTITY: PLATFORM SETTINGS

Purpose:

Global platform configuration.

---

## Ownership

Platform Wide

Not tenant-owned.

---

## Cardinality

```text
Platform
    └── 1 Settings Record
```

---

# ENTITY: AUDIT EVENTS

Purpose:

Capture important system events.

---

## Ownership

Events may reference:

```text
User
Organisation
Carrier Account
Search
Export
```

---

## Examples

```text
Login
Credential Update
Carrier Validation
Search Execution
Export Creation
```

---

# TENANT BOUNDARY RULES

Mandatory rules:

```text
Organisation data isolated

Carrier Accounts isolated

Credentials isolated

Searches isolated

Exports isolated
```

Cross-tenant ownership is forbidden.

---

# AGGREGATE CANDIDATES

Organisation Aggregate

```text
Organisation
Memberships
```

---

Carrier Aggregate

```text
CarrierAccount
CredentialReference
```

---

Search Aggregate

```text
Search
SearchRequest
SearchResult
```

---

Export Aggregate

```text
Export
ExportFile
```

---

# DATABASE MODEL QUESTIONS

The following questions remain intentionally open.

---

## Search Retention Policy

How long should Search Results be stored?

Status:

Future decision.

---

## Export Retention Policy

How long should export files remain available?

Status:

Future decision.

---

## Audit Retention Policy

How long should audit events remain stored?

Status:

Future decision.

---

# OUT OF SCOPE

This document does not define:

```text
SQLAlchemy Models
Alembic Migrations
Database Tables
Indexes
Constraints
Query Optimization
```

These topics belong to implementation.

---

# NEXT STEP

Phase 7

Persistence Design

Objectives:

- SQLAlchemy models
- entity mapping
- migration strategy
- indexing strategy

---

# CHANGE HISTORY

2026-07-22

Initial database model created.
