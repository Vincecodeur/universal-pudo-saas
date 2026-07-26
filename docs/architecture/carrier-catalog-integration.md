# Carrier Catalog Integration

Version: 1.0

Status: Accepted

Last Updated: 2026-07-26

Location:

docs/architecture/carrier-catalog-integration.md

Related Documents:

- docs/ecosystem/engine-saas-contract.md
- docs/ecosystem/saas-consumption-plan.md
- docs/architecture/carrier-consumption-model.md

---

# Purpose

This document defines how Universal PUDO SaaS integrates with the carrier catalogue provided by Universal PUDO Engine.

The objective is to ensure that the SaaS consumes carrier information from the Engine without duplicating carrier definitions or carrier metadata.

The Engine remains the source of truth.

The SaaS remains the consumer.

---

# Architectural Principle

The Engine owns the carrier catalogue.

The SaaS consumes the carrier catalogue.

The SaaS never creates carrier definitions.

The SaaS never maintains its own carrier catalogue.

---

# Source Of Truth

Source of truth:

```text
Universal PUDO Engine
```

Engine concepts:

```text
Carrier

CarrierCapability

CarrierLifecycle
```

The Engine is responsible for:

```text
Carrier registration

Carrier metadata

Carrier capabilities

Carrier lifecycle

Carrier visibility
```

The SaaS must trust Engine data.

---

# SaaS Responsibility

The SaaS consumes the Engine carrier catalogue.

The SaaS is responsible for:

```text
Carrier selection

Carrier activation

Carrier account management

Credential management

Administration UI

User experience
```

The SaaS is not responsible for carrier discovery.

---

# Carrier Discovery Strategy

The Engine already provides a carrier catalogue.

Recommended flow:

```text
Universal PUDO Engine
        ↓
Carrier Catalogue
        ↓
GET /carriers
        ↓
Carrier
        ↓
Universal PUDO SaaS
```

Alternative internal Engine flow:

```text
ListCarriersUseCase
        ↓
Carrier
        ↓
Consumer
```

The discovery mechanism remains Engine-owned.

---

# SaaS Carrier Catalogue View

The SaaS may display a carrier catalogue view.

The data displayed must come from the Engine.

Example:

```text
Carrier

Code:
colissimo

Name:
Colissimo

Capabilities:
SEARCH_PICKUP_POINTS

Lifecycle:
ACTIVE
```

The SaaS must not create its own version of this information.

---

# Carrier Selection Workflow

Recommended flow:

```text
Owner opens carrier administration

        ↓

SaaS requests Engine carrier catalogue

        ↓

SaaS displays available carriers

        ↓

Owner selects carrier

        ↓

CarrierAccount created

        ↓

CarrierCredential created

        ↓

Carrier activated for organisation
```

The carrier itself remains Engine-owned.

---

# Carrier Account Relationship

Relationship model:

```text
Engine

Carrier
        ↓
        ↓ 1..N
        ↓
SaaS

CarrierAccount
```

Meaning:

A single Engine carrier can be used by multiple organisations.

Example:

```text
Carrier

Colissimo
```

may be linked to:

```text
Organisation A
    CarrierAccount A

Organisation B
    CarrierAccount B

Organisation C
    CarrierAccount C
```

---

# Carrier Code Mapping

Reference strategy:

```text
carrier_code
```

Current example:

```text
Carrier.code
        ↓
CarrierAccount.carrier_code
```

Example:

```text
Engine

Carrier.code

"colissimo"
```

```text
SaaS

CarrierAccount.carrier_code

"colissimo"
```

No additional mapping layer is required.

---

# Carrier Lifecycle Consumption

The SaaS consumes lifecycle information from the Engine.

Supported values:

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
Display carrier

Allow activation
```

DEPRECATED

```text
Display carrier

Allow activation

Show warning
```

UNLISTED

```text
Hide carrier

Do not promote activation
```

SUNSET

```text
Display warning

Allow migration planning
```

REMOVED

```text
Do not allow activation
```

The Engine remains responsible for determining lifecycle values.

---

# Carrier Capability Consumption

Capabilities are Engine-owned.

Examples:

```text
SEARCH_PICKUP_POINTS

GET_PICKUP_DETAILS

RESOLVE_PICKUP_POINT
```

The SaaS may use capabilities for:

```text
Feature visibility

Capability badges

Activation validation

Future onboarding guidance
```

The SaaS must never create custom capability definitions.

---

# Catalog Synchronisation Strategy

The SaaS does not synchronize carrier definitions into its database.

The SaaS consumes carrier data at runtime.

Carrier definitions remain in the Engine.

The SaaS persists only:

```text
CarrierAccount

CarrierCredential
```

No carrier catalogue replication is required.

---

# Forbidden Patterns

The following approaches are forbidden:

```text
Custom SaaS carrier catalogue

Manual SaaS carrier list

Provider package scanning

Carrier metadata duplication

Carrier capability duplication
```

These patterns would create divergence from the Engine.

---

# Valid Architecture

```text
Universal PUDO Engine

Carrier
CarrierCapability
CarrierLifecycle

        ↓

Carrier Catalogue

        ↓

Universal PUDO SaaS

CarrierAccount
CarrierCredential
Administration
```

The boundary
