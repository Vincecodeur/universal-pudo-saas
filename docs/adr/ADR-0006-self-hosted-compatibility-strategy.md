# ADR-0006 - Self-Hosted Compatibility Strategy

Status: Accepted

Date: 2026-07-22

Authors:

- Vincent Gueret
- Microsoft Copilot

---

# Context

Universal PUDO SaaS is primarily designed as:

SaaS-first

However, the product vision explicitly states:

Self-host-ready

This means that V1 will be delivered as a shared SaaS platform, but future deployment models may include:

- customer-managed deployments
- private cloud deployments
- enterprise deployments
- self-hosted installations

The project must define architectural constraints now to avoid future redesign.

---

# Problem Statement

How should the platform prepare for future self-hosting while remaining focused on SaaS delivery?

---

## Option A

Pure SaaS

Assume the platform will always be hosted by us.

No self-host considerations.

---

## Option B

Build Full Self-Hosted Support Immediately

Design and implement:

- installation packages
- deployment automation
- customer-operated infrastructure

from the beginning.

---

## Option C

SaaS-First / Self-Hosted Compatible

Develop only the SaaS version.

Apply architectural rules that preserve future self-host viability.

---

# Decision

Accepted Option:

Option C

SaaS-First / Self-Hosted Compatible

---

# Rationale

The project currently has:

- no production users
- no enterprise customers
- no self-hosting requirements

Implementing self-hosted functionality now would create complexity without immediate value.

However, completely ignoring self-hosting would risk future architectural lock-in.

Option C provides the best balance between:

- delivery speed
- simplicity
- future flexibility

---

# Architectural Principle

Rule:

Build SaaS today.

Avoid architectural decisions that would prevent self-hosting tomorrow.

---

# Current Scope

The following deployment model is officially supported:

```text
Multi-Tenant SaaS
```

Only.

No self-hosted implementation is planned during V1.

---

# Future Scope

Potential future deployment models include:

```text
Private Cloud
Enterprise Hosted
Customer Managed Infrastructure
Self-Hosted Installations
```

No commitment is made regarding delivery dates.

---

# Configuration Strategy

Application configuration must not be hardcoded.

Configuration should be externalized.

Examples:

```text
Database Connection
Secrets
Environment Variables
Feature Flags
```

The application must be deployable in different environments without code changes.

---

# Secret Management Strategy

The platform must avoid vendor-specific secret dependencies.

Examples of future-compatible solutions:

```text
Environment Variables
Azure Key Vault
AWS Secrets Manager
HashiCorp Vault
Google Secret Manager
```

No deployment model should be forced by secret management choices.

---

# Database Compatibility

The application must not assume a specific hosting provider.

Examples:

```text
Managed PostgreSQL
Self-Hosted PostgreSQL
Containerized PostgreSQL
```

The architecture should support all reasonable PostgreSQL deployment scenarios.

---

# Storage Compatibility

The application must not tightly couple business logic to a specific cloud provider.

Examples:

```text
Local Storage
Object Storage
Cloud Storage
```

Storage implementation should remain replaceable.

---

# Application Portability

The application should remain portable across:

```text
Cloud
Private Cloud
On-Premise
Container Platforms
```

Portability is a design objective.

---

# Deployment Portability

Future deployment targets may include:

```text
Docker
Kubernetes
Virtual Machines
Managed Platforms
```

The architecture should remain compatible with multiple deployment approaches.

---

# Core Dependency Compatibility

Universal PUDO SaaS depends on:

Universal PUDO Engine

This dependency must remain portable.

The SaaS should avoid dependency strategies that make self-hosted deployments difficult.

---

# Tenant Compatibility

Self-hosted deployments do not remove tenant requirements.

Rules remain valid:

```text
Tenant Isolation
Credential Isolation
Permission Enforcement
```

Even in a dedicated deployment.

---

# Security Compatibility

Security requirements remain identical across deployment models.

Examples:

```text
Authentication
Encryption
Credential Protection
Access Control
Auditability
```

Hosting location must not weaken security expectations.

---

# Rejected Alternatives

---

## Option A

Pure SaaS

Status:

Rejected

Reason:

Creates long-term architectural lock-in.

Incompatible with future enterprise requirements.

---

## Option B

Full Self-Hosted Implementation From Day One

Status:

Rejected

Reason:

Premature complexity.

No business justification.

Would slow product delivery.

---

# Positive Consequences

```text
Faster Initial Delivery
Lower Complexity
Future Flexibility
Enterprise Compatibility
Lower Risk Of Future Redesign
```

---

# Negative Consequences

```text
Additional Architectural Discipline Required
Some Future Deployment Work Deferred
Future Packaging Work Still Required
```

These drawbacks are acceptable.

---

# Architectural Constraints

This ADR does not authorize:

```text
Cloud Vendor Lock-In
Hardcoded Infrastructure Assumptions
Single Deployment Model Assumptions
Environment-Specific Business Logic
```

These constraints are mandatory.

---

# Future Re-evaluation

This ADR should be revisited when:

```text
Enterprise Customers Appear
Private Deployments Are Requested
Dedicated Hosting Becomes A Requirement
```

Current expectation:

This strategy remains valid throughout V1 and future major releases.

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

ADR-0005

Module Boundary Strategy

---

# Status History

2026-07-22

Accepted.
