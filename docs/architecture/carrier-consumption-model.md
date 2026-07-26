# Carrier Consumption Model

Version: 1.0

Status: Accepted

Last Updated: 2026-07-26

Location:

docs/architecture/carrier-consumption-model.md

Related Documents:

- docs/ecosystem/engine-saas-contract.md
- docs/ecosystem/saas-consumption-plan.md
- docs/ecosystem/repository-ownership.md

---

# Purpose

This document defines how Universal PUDO SaaS consumes carrier information managed by Universal PUDO Engine.

The objective is to establish a clear separation between:

- carrier functionality
- carrier configuration

while keeping the Engine as the single source of truth for carriers.

---

# Architectural Principle

The Engine owns carriers.

The SaaS owns carrier usage.

The SaaS never creates carrier definitions.

The SaaS only creates carrier configurations that reference Engine carriers.

---

# Ownership Model

## Engine Owns

Repository:

```text
universal-pudo-engine
```

Concepts:

```text
Carrier

CarrierCapability

CarrierLifecycle

ProviderFactory
```

Responsibilities:

```text
Carrier catalogue

Carrier metadata

Carrier capabilities

Carrier lifecycle

Carrier implementations

Carrier search

Provider execution
```

The Engine is the source of truth.

---

## SaaS Owns

Repository:

```text
universal-pudo-saas
```

Concepts:

```text
CarrierAccount

CarrierCredential
```

Responsibilities:

```text
Customer configuration

Carrier activation

Credential storage

Account management

Administration
```

The SaaS is not responsible for carrier implementation.

---

# Current CarrierAccount Model

Current implementation:

```python
class CarrierAccount:
    organisation_id
    carrier_code
    name
    is_active
```

Meaning:

```text
A CarrierAccount represents
an organisation-specific configuration
of an Engine carrier.
```

Example:

Carrier:

```text
colissimo
```

CarrierAccount:

```text
carrier_code = "colissimo"

name = "My Production Colissimo Account"
```

---

# Carrier Reference Strategy

The reference between SaaS and Engine is:

```text
carrier_code
```

Current examples:

```text
colissimo

chronopost

mondial_relay
```

The SaaS stores only the carrier code.

The carrier metadata remains owned by the Engine.

---

# Relationship Model

## Carrier

Owned by:

```text
Engine
```

Represents:

```text
A transport carrier available
inside Universal PUDO Engine.
```

---

## CarrierAccount

Owned by:

```text
SaaS
```

Represents:

```text
An organisation-specific configuration
of a carrier.
```

Relationship:

```text
Carrier
    ↓
0..N
CarrierAccount
```

Example:

```text
Carrier

Colissimo
```

may have:

```text
CarrierAccount

Organisation A
    Colissimo Production

Organisation B
    Colissimo France

Organisation C
    Colissimo Export
```

---

## CarrierCredential

Owned by:

```text
SaaS
```

Represents:

```text
Authentication information
required to use a CarrierAccount.
```

Relationship:

```text
Carrier
    ↓
CarrierAccount
    ↓
CarrierCredential
```

---

# Conceptual Flow

```text
Engine

Carrier
│
├── code
├── name
├── lifecycle
└── capabilities

        ↓ reference

SaaS

CarrierAccount
│
├── organisation_id
├── carrier_code
├── name
└── is_active

        ↓

CarrierCredential
│
├── username
├── password
├── token
└── configuration
```

---

# Carrier Discovery

The Engine remains responsible for carrier discovery.

The SaaS consumes the Engine catalogue.

Recommended flow:

```text
Engine

Carrier Catalogue
        ↓
GET /carriers
        ↓
Carrier
        ↓
SaaS Administration UI
```

The SaaS must not:

```text
Scan providers

Discover carriers itself

Build a separate carrier catalogue

Duplicate carrier metadata
```

---

# Carrier Lifecycle Consumption

The SaaS consumes CarrierLifecycle.

Supported lifecycle values:

```text
ACTIVE

DEPRECATED

UNLISTED

SUNSET

REMOVED
```

Recommended behavior:

ACTIVE

```text
Visible
Activatable
```

DEPRECATED

```text
Visible
Activatable
Warning displayed
```

UNLISTED

```text
Hidden from standard activation
```

SUNSET

```text
Visible
Warning displayed
Migration expected
```

REMOVED

```text
Not activatable
```

The Engine remains the authority on lifecycle values.

---

# Carrier Capability Consumption

The SaaS consumes CarrierCapability.

Examples:

```text
SEARCH_PICKUP_POINTS

GET_PICKUP_DETAILS

RESOLVE_PICKUP_POINT
```

Capabilities may be used by the SaaS for:

```text
Feature visibility

Activation checks

Future onboarding assistance

User guidance
```

The SaaS must not define its own capability catalogue.

---

# Carrier Activation Workflow

Recommended workflow:

```text
Organisation Owner
        ↓
Select Carrier
        ↓
CarrierAccount Created
        ↓
Credentials Configured
        ↓
CarrierAccount Activated
```

The SaaS activates access to carriers.

The SaaS does not create carriers.

---

# Design Rules

Rule 1

```text
The Engine owns carriers.
```

---

Rule 2

```text
The SaaS owns carrier accounts.
```

---

Rule 3

```text
The SaaS owns credentials.
```

---

Rule 4

```text
CarrierAccount references Carrier
through carrier_code.
```

---

Rule 5

```text
The SaaS never duplicates carrier definitions.
```

---

Rule 6

```text
The SaaS never implements provider logic.
```

---

Rule 7

```text
The Engine remains the single source
of truth for carrier metadata.
```

---

# Current Architecture Validation

Current SaaS implementation:

```text
CarrierAccount
    contains carrier_code
```

Current Engine implementation:

```text
Carrier
    contains code
```

Result:

```text
✅ Compatible

✅ No schema change required

✅ No migration required

✅ Aligned with Engine v1.0.0
```

---

# Decision Summary

Universal PUDO Engine owns carriers.

Universal PUDO SaaS owns carrier accounts and credentials.

CarrierAccount references Engine carriers through carrier_code.

The Engine remains the source of truth for carrier metadata, lifecycle and capabilities.

The SaaS consumes the Engine catalogue and must never duplicate carrier definitions.
