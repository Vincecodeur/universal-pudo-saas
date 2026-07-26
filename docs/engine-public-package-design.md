# Engine Public Package Design

Version: 1.0

Status: Draft

Last Updated: 2026-07-26

Related Documents:

- ADR-0007 Carrier Catalog Ownership
- ADR-0008 Public Engine Contract
- public-engine-contract.md

---

# Purpose

This document defines the public package architecture of Universal PUDO Engine.

The objective is to establish a stable and reusable contract that can be consumed by:

- Universal PUDO SaaS
- Engine APIs
- Shopify Plugins
- WooCommerce Plugins
- Future Products
- Internal Tools

while preserving a strict separation between:

```text
Public Contract

and

Internal Engine Implementation
```

---

# Design Principles

## Single Source of Truth

Carrier definitions exist only inside Universal PUDO Engine.

The Engine remains responsible for:

- carrier catalog
- carrier metadata
- carrier capabilities
- carrier implementations

No consumer is allowed to maintain its own carrier catalog.

---

## Public Contract First

Consumers must access Engine functionality exclusively through the public package.

Allowed:

```python
from universal_pudo_engine.public import ...
```

Not Allowed:

```python
from universal_pudo_engine.providers import ...
```

```python
from universal_pudo_engine.carriers import ...
```

```python
from universal_pudo_engine.services import ...
```

---

## Internal Refactoring Freedom

The Engine team must be able to:

- rename internal modules
- move implementations
- reorganize providers
- refactor services

without breaking consumers.

The public package acts as the stability layer.

---

# Target Package Structure

```text
universal-pudo-engine/

src/
└── universal_pudo_engine/

    ├── carriers/
    │
    ├── providers/
    │
    ├── services/
    │
    ├── normalization/
    │
    ├── search/
    │
    └── public/
        ├── __init__.py
        ├── models.py
        ├── catalog.py
        ├── search.py
        └── capabilities.py
```

---

# Package Responsibilities

## carriers/

Purpose:

```text
Carrier registrations

Carrier metadata

Carrier configuration
```

Visibility:

```text
Internal
```

---

## providers/

Purpose:

```text
Carrier-specific implementations
```

Examples:

```text
Mondial Relay

Colissimo

Chronopost

DPD

UPS
```

Visibility:

```text
Internal
```

---

## services/

Purpose:

```text
Business orchestration
```

Examples:

```text
Search orchestration

Validation

Normalization workflows
```

Visibility:

```text
Internal
```

---

## normalization/

Purpose:

```text
Standardization of carrier responses
```

Visibility:

```text
Internal
```

---

## search/

Purpose:

```text
Pickup point search workflows
```

Visibility:

```text
Internal
```

---

# Public Package

Only the following package is considered public:

```text
universal_pudo_engine.public
```

Consumers must depend exclusively on this package.

---

# public.models

Purpose:

Expose stable public domain models.

Example:

```python
CarrierDefinition
```

Initial structure:

```python
CarrierDefinition(
    carrier_code: str,
    carrier_name: str,
    countries: list[str],
    services: list[str],
    capabilities: list[str],
)
```

This model represents the public definition of a carrier.

---

# public.catalog

Purpose:

Provide carrier catalog discovery functions.

---

## get_available_carriers()

Returns:

```python
list[CarrierDefinition]
```

Example:

```python
carriers = get_available_carriers()
```

Purpose:

```text
Discover all carriers available in the Engine.
```

---

## get_carrier_definition()

Signature:

```python
get_carrier_definition(
    carrier_code: str,
)
```

Returns:

```python
CarrierDefinition | None
```

Example:

```python
carrier = get_carrier_definition(
    "mondialrelay"
)
```

Purpose:

```text
Retrieve a single carrier definition.
```

---

# public.search

Purpose:

Expose future search capabilities.

Planned functions:

```python
search_pickup_points()
```

Status:

```text
Reserved for future phases.
```

---

# public.capabilities

Purpose:

Expose capability-related metadata.

Examples:

```python
supports_tracking()

supports_labels()

supports_pudo_search()
```

Status:

```text
Reserved for future phases.
```

---

# Public Contract Rules

## Rule 1

Consumers may import only:

```text
universal_pudo_engine.public
```

---

## Rule 2

Consumers must never import:

```text
providers/*
```

---

## Rule 3

Consumers must never import:

```text
services/*
```

---

## Rule 4

Consumers must never import:

```text
normalization/*
```

---

## Rule 5

Consumers must never import:

```text
search/*
```

unless explicitly re-exported through the public package.

---

# Carrier Discovery Workflow

Adding a carrier follows the same process regardless of consumer count.

Example:

```text
Developer adds:

DPD South Africa
```

Workflow:

```text
1. Implement carrier

2. Register carrier

3. Publish carrier through public catalog

4. Consumers automatically discover carrier
```

Consumers requiring no modification:

```text
Universal PUDO SaaS

Engine APIs

Shopify Plugins

WooCommerce Plugins

Future Applications
```

---

# SaaS Integration Strategy

Universal PUDO SaaS consumes:

```python
get_available_carriers()

get_carrier_definition()
```

Universal PUDO SaaS stores:

```text
CarrierAccount

CarrierCredential
```

Universal PUDO SaaS does not store:

```text
Carrier

CarrierDefinition

CarrierCatalog
```

This preserves ADR-0007 ownership boundaries.

---

# Versioning Strategy

The public package is versioned.

Compatible changes:

```text
Adding new carriers

Adding new optional fields

Adding new public functions
```

Breaking changes:

```text
Removing public functions

Renaming public functions

Removing public fields

Changing public return types
```

Breaking changes require a new major version.

---

# Long-Term Ecosystem Vision

```text
                    Universal PUDO Engine
                               │
                               ▼
                     Public Package Contract
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
           ▼                   ▼                   ▼

         SaaS            Engine APIs          Plugins
                                                   │
                                                   ▼
                                          Future Products
```

All consumers share the same source of truth.

No carrier duplication exists.

No consumer depends on Engine internals.

---

# Validation Criteria

The design is considered validated when:

- Public package structure is finalized
- Public modules are identified
- CarrierDefinition is validated
- Discovery functions are validated
- ADR-0008 is approved
- Consumers only depend on public modules

---

# Decision Summary

Universal PUDO Engine exposes a dedicated public package.

All consumers depend exclusively on that package.

Carrier ownership remains inside Universal PUDO Engine.

This design guarantees:

- Single Source of Truth
- Easy Carrier Expansion
- Multi-Consumer Support
- Refactoring Flexibility
- Long-Term Maintainability
- Reusability Across Organizations
