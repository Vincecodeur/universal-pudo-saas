# ADR-0003 - Credential Storage Strategy

Status: Accepted

Date: 2026-07-22

Authors:

- Vincent Gueret
- Microsoft Copilot

---

# Context

Universal PUDO SaaS allows organisations to connect their own carrier accounts.

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- DPD
- GLS
- UPS
- InPost

Carrier integrations are executed by:

Universal PUDO Engine

However, carrier credentials belong to customer organisations.

A clear strategy is required regarding:

- ownership
- storage
- encryption
- access
- usage

of carrier credentials.

This decision has direct impact on:

- security
- multi-tenancy
- self-host compatibility
- provider execution
- administration
- future audits

---

# Problem Statement

Where should carrier credentials be owned and managed?

Option A

Credentials managed by Universal PUDO SaaS.

Core consumes credentials.

---

Option B

Credentials managed directly by Universal PUDO Engine.

---

Option C

External credential platform required from day one.

Examples:

- Vault
- Cloud Key Vault
- Secret Manager

---

# Decision

Accepted Option:

Option A

Carrier credentials are owned and managed by Universal PUDO SaaS.

Universal PUDO Engine consumes credentials but never owns them.

---

# Rationale

The Core is designed to remain:

- reusable
- portable
- carrier focused

The Core should not become:

- an identity platform
- a credential management platform
- a tenant management platform

Credential ownership belongs naturally to the SaaS application layer.

---

# Ownership Model

Relationship:

```text
Organisation
│
└── Carrier Account
       │
       └── Credentials
```

The organisation owns:

- carrier accounts
- credentials

The SaaS manages:

- storage
- updates
- validation
- access controls

The Core only consumes credentials during provider execution.

---

# Core / SaaS Responsibility Boundary

---

## SaaS Responsibilities

```text
Credential Creation
Credential Update
Credential Validation
Credential Encryption
Credential Access Control
Credential Auditing
```

---

## Core Responsibilities

```text
Credential Consumption
Provider Execution
Carrier Communication
```

---

## Forbidden Core Responsibilities

```text
Credential Storage
Credential Ownership
Credential Administration
Credential Lifecycle Management
```

---

# Initial Storage Strategy

V1 strategy:

```text
Credentials stored in PostgreSQL
```

The database record should contain:

```text
Carrier
Organisation
Credential Metadata
Encrypted Credential Payload
```

Plain text credentials must never be stored.

---

# Encryption Strategy

Requirement:

```text
Credentials must be encrypted before persistence.
```

The precise implementation remains an implementation detail.

This ADR defines the architectural principle, not the technical library.

---

# Access Control Strategy

Only authorised users may:

```text
View Carrier Account Configuration
Update Credentials
Disable Credentials
Run Connection Tests
```

Role enforcement remains a SaaS responsibility.

---

# Provider Execution Flow

```text
User
↓
Search Request
↓
SaaS Service Layer
↓
Retrieve Encrypted Credentials
↓
Decrypt Credentials
↓
Core Adapter
↓
Universal PUDO Engine
↓
Provider Execution
```

The Core receives only the credentials required to execute the provider request.

---

# Multi-Tenant Compatibility

Credentials are tenant-scoped.

Relationship:

```text
Organisation A
   └── Credentials A

Organisation B
   └── Credentials B
```

No credential sharing exists between organisations.

This rule is mandatory.

---

# Self-Hosted Compatibility

The storage strategy must remain compatible with:

```text
Cloud Deployment
Private Cloud
Self-Hosted Deployment
```

The architecture must avoid vendor lock-in.

---

# Future Secret Management Compatibility

Future implementations may use:

```text
HashiCorp Vault
Azure Key Vault
AWS Secrets Manager
Google Secret Manager
```

The architecture must support migration without redesign.

---

# Rejected Alternatives

---

## Option B

Credentials owned by Universal PUDO Engine

Status:

Rejected

Reason:

Violates Core/SaaS separation.

Creates tenant-management responsibilities inside the Core.

Reduces Core portability.

---

## Option C

External Secret Platform Required From Day One

Status:

Rejected

Reason:

Premature complexity.

Not justified during early project stages.

Can be introduced later without redesigning ownership.

---

# Security Requirements

Mandatory principles:

```text
Encrypted Storage
Least Privilege
Tenant Isolation
Auditability
Controlled Access
```

---

# Positive Consequences

```text
Clear Ownership
Strong Core/SaaS Separation
Multi-Tenant Compatibility
Future Secret Manager Compatibility
Self-Hosted Compatibility
```

---

# Negative Consequences

```text
Credential Security Becomes SaaS Responsibility
Additional Encryption Implementation Required
Future Secret Migration Work Required
```

These drawbacks are acceptable.

---

# Architectural Constraints

This ADR does not authorize:

```text
Plain Text Credential Storage
Credential Sharing Across Organisations
Credential Ownership Inside Core
```

These constraints are mandatory.

---

# Future Re-evaluation

This ADR should be revisited when:

```text
Enterprise Customers Request Vault Integration
Self-Hosted Deployments Are Introduced
Dedicated Secret Platforms Become Necessary
```

Current expectation:

The strategy remains valid for V1 and several future releases.

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

ADR-0006

Multi-Tenant Strategy

ADR-0007

Self-Hosted Compatibility Strategy

---

# Status History

2026-07-22

Accepted.
