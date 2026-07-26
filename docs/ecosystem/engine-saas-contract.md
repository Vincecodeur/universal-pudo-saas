# Engine ↔ SaaS Contract

Version: 1.0

Status: Draft

Last Updated: 2026-07-26

---

# Purpose

This document defines the integration contract between:

```text
universal-pudo-engine
```

and

```text
universal-pudo-saas
```

---

# Ownership

## Engine Owns

- carriers
- carrier capabilities
- provider implementations
- pickup point discovery
- normalization
- search orchestration

---

## SaaS Owns

- users
- organisations
- memberships
- authentication
- carrier accounts
- carrier credentials
- permissions
- administration

---

# Integration Principle

The SaaS consumes Engine capabilities.

The SaaS never reimplements carrier logic.

---

# Carrier Ownership

The Engine is the source of truth for:

- carrier identity
- carrier lifecycle
- carrier capabilities

The SaaS stores only:

- CarrierAccount
- CarrierCredential

The SaaS must never maintain its own carrier catalog.

---

# Activation Workflow

User selects a carrier.

↓

SaaS validates carrier existence through Engine.

↓

SaaS creates CarrierAccount.

↓

SaaS stores credentials.

↓

Engine executes carrier functionality.

---

# Architectural Boundary

Engine responsibilities stop at:

```text
Provider execution
```

SaaS responsibilities start at:

```text
User management
```

Neither repository owns responsibilities of the other.

---

# Future Evolution

Possible future additions:

- Engine version compatibility
- capability discovery
- carrier lifecycle handling
- activation validation
- SDK integration support

---

# Decision Summary

The Engine remains the owner of carrier functionality.

The SaaS remains the owner of carrier configuration and administration.

The contract focuses on consumption rather than duplication.
