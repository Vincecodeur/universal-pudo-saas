# ADR-0005 - Module Boundary Strategy

Status: Accepted

Date: 2026-07-22

Authors:

- Vincent Gueret
- Microsoft Copilot

---

# Context

Universal PUDO SaaS is expected to evolve into a long-term SaaS platform.

Planned capabilities include:

- authentication
- organisations
- users
- carrier accounts
- searches
- exports
- administration
- future APIs

Without clear module boundaries, business logic tends to spread across the application over time.

This often results in:

- duplicated logic
- unclear ownership
- difficult maintenance
- complex testing
- architectural drift

A module boundary strategy must therefore be defined before:

- domain modelling
- database modelling
- feature implementation

---

# Problem Statement

How should business responsibilities be distributed inside Universal PUDO SaaS?

---

## Option A

Technical Layer Boundaries

Examples:

```text
Controllers
Services
Repositories
Models
```

The application is organised by technical responsibility.

---

## Option B

Business Module Boundaries

Examples:

```text
Auth
Organisations
Users
Carrier Accounts
Searches
Exports
Administration
```

Each module owns its domain responsibilities.

---

## Option C

Hybrid Structure

Business modules mixed with technical ownership.

---

# Decision

Accepted Option:

Option B

Business Module Boundaries

---

# Rationale

Universal PUDO SaaS is fundamentally a business platform.

The primary concern is:

```text
Business capability ownership
```

rather than:

```text
Technical file classification
```

Business modules:

- scale better
- support independent evolution
- improve maintainability
- simplify testing
- reduce coupling

---

# Architectural Principle

Every business capability must have a single owner.

Rule:

```text
One Responsibility
One Module
```

A capability should never be owned by multiple modules.

---

# Initial Module Map

The platform is divided into the following business modules.

---

## Module: Auth

Responsibilities:

```text
Authentication
Password Management
JWT Management
Future SSO Integration
```

Non Responsibilities:

```text
Users
Permissions
Organisation Management
```

---

## Module: Organisations

Responsibilities:

```text
Organisation Creation
Organisation Settings
Membership Management
```

Non Responsibilities:

```text
Authentication
Search Execution
```

---

## Module: Users

Responsibilities:

```text
User Profiles
User Preferences
User Metadata
```

Non Responsibilities:

```text
Authentication
Carrier Accounts
```

---

## Module: Carrier Accounts

Responsibilities:

```text
Carrier Configuration
Credential Storage
Credential Validation
Connectivity Tests
```

Non Responsibilities:

```text
Provider Logic
Carrier APIs
Provider Execution
```

These belong to Universal PUDO Engine.

---

## Module: Searches

Responsibilities:

```text
Search Requests
Search Orchestration
Search History
```

Non Responsibilities:

```text
Carrier Integrations
Provider Execution
```

These belong to Universal PUDO Engine.

---

## Module: Exports

Responsibilities:

```text
Export Creation
Export History
Export Delivery
```

Non Responsibilities:

```text
Search Logic
Authentication
```

---

## Module: Administration

Responsibilities:

```text
Diagnostics
Monitoring
Organisation Oversight
Platform Governance
```

Non Responsibilities:

```text
Search Execution
Carrier Logic
```

---

# Module Communication Rules

Modules should communicate through defined service contracts.

Preferred communication:

```text
Module A
     ↓
Application Service
     ↓
Module B
```

Avoid:

```text
Direct Database Access Between Modules
```

---

# Ownership Rules

Every business object belongs to exactly one module.

Examples:

```text
CarrierAccount
  → Carrier Accounts Module

Organisation
  → Organisations Module

Export
  → Exports Module
```

Shared ownership is forbidden.

---

# Universal PUDO Engine Boundary

The following responsibilities remain outside SaaS module ownership:

```text
Carrier Integrations
Provider Implementations
ProviderFactory
Payload Mapping
Payload Parsing
Pickup Point Normalization
Carrier Synchronization
```

These responsibilities belong exclusively to:

Universal PUDO Engine

---

# Database Compatibility

This ADR does not define the database schema.

However database entities must respect module ownership.

Example:

```text
CarrierAccount Entity
```

must belong to:

```text
Carrier Accounts Module
```

and not to multiple modules.

---

# API Compatibility

Future APIs should mirror module boundaries.

Examples:

```text
/auth

/organisations

/users

/carrier-accounts

/searches

/exports

/admin
```

This improves consistency and long-term maintainability.

---

# Testing Compatibility

Testing strategy should follow module ownership.

Examples:

```text
Auth Tests

Organisation Tests

Carrier Account Tests

Search Tests
```

Module isolation should simplify testing.

---

# Rejected Alternatives

---

## Option A

Technical Layer Boundaries

Status:

Rejected

Reason:

Business ownership becomes unclear.

Large applications tend to accumulate tightly coupled logic.

---

## Option C

Hybrid Structure

Status:

Rejected

Reason:

Creates ambiguity.

Responsibility ownership becomes difficult to determine.

---

# Positive Consequences

```text
Clear Ownership
Reduced Coupling
Improved Maintainability
Simpler Testing
Improved Scalability
Cleaner APIs
```

---

# Negative Consequences

```text
Module Boundaries Must Be Enforced
Cross-Module Work Requires Discipline
Initial Design Effort Is Higher
```

These drawbacks are acceptable.

---

# Architectural Constraints

This ADR does not authorize:

```text
Shared Ownership
Business Logic Duplication
Carrier Logic Inside SaaS Modules
Cross-Module Database Bypasses
```

These constraints are mandatory.

---

# Future Re-evaluation

This ADR should be revisited when:

```text
New Business Domains Appear
Enterprise Modules Are Introduced
Billing Is Implemented
Analytics Become First-Class Features
```

Current expectation:

The module structure remains stable throughout V1.

---

# Related Documents

- docs/project-memory.md
- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md
- docs/project-status.md

---

# Related ADRs

ADR-0001

Repository Structure Strategy

ADR-0002

Authentication Strategy

ADR-0003

Credential Storage Strategy

ADR-0004

Multi-Tenant Strategy

ADR-0006

Public API Strategy (planned)

ADR-0007

Self-Hosted Compatibility Strategy (planned)

---

# Status History

2026-07-22

Accepted.
