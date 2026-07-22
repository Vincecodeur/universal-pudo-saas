# Universal PUDO SaaS - Persistence Decisions

Version: 0.1.0

Status: Persistence Design

Last Updated: 2026-07-22

---

# PURPOSE

This document captures persistence decisions that affect the entire data model.

Its purpose is to avoid making structural persistence decisions directly in implementation.

These decisions apply across all future entities.

---

# DECISION 001

Identifier Strategy

Status:

Accepted

---

## Decision

Use UUID identifiers for all business entities.

Examples:

```text
Organisation
User
Membership
CarrierAccount
Search
Export
AuditEvent
```

---

## Reasoning

Benefits:

```text
Globally Unique
Distributed-System Friendly
Self-Hosted Friendly
API Friendly
Safer Than Sequential IDs
```

---

## Consequences

All primary entities will use:

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

All persisted business entities inherit from a common Base Entity.

---

## Common Attributes

```text
id
created_at
updated_at
```

---

## Goal

Provide:

```text
Consistency
Traceability
Maintainability
```

across the data model.

---

# DECISION 003

Timestamp Strategy

Status:

Accepted

---

## Decision

Every persisted entity contains:

```text
created_at
updated_at
```

---

## Reasoning

Supports:

```text
Auditing
Diagnostics
Debugging
Analytics
```

---

## Future Possibility

Additional timestamps may be added:

```text
deleted_at
last_accessed_at
last_validated_at
```

when required.

---

# DECISION 004

Soft Delete Strategy

Status:

Accepted

---

## Decision

Business entities use Soft Delete.

---

## Applicability

Examples:

```text
CarrierAccount
Search
Export
Organisation
```

---

## Implementation Principle

Entities are marked inactive rather than physically removed.

Future common attribute:

```text
deleted_at
```

---

## Reasoning

Supports:

```text
Recovery
Auditability
Compliance
Diagnostics
```

---

# DECISION 005

Audit Strategy

Status:

Accepted

---

## Decision

Centralized Audit Model.

---

## Entity

AuditEvent

---

## Examples

```text
User Login
Password Reset
Credential Update
Carrier Validation
Search Execution
Export Creation
```

---

## Goal

Provide a single audit source.

---

# DECISION 006

Organisation Settings

Status:

Accepted

---

## Decision

Organisation-specific settings are supported.

---

## Entity

OrganisationSettings

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

Belongs to:

```text
One Organisation
```

---

# DECISION 007

Role Ownership Strategy

Status:

Accepted

---

## Decision

Roles belong to Membership.

Not to User.

---

## Example

```text
User A
 ├── Organisation X
 │      └── Admin
 │
 └── Organisation Y
        └── User
```

---

## Reasoning

Supports multi-organisation membership.

---

# DECISION 008

Search Result Persistence

Status:

Accepted

---

## Decision

Search Results are persisted.

---

## Benefits

```text
Search History
Exports
Auditability
Diagnostics
Analytics
```

---

## Consequence

SearchResult becomes a persistent business entity.

---

# DECISION 009

Credential Persistence Model

Status:

Accepted

---

## Decision

Carrier credentials remain:

```text
Encrypted
Tenant-Owned
CarrierAccount-Owned
```

---

## Constraint

Plain text credential storage is forbidden.

---

# DECISION 010

Tenant Ownership Rule

Status:

Accepted

---

## Decision

Every tenant-owned entity must reference an Organisation.

Examples:

```text
CarrierAccount
Search
Export
Membership
OrganisationSettings
```

---

## Goal

Guarantee tenant isolation.

---

# ENTITY CLASSIFICATION

---

## Global Entities

```text
User
Role
PlatformSettings
AuditEvent
```

---

## Tenant-Owned Entities

```text
Organisation
Membership
CarrierAccount
CredentialReference
Search
SearchRequest
SearchResult
Export
ExportFile
OrganisationSettings
```

---

# FUTURE DECISIONS

Not yet decided.

---

## Search Retention

How long SearchResults remain stored.

Status:

Deferred.

---

## Export Retention

How long ExportFiles remain available.

Status:

Deferred.

---

## Audit Retention

How long AuditEvents remain stored.

Status:

Deferred.

---

## API Key Strategy

Public API identifiers.

Status:

Deferred.

---

# NEXT STEP

Implementation Preparation

Future objectives:

```text
SQLAlchemy Models
Alembic Strategy
Database Constraints
Indexes
Repository Layer
```

---

# CHANGE HISTORY

2026-07-22

Initial persistence decisions created.
