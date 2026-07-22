# Universal PUDO SaaS - Domain Model

Version: 0.1.0

Status: Domain Modeling

Last Updated: 2026-07-22

---

# PURPOSE

This document defines the business domain model of Universal PUDO SaaS.

It describes:

- business entities
- ownership
- responsibilities
- relationships

It does not describe:

- database schema
- implementation
- APIs
- infrastructure

These topics belong to later phases.

---

# DOMAIN PRINCIPLES

The domain model must respect:

ADR-0002 Authentication Strategy

ADR-0003 Credential Storage Strategy

ADR-0004 Multi-Tenant Strategy

ADR-0005 Module Boundary Strategy

ADR-0006 Self-Hosted Compatibility Strategy

---

# DOMAIN OVERVIEW

The platform is composed of the following business domains:

```text
Organisation
User
Carrier Account
Search
Export
Administration
```

---

# ORGANISATION DOMAIN

Organisation is the primary tenant of the platform.

All business objects belong to an organisation.

---

## Entity

Organisation

---

## Responsibilities

```text
Own Users
Own Carrier Accounts
Own Searches
Own Exports
Own Settings
```

---

## Business Rules

```text
An organisation owns its data.

An organisation cannot access another organisation's data.
```

---

# USER DOMAIN

Users represent authenticated identities.

Authentication and tenancy remain separate concerns.

---

## Entity

User

---

## Responsibilities

```text
Authentication Identity
Profile Ownership
Preference Ownership
```

---

## Business Rules

```text
A user may belong to multiple organisations.

A user authenticates before tenant resolution.
```

---

# MEMBERSHIP DOMAIN

Membership links users and organisations.

---

## Entity

Membership

---

## Responsibilities

```text
Tenant Association
Role Assignment
Access Control Context
```

---

## Business Rules

```text
A membership belongs to one user.

A membership belongs to one organisation.

Permissions are evaluated through memberships.
```

---

# ROLE DOMAIN

Roles define permissions.

---

## Entity

Role

---

## Initial Roles

```text
SuperAdmin
OrganisationAdmin
OrganisationUser
```

---

## Business Rules

```text
Roles do not authenticate users.

Roles define capabilities.
```

---

# CARRIER ACCOUNT DOMAIN

Carrier Accounts represent carrier connectivity owned by organisations.

---

## Entity

CarrierAccount

---

## Responsibilities

```text
Carrier Configuration
Credential Ownership
Connection Status
Account Lifecycle
```

---

## Business Rules

```text
A Carrier Account belongs to one organisation.

Carrier credentials are organisation-owned.

Carrier Accounts never belong to users.
```

---

# CREDENTIAL DOMAIN

Credentials are sensitive assets attached to Carrier Accounts.

---

## Entity

CredentialReference

---

## Responsibilities

```text
Credential Ownership
Credential Access
Credential Security
```

---

## Business Rules

```text
Credentials belong to Carrier Accounts.

Credentials must remain isolated per organisation.
```

---

# SEARCH DOMAIN

Searches represent pickup point discovery requests.

---

## Entity

Search

---

## Responsibilities

```text
Search Execution Request
Search History
Search Traceability
```

---

## Business Rules

```text
Searches belong to an organisation.

Searches never belong directly to a carrier.
```

---

# SEARCH REQUEST DOMAIN

Search requests capture search criteria.

---

## Entity

SearchRequest

---

## Examples

```text
Postal Code Search
City Search
Coordinate Search
```

---

## Responsibilities

```text
Input Validation
Search Criteria Definition
```

---

# SEARCH RESULT DOMAIN

Search results represent normalized pickup point responses.

---

## Entity

SearchResult

---

## Responsibilities

```text
Result Presentation
Result Reuse
Export Source Data
```

---

## Business Rules

```text
Search results originate from Universal PUDO Engine.

Normalization belongs to the Core.
```

---

# EXPORT DOMAIN

Exports represent reusable output generated from search activity.

---

## Entity

Export

---

## Responsibilities

```text
Export Creation
Export Lifecycle
Export Ownership
```

---

## Business Rules

```text
Exports belong to one organisation.
```

---

# EXPORT FILE DOMAIN

Represents generated export artifacts.

---

## Entity

ExportFile

---

## Responsibilities

```text
Download Availability
Export Delivery
Export Retention
```

---

# ADMINISTRATION DOMAIN

Administration manages the platform.

---

## Entity

PlatformSettings

---

## Responsibilities

```text
Platform Configuration
Operational Governance
```

---

# AUDIT DOMAIN

Captures important platform events.

---

## Entity

AuditEvent

---

## Responsibilities

```text
Traceability
Security Monitoring
Operational Visibility
```

---

## Examples

```text
User Login
Carrier Account Creation
Credential Update
Search Execution
Export Creation
```

---

# DOMAIN OWNERSHIP MAP

```text
Auth Module
 ├── User
 ├── Role

Organisation Module
 ├── Organisation
 ├── Membership

Carrier Accounts Module
 ├── CarrierAccount
 ├── CredentialReference

Search Module
 ├── Search
 ├── SearchRequest
 ├── SearchResult

Export Module
 ├── Export
 ├── ExportFile

Administration Module
 ├── PlatformSettings
 ├── AuditEvent
```

---

# AGGREGATE CANDIDATES

Potential future aggregates:

Organisation Aggregate

```text
Organisation
Membership
Role
```

Carrier Account Aggregate

```text
CarrierAccount
CredentialReference
```

Search Aggregate

```text
Search
SearchRequest
SearchResult
```

Export Aggregate

```text
Export
ExportFile
```

---

# OUT OF SCOPE

This document does not define:

```text
Database Tables
SQL Types
Indexes
APIs
Controllers
Repositories
Services
```

These belong to future phases.

---

# NEXT STEP

Phase 6

Database Model Design

Objective:
