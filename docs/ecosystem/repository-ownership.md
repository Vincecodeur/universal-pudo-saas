# Repository Ownership

Version: 1.0

Status: Accepted

Last Updated: 2026-07-26

Location:

docs/ecosystem/repository-ownership.md

---

# Purpose

This document defines ownership boundaries across the Universal PUDO ecosystem.

Its primary purpose is to prevent architectural confusion between repositories and to ensure that responsibilities remain clearly separated as the ecosystem grows.

This document is the official reference whenever there is uncertainty regarding:

- where a change should be implemented
- which repository owns a feature
- which repository owns a contract
- which repository owns a business capability

---

# Ecosystem Overview

Current repositories:

```text
universal-pudo-engine
universal-pudo-saas
```

Future repositories may include:

```text
universal-pudo-sdk-python
universal-pudo-sdk-typescript
universal-pudo-cms-woocommerce
universal-pudo-cms-prestashop
```

Each repository has a distinct responsibility.

---

# Repository Ownership Model

The ecosystem follows a simple rule:

```text
Engine
    owns implementation

Consumer
    owns consumption

Consumer
    owns its contract documentation
```

Examples:

```text
Engine ↔ SaaS
Contract lives in:
universal-pudo-saas

Engine ↔ WooCommerce
Contract lives in:
universal-pudo-cms-woocommerce

Engine ↔ Python SDK
Contract lives in:
universal-pudo-sdk-python
```

---

# Universal PUDO Engine Ownership

Repository:

```text
universal-pudo-engine
```

The Engine owns:

- carrier integrations
- provider implementations
- carrier clients
- carrier response parsers
- carrier mappers
- carrier discovery
- carrier lifecycle management
- carrier capabilities
- pickup point normalization
- provider execution
- provider health
- synchronization
- hybrid search
- public Core interfaces
- carrier metadata
- carrier catalog implementation

The Engine is the single source of truth for carrier functionality.

---

# Universal PUDO SaaS Ownership

Repository:

```text
universal-pudo-saas
```

The SaaS owns:

- authentication
- users
- organisations
- memberships
- permissions
- carrier accounts
- carrier credentials
- administration
- dashboards
- reporting
- future billing
- future subscription management
- frontend
- user experience

The SaaS consumes the Engine.

The SaaS never reimplements carrier integrations.

---

# Contract Ownership Rules

The consumer repository owns the contract.

Reason:

```text
The consumer defines how it consumes
Engine capabilities.
```

Examples:

Engine ↔ SaaS

```text
Owner:
universal-pudo-saas

Documentation:
docs/ecosystem/
```

Engine ↔ WooCommerce

```text
Owner:
universal-pudo-cms-woocommerce

Documentation:
docs/ecosystem/
```

Engine ↔ Python SDK

```text
Owner:
universal-pudo-sdk-python

Documentation:
docs/ecosystem/
```

---

# Ecosystem Documentation Ownership

The following documents belong inside:

```text
universal-pudo-saas/docs/ecosystem/
```

Current documents:

```text
future-consumers.md

adr-ecosystem-0001-public-contract.md

adr-ecosystem-0002-publication-rules.md

engine-saas-contract.md

repository-ownership.md
```

These documents are ecosystem-level documents.

They are not Engine ADRs.

They are not SaaS implementation documents.

They describe interaction rules between repositories.

---

# Decision Classification Rules

Every future architectural discussion must be classified into one of three categories.

---

## Category A

ENGINE

Questions:

```text
How should ProviderFactory work?

How should synchronization work?

How should CarrierLifecycle work?

How should pickup point normalization work?
```

Repository:

```text
universal-pudo-engine
```

---

## Category B

SAAS

Questions:

```text
How are users managed?

How are credentials stored?

How are permissions enforced?

How is onboarding implemented?
```

Repository:

```text
universal-pudo-saas
```

---

## Category C

CONTRACT

Questions:

```text
How does the SaaS discover carriers?

How does the SaaS activate carriers?

How does the SaaS consume capabilities?

How does version compatibility work?
```

Repository:

```text
Consumer repository

Current example:
universal-pudo-saas
```

---

# Modification Decision Matrix

Question:

```text
Add new carrier integration
```

Repository:

```text
universal-pudo-engine
```

---

Question:

```text
Add carrier activation screen
```

Repository:

```text
universal-pudo-saas
```

---

Question:

```text
Define carrier activation workflow
```

Repository:

```text
docs/ecosystem
```

---

Question:

```text
Add new carrier capability
```

Repository:

```text
universal-pudo-engine
```

---

Question:

```text
Display carrier capability in UI
```

Repository:

```text
universal-pudo-saas
```

---

Question:

```text
Define capability exposure contract
```

Repository:

```text
docs/ecosystem
```

---

# Repository Navigation Rule

At the start of every architectural discussion, identify the active scope.

Example:

```text
[REPOSITORY ACTIF]
universal-pudo-engine
```

or

```text
[REPOSITORY ACTIF]
universal-pudo-saas
```

or

```text
[SUJET]
CONTRACT
```

No recommendation should be made without identifying the active scope first.

---

# Long-Term Ecosystem Governance

As new repositories appear:

```text
WooCommerce

Prestashop

Python SDK

TypeScript SDK

Mobile SDK
```

each repository owns:

```text
its implementation

its contract documentation

its integration rules
```

The Engine remains implementation-focused.

Consumers remain consumption-focused.

Contracts remain consumer-owned.

---

# Golden Rule

When uncertainty exists:

```text
Engine
    owns carrier functionality

Consumer
    owns user experience

Contract
    belongs to the consumer
```

This rule takes precedence over all other ecosystem discussions.

---

# Decision Summary

Universal PUDO Engine and Universal PUDO SaaS are independent repositories with independent responsibilities.

Contract documentation belongs to the consuming repository.

The purpose of this ownership model is to prevent architectural confusion, preserve repository autonomy, and support future ecosystem growth.
