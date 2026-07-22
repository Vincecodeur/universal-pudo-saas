# ADR-0004 - Multi-Tenant Strategy

Status: Accepted

Date: 2026-07-22

Authors:

- Vincent Gueret
- Microsoft Copilot

---

# Context

Universal PUDO SaaS is designed as a shared platform serving multiple independent organisations.

Target customer types include:

- Logistics Providers (3PL)
- E-commerce Merchants
- Software Vendors

Each organisation requires independent ownership of:

- users
- carrier accounts
- searches
- exports
- settings
- permissions

Before designing:

- the domain model
- the database schema
- the API architecture
- the permission model

the project must establish a clear tenant strategy.

---

# Problem Statement

How should tenant isolation be implemented?

---

## Option A

Single-Tenant Platform

One deployment.

One organisation.

No tenant isolation required.

---

## Option B

Multi-Tenant Shared Platform

Single platform.

Multiple organisations.

Shared infrastructure.

Logical isolation.

---

## Option C

Dedicated Deployment Per Organisation

Each customer receives:

- dedicated infrastructure
- dedicated application deployment
- dedicated database

---

# Decision

Accepted Option:

Option B

Multi-Tenant Shared Platform

---

# Rationale

The product vision explicitly targets multiple organisations using the same platform.

The platform must support:

- scalability
- operational efficiency
- future growth

A multi-tenant architecture provides the best balance between:

- development effort
- hosting cost
- maintainability
- future expansion

while remaining compatible with future self-hosted deployments.

---

# Tenant Definition

For V1:

```text
Tenant
=
Organisation
```

The terms:

```text
Tenant
Organisation
```

are considered equivalent.

Future platform evolution may introduce more complex organisational hierarchies, but they are out of scope for V1.

---

# Tenant Ownership Model

Each tenant owns its own business data.

Examples:

```text
Users
Carrier Accounts
Searches
Exports
Settings
Permissions
```

No tenant owns or shares business data belonging to another tenant.

---

# Isolation Strategy

The platform uses:

```text
Logical Isolation
```

Shared resources:

```text
Application
Infrastructure
Database
```

Isolated resources:

```text
Business Data
Permissions
Carrier Credentials
Search History
Exports
```

Tenant boundaries are enforced by the application.

---

# Data Ownership Principle

Every business object must belong to a tenant.

Examples:

```text
Organisation
Membership
Carrier Account
Search
Export
```

Rule:

Business objects without tenant ownership are forbidden.

---

# User Model

Authentication and tenancy remain separate concerns.

Relationship:

```text
User
 │
 ▼
Membership
 │
 ▼
Organisation
```

Flow:

```text
Authenticate User
       ↓
Resolve Membership
       ↓
Resolve Tenant Context
       ↓
Apply Permissions
```

This separation improves flexibility and future SSO compatibility.

---

# Membership Strategy

The architecture must support:

```text
Multiple Memberships
```

Example:

```text
User A
 ├── Organisation X
 └── Organisation Y
```

Even if the first UI implementation exposes only simple membership management.

This avoids future redesign.

---

# Carrier Account Isolation

Carrier accounts are tenant-scoped.

Example:

```text
Organisation A
 └── Colissimo Account A

Organisation B
 └── Colissimo Account B
```

Credentials must never be shared across organisations.

This rule is mandatory.

---

# Search Isolation

Searches belong to the tenant that initiated them.

Example:

```text
Organisation A
 └── Search History A

Organisation B
 └── Search History B
```

Search history is tenant-specific.

Cross-tenant visibility is forbidden.

---

# Export Isolation

Exports belong to the tenant that generated them.

Rules:

```text
No cross-tenant access
No cross-tenant downloads
No shared export ownership
```

---

# Administration Model

Two administration levels exist.

---

## SaaS Super Admin

Scope:

Platform-wide.

Capabilities:

```text
Organisation Management
Platform Monitoring
Diagnostics
Support Operations
```

---

## Organisation Admin

Scope:

Single Tenant.

Capabilities:

```text
User Management
Carrier Management
Organisation Settings
```

Organisation admins must not access other organisations.

---

# Database Compatibility

Future database modelling must support tenant ownership.

Expected examples:

```text
organisation_id
```

on tenant-owned entities.

The exact schema remains a database design decision.

---

# API Compatibility

All future APIs must be tenant-aware.

Requirements:

```text
Tenant Context Validation
Permission Enforcement
Data Ownership Verification
```

API endpoints exposing tenant data without ownership validation are forbidden.

---

# Security Requirements

Mandatory requirements:

```text
Tenant Isolation
Access Control
Role Enforcement
Credential Isolation
Auditability
```

Tenant boundary violations are considered critical security events.

---

# Self-Hosted Compatibility

This strategy must remain compatible with:

```text
Multi-Tenant SaaS
Private Cloud
Self-Hosted Deployment
```

Tenant isolation remains mandatory in every deployment model.

---

# Rejected Alternatives

---

## Option A

Single-Tenant Platform

Status:

Rejected

Reason:

Incompatible with long-term product vision.

Would prevent SaaS scalability.

---

## Option C

Dedicated Deployment Per Organisation

Status:

Rejected

Reason:

Higher operational complexity.

Higher hosting costs.

Reduced maintainability.

Not justified for V1.

---

# Positive Consequences

```text
Scalable SaaS Architecture
Shared Infrastructure
Lower Operating Cost
Future API Compatibility
Future Enterprise Compatibility
```

---

# Negative Consequences

```text
More Complex Permission System
Stronger Security Requirements
Tenant Isolation Must Be Enforced Everywhere
```

These drawbacks are considered acceptable.

---

# Architectural Constraints

This ADR does not authorize:

```text
Cross-Tenant Data Access
Credential Sharing
Shared Search History
Tenant-Free Business Objects
Direct Tenant Bypass
```

These constraints are mandatory.

---

# Future Re-evaluation

This ADR should be revisited when:

```text
Enterprise Requirements Expand
Advanced Organisation Hierarchies Appear
Dedicated Customer Deployments Become Necessary
```

Current expectation:

The strategy remains valid throughout V1 and future major releases.

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

ADR-0007

Self-Hosted Compatibility Strategy

---

# Status History

2026-07-22

Accepted.
