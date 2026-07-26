# Carrier Account Architecture

Version: 1.0

Status: Draft

Last Updated: 2026-07-25

---

# Purpose

This document defines how Carrier Account Management integrates into the Universal PUDO SaaS architecture.

It formalizes the boundary between:

- Organisations
- Carrier Accounts
- Carrier Integrations
- Universal PUDO SaaS
- Universal PUDO Engine

---

# Architecture Principle

Universal PUDO SaaS manages:

- Organisations
- Users
- Memberships
- Roles
- Carrier Accounts
- Carrier Credentials

Universal PUDO Engine manages:

- Carrier APIs
- Carrier Adapters
- Carrier Business Logic
- Search Orchestration
- Pickup Point Normalization

The SaaS configures.

The Engine executes.

---

# High-Level Architecture

Organisation
|
+---- Carrier Account
|
+---- Carrier Credentials
|
+---- carrier_code
|
+---- Universal PUDO Engine Carrier Catalog

---

# Responsibility Matrix

Organisation

Owns:

- Carrier Accounts

Does NOT own:

- Carrier Integrations

---

Carrier Catalog

Owned by Universal PUDO Engine.

Consumed by Universal PUDO SaaS.

Not persisted inside Universal PUDO SaaS.

---

Carrier Account

Owns:

- Operational configuration
- Credential references

Does NOT own:

- Carrier implementation

---

Universal PUDO Engine

Consumes:

- Carrier Name
- Credentials
- Search Parameters

Produces:

- Pickup Point Results

---

# Example Execution Flow

User
↓

Organisation

    ↓

Carrier Account

    ↓

Carrier Credentials

    ↓

Universal PUDO Engine

    ↓

Carrier API

    ↓

Normalized Pickup Points

    ↓

Universal PUDO SaaS

---

# Boundary Rules

Rule 1

Carrier APIs never communicate directly with Organisations.

All communication passes through the SaaS.

---

Rule 2

Universal PUDO Engine never owns customer credentials.

Credentials belong to the SaaS.

---

Rule 3

Carrier Integrations are globally managed.

Organisations only consume them.

---

Rule 4

Search execution belongs to Universal PUDO Engine.

Search authorization belongs to SaaS.

---

# Future Permissions Model

Planned

SAAS_ADMIN

- Global administration

OWNER

- Manage carrier accounts

VIEWER

- Read-only access

Permission enforcement is not part of Phase 14.

---

# Future Carrier Workflow

Carrier Catalog
↓
Carrier Account
↓
Credential Validation
↓
Activation
↓
Search Execution

---

# Future Extensions

Not part of this phase:

- Audit logging
- Encryption
- Secret vault
- Carrier monitoring
- Usage analytics
- Quotas
- Billing

---

# Validation Criteria

Architecture Integration Foundation is complete when:

- SaaS responsibilities defined
- Engine responsibilities defined
- Ownership boundaries defined
- Execution flow defined
- Search responsibility defined
- Credential ownership defined
