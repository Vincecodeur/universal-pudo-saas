# Public Engine Contract

Version: 1.0

Status: Draft

Last Updated: 2026-07-26

Related ADRs:

- ADR-0007 Carrier Catalog Ownership
- ADR-0008 Public Engine Contract

---

# Purpose

This document defines the public contract exposed by Universal PUDO Engine.

The objective is to provide a stable integration surface for all consumers of the Engine while preserving the Engine as the single source of truth for carrier definitions and carrier capabilities.

Consumers must never depend on internal Engine implementation details.

---

# Architectural Principles

## Single Source of Truth

Carrier definitions exist only once.

Owner:

```text
Universal PUDO Engine
```

Carrier definitions must not be duplicated in:

- Universal PUDO SaaS
- APIs
- Plugins
- External applications

---

## Public Contract First

Consumers access carrier information exclusively through the public contract.

Consumers must never import internal modules.

Allowed:

```python
from universal_pudo_engine.public ...
```

Not allowed:

```python
from universal_pudo_engine.providers ...
```

```python
from universal_pudo_engine.internal ...
```

```python
from universal_pudo_engine.services ...
```

---

## Consumer Independence

Any future consumer must use the same contract.

Examples:

- Universal PUDO SaaS
- Engine REST API
- Shopify Plugin
- WooCommerce Plugin
- Prestashop Plugin
- CLI Applications
- Internal Tools
- Future Products

---

# Public Package Structure

Proposed structure:

```text
universal-pudo-engine/

└── public/
    ├── __init__.py
    ├── catalog.py
    ├── models.py
    └── capabilities.py
```

Only this package is considered public.

Everything else remains an internal implementation detail.

---

# Public Domain Model

## CarrierDefinition

CarrierDefinition represents a transport carrier known by the Engine.

Example structure:

```python
CarrierDefinition
```

Properties:

```python
carrier_code: str
carrier_name: str
countries: list[str]
services: list[str]
capabilities: list[str]
```

---

## Example

```python
CarrierDefinition(
    carrier_code="mondialrelay",
    carrier_name="Mondial Relay",
    countries=["FR", "BE", "ES"],
    services=[
        "PUDO",
        "HOME_DELIVERY",
    ],
    capabilities=[
        "SEARCH_PUDO",
        "TRACKING",
        "LABEL",
    ],
)
```

---

# Public Catalog Functions

## get_available_carriers()

Purpose:

Return all carriers registered inside Universal PUDO Engine.

Signature:

```python
get_available_carriers() -> list[CarrierDefinition]
```

Example:

```python
carriers = get_available_carriers()
```

---

## get_carrier_definition()

Purpose:

Return a single carrier definition.

Signature:

```python
get_carrier_definition(
    carrier_code: str,
) -> CarrierDefinition | None
```

Example:

```python
carrier = get_carrier_definition(
    "mondialrelay"
)
```

---

# Ownership Model

The Engine owns:

- carrier catalog
- carrier definitions
- carrier metadata
- carrier capabilities
- provider implementations

The SaaS owns:

- CarrierAccount
- CarrierCredential
- User Management
- Tenant Management
- Authorization

---

# Carrier Discovery Workflow

Adding a new carrier follows this workflow:

```text
1. Implement carrier

2. Register carrier

3. Carrier becomes visible through public contract

4. Consumers discover carrier automatically
```

---

# Example

Developer adds:

```text
DPD South Africa
```

inside Universal PUDO Engine.

Result:

```text
Universal PUDO SaaS
    ✅ can discover carrier

Engine API
    ✅ can discover carrier

Shopify Plugin
    ✅ can discover carrier

WooCommerce Plugin
    ✅ can discover carrier

Future Applications
    ✅ can discover carrier
```

No catalog duplication is required.

---

# Catalog Persistence Rules

Universal PUDO SaaS must not store:

```text
Carrier

CarrierDefinition

CarrierCatalog
```

Universal PUDO SaaS may store:

```text
carrier_code

CarrierAccount

CarrierCredential
```

The carrier catalog remains Engine-owned.

---

# Versioning Rules

Changes to the public contract must be treated as API changes.

Examples:

```text
Adding new fields
    Compatible

Adding new carriers
    Compatible

Removing public functions
    Breaking Change

Renaming public functions
    Breaking Change

Removing public fields
    Breaking Change
```

---

# Long-Term Vision

The public contract becomes the single integration point for the entire ecosystem.

```text
                 Universal PUDO Engine
                         │
                         ▼
                 Public Contract
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
      ▼                  ▼                  ▼
   SaaS             Engine API         Plugins
                                            │
                                            ▼
                                   Future Applications
```

This architecture guarantees:

- Single source of truth
- Easy carrier extensibility
- Reduced coupling
- Reusability
- Long-term maintainability

---

# Phase 15 Scope

Phase 15 validates:

- CarrierDefinition model
- Carrier discovery strategy
- Public package structure
- SaaS consumption strategy

No carrier catalog persistence will be added to the SaaS.

The Engine remains the sole owner of carrier definitions.

---

# Validation Criteria

The Public Engine Contract is considered validated when:

- CarrierDefinition is finalized
- Public package structure is finalized
- Discovery functions are implemented
- SaaS can consume carrier metadata through the public contract
- No carrier duplication exists across repositories
