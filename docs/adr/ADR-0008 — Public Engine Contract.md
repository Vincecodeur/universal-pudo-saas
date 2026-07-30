# ADR-0008 - Public Engine Contract

Status: Proposed

Date: 2026-07-26

Decision Type: Architecture

---

# Context

Universal PUDO Engine is the source of truth for carrier integrations and carrier definitions.

Universal PUDO SaaS, plugins, APIs, and future applications must consume carrier capabilities without duplicating carrier metadata or integration logic.

ADR-0007 established that:

- Universal PUDO Engine owns the carrier catalog.
- Universal PUDO SaaS must not persist carrier definitions.
- Universal PUDO SaaS references carriers through carrier_code.
- Universal PUDO SaaS owns Carrier Accounts and Carrier Credentials.

One of the core objectives of the project is that adding a new carrier integration should require modifications in a single location only.

Example:

```text
Developer adds:

DPD South Africa

inside Universal PUDO Engine

↓

New carrier becomes available to:

- Universal PUDO SaaS
- Engine APIs
- Shopify Plugins
- WooCommerce Plugins
- Future Applications
```

without duplicating carrier definitions across repositories.

The project is intended to remain reusable by any company and is not currently designed around a commercial SaaS offering.

---

# Problem

Without a defined public contract, consumer applications may start to import internal Engine modules directly.

Example:

```python
from universal_pudo_engine.providers.dpd.provider import ...
```

This creates strong coupling between:

```text
Universal PUDO Engine internals

and

Consumer applications
```

As the Engine evolves, internal refactoring may break consumers.

Examples:

- Module renaming
- Package restructuring
- Class relocation
- API signature changes

This increases maintenance costs and reduces long-term flexibility.

---

# Decision

Universal PUDO Engine shall expose a stable public contract.

All consumers must interact exclusively through this public contract.

Consumers must never depend on internal Engine implementation details.

Examples of consumers:

- Universal PUDO SaaS
- Engine REST API
- Shopify Plugins
- WooCommerce Plugins
- Prestashop Plugins
- CLI Applications
- Internal Tools
- Future Products

---

# Public Contract Principle

Only the dedicated public layer is considered stable and consumable.

Proposed structure:

```text
universal-pudo-engine

├── core/
├── carriers/
├── providers/
├── services/
│
└── public/
```

Consumer applications may import only:

```text
universal_pudo_engine.public
```

Internal modules remain private implementation details.

---

# Public Contract Responsibilities

The public contract exposes Engine capabilities.

Examples:

```python
get_available_carriers()

get_carrier_definition()

search_pickup_points()

validate_credentials()
```

The exact API surface may evolve over time.

The architectural rule remains:

```text
Consumers depend on the public contract.

Consumers do not depend on Engine internals.
```

---

# Carrier Catalog Ownership

Carrier definitions exist only once.

Source of truth:

```text
Universal PUDO Engine
```

Examples of owned information:

- carrier_code
- carrier_name
- provider implementation
- supported services
- supported countries
- feature flags
- capability definitions

Universal PUDO SaaS must not store these definitions.

---

# Expected Workflow

Adding a new carrier:

```text
1. Implement carrier in Engine

2. Register carrier in Engine catalog

3. Expose carrier through Public Contract

4. Consumers automatically discover carrier
```

Consequences:

```text
No SaaS database migration required.

No SaaS carrier catalog update required.

No plugin carrier catalog duplication required.
```

---

# Benefits

## Single Source of Truth

Carrier definitions exist in only one system.

```text
Universal PUDO Engine
```

---

## Consistency

All consumers use the same carrier metadata and capabilities.

---

## Maintainability

Engine internals can evolve without breaking consumers.

---

## Scalability

New consumer applications can be added without creating new catalog ownership.

---

## Reusability

Any company can use Universal PUDO Engine independently of Universal PUDO SaaS.

---

# Consequences

Universal PUDO SaaS consumes carrier metadata through the Public Contract.

Universal PUDO SaaS continues to own:

- CarrierAccount
- CarrierCredential

Universal PUDO SaaS must not own:

- Carrier
- CarrierDefinition
- CarrierCatalog

Carrier ownership remains exclusively inside Universal PUDO Engine.

---

# Relationship With ADR-0007

ADR-0007 defines ownership.

ADR-0008 defines consumption.

```text
ADR-0007
    ↓
Who owns carrier definitions?

Answer:
Universal PUDO Engine

ADR-0008
    ↓
How do consumers access carrier definitions?

Answer:
Through the Public Engine Contract
```

The two ADRs are complementary.

---

# Architectural Rule

All current and future consumers must follow the same access pattern:

```text
Universal PUDO Engine
        │
        ▼
Public Contract
        │
        ├── Universal PUDO SaaS
        ├── Engine APIs
        ├── Shopify Plugins
        ├── WooCommerce Plugins
        ├── CLI Tools
        └── Future Applications
```

No consumer may access Engine internal modules directly.

---

# Future Work

Phase 15 objectives:

- Define first public catalog interface.
- Implement carrier discovery through the Public Contract.
- Validate SaaS → Engine integration.
- Validate automatic carrier visibility across consumers.
- Formalize versioning strategy for the Public Contract.

---

# Decision Summary

Universal PUDO Engine remains the sole owner of carrier definitions.

All consumers must depend on a stable Public Engine Contract rather than Engine internals.

This architecture guarantees:

- Single source of truth
- Easy carrier extensibility
- Reduced coupling
- Long-term maintainability
- Reusability across multiple products and organizations
