# Universal PUDO SaaS - Carrier Integration Model

Version: 2.0.0

Status: Updated After Universal PUDO Engine Integration

Last Updated: 2026-07-27

---

# PURPOSE

This document defines how Universal PUDO SaaS consumes carrier capabilities.

The objective is to clearly separate:

- carrier catalog ownership
- carrier account ownership
- carrier credential ownership
- Engine responsibilities
- SaaS responsibilities
- organisation responsibilities

This document replaces the previous SaaS-owned CarrierIntegration model.

The current architecture follows the final Phase 15 ownership decision:

Universal PUDO Engine owns the carrier catalog.

Universal PUDO SaaS owns carrier accounts and carrier credentials.

Universal PUDO SaaS does not persist carrier definitions.

---

# BUSINESS VISION

Universal PUDO SaaS allows organisations to consume pickup point data from multiple carriers.

Organisations do not directly manage carrier integrations.

Organisations connect carrier accounts that reference carriers exposed by Universal PUDO Engine.

The business model is based on three distinct concepts:

1. Engine Carrier Catalog
2. Carrier Account
3. Carrier Credential

These concepts must never be merged.

---

# FINAL OWNERSHIP MODEL

## Universal PUDO Engine Owns

Universal PUDO Engine owns:

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
- hybrid search
- carrier metadata
- carrier catalog implementation

Universal PUDO Engine is the single source of truth for carrier functionality.

---

## Universal PUDO SaaS Owns

Universal PUDO SaaS owns:

- organisations
- users
- memberships
- permissions
- carrier accounts
- carrier credentials
- organisation-level carrier activation
- organisation search experience
- multi-carrier search entry point
- future dashboards
- future exports
- future administration
- future frontend

Universal PUDO SaaS consumes Universal PUDO Engine.

Universal PUDO SaaS must never duplicate carrier integration logic.

---

# ENGINE CARRIER CATALOG

## Scope

Universal PUDO Engine

## Owner

Universal PUDO Engine

## Purpose

The Engine Carrier Catalog represents the carrier capabilities exposed by Universal PUDO Engine.

It describes which carriers exist, what their lifecycle state is, and which capabilities they expose.

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- DPD France
- GLS
- UPS
- InPost

## SaaS Consumption

Universal PUDO SaaS consumes the Engine Carrier Catalog through:

```text
engine_catalog/
├── models.py
├── client.py
└── service.py
```

## SaaS Read Model

The SaaS consumes carriers through a SaaS-side read model:

```text
Carrier
CarrierCapability
CarrierLifecycle
```

These models are not SQLAlchemy models.

They are not persisted by the SaaS.

The Engine remains the source of truth.

---

# CARRIER ACCOUNT

## Scope

Organisation

## Owner

Organisation Owner

## Purpose

A Carrier Account represents an organisation-specific connection to a carrier exposed by Universal PUDO Engine.

A Carrier Account belongs to exactly one organisation.

Examples:

```text
Organisation A
├── Colissimo Account
├── Mondial Relay Account
└── Chronopost Account

Organisation B
└── DPD Account
```

## Important Boundary

A Carrier Account does not define the carrier.

A Carrier Account references a carrier through:

```text
carrier_code
```

The value maps to:

```text
Engine Carrier.code
```

The SaaS does not persist carrier metadata.

---

# CARRIER ACCOUNT RESPONSIBILITIES

The Organisation Owner is responsible for:

- creating carrier accounts
- configuring carrier credentials
- updating carrier credentials
- enabling carrier accounts
- disabling carrier accounts
- managing organisation-specific carrier access

Allowed examples:

```text
✅ Configure Colissimo credentials
✅ Configure Mondial Relay credentials
✅ Enable a carrier account
✅ Disable a carrier account
```

Not allowed examples:

```text
❌ Create a carrier integration
❌ Modify Engine carrier metadata
❌ Publish a carrier globally
❌ Add carrier capabilities
❌ Implement carrier-specific provider logic
```

---

# CARRIER ACCOUNT ENTITY

Implemented entity:

```text
CarrierAccount
```

Implemented fields:

```text
id
organisation_id
carrier_code
name
is_active
created_at
updated_at
```

Ownership:

```text
Organisation
    1
    │
    ▼
CarrierAccount
    N
```

Status:

```text
Implemented
Persisted
Validated
Tested
```

---

# CARRIER CREDENTIAL

## Scope

Organisation Carrier Account

## Owner

Organisation Owner

## Purpose

A Carrier Credential stores authentication configuration attached to a Carrier Account.

Implemented entity:

```text
CarrierCredential
```

Implemented fields:

```text
id
carrier_account_id
credential_key
credential_value
created_at
updated_at
```

Ownership:

```text
CarrierAccount
    1
    │
    ▼
CarrierCredential
    N
```

Status:

```text
Implemented
Persisted
Validated
Tested
```

---

# CARRIER CREDENTIAL RESPONSIBILITIES

The SaaS stores organisation-owned credentials.

The Engine consumes credentials when required for carrier execution.

Current rules:

```text
✅ Credentials belong to an organisation
✅ Credentials belong to a carrier account
✅ Credentials are never stored in the Engine Carrier Catalog
✅ Credentials are never stored in the Engine carrier metadata
```

Future rule:

```text
Credential encryption must be implemented before production usage.
```

---

# ORGANISATION CARRIER CATALOG

Universal PUDO SaaS exposes organisation-specific carrier views through:

```text
carrier_catalog/service.py
```

Implemented service:

```text
CarrierCatalogService
```

Implemented responsibilities:

```text
list_available_carriers()
list_organisation_carriers()
list_activatable_carriers_for_organisation()
```

The service crosses:

```text
Engine Carrier.code
```

with:

```text
CarrierAccount.carrier_code
```

This allows the SaaS to expose:

- available carriers
- organisation-linked carriers
- activatable carriers

without persisting carrier definitions.

---

# SEARCH CONSUMPTION MODEL

Universal PUDO SaaS consumes pickup point search through:

```text
engine_search/
├── models.py
├── client.py
└── service.py
```

Implemented service:

```text
EngineSearchService
```

Implemented responsibilities:

```text
search_pickup_points()
search_pickup_points_by_radius()
get_pickup_point()
list_carrier_pickup_points()
```

The SaaS consumes Engine search capabilities.

The SaaS does not reimplement Engine search use cases.

---

# ORGANISATION SEARCH MODEL

Implemented service:

```text
OrganisationSearchService
```

Location:

```text
organisation_search/service.py
```

Purpose:

```text
Allow an organisation to search pickup points only through its linked carrier accounts.
```

Architecture:

```text
OrganisationSearchService
        ↓
CarrierCatalogService
        ↓
EngineSearchService
```

Responsibilities:

```text
✅ Use organisation carriers
✅ Use CarrierCatalogService
✅ Use EngineSearchService
✅ Return PickupPoint results
✅ Avoid search persistence
✅ Avoid Engine modification
```

---

# MULTI-CARRIER SEARCH MODEL

Implemented service:

```text
MultiCarrierSearchService
```

Location:

```text
multi_carrier_search/service.py
```

Purpose:

```text
Provide a dedicated SaaS search entry point for future Search Platform features.
```

Architecture:

```text
MultiCarrierSearchService
        ↓
OrganisationSearchService
        ↓
CarrierCatalogService
        ↓
EngineSearchService
        ↓
Universal PUDO Engine
```

Responsibilities:

```text
✅ Expose a dedicated SaaS multi-carrier search boundary
✅ Use OrganisationSearchService
✅ Return PickupPoint results
✅ Prepare Search Platform
```

Out of scope:

```text
❌ Search persistence
❌ Search history
❌ Advanced ranking
❌ Distance calculation
❌ Provider timeout handling
❌ Parallel execution
❌ Cache
```

---

# FINAL RELATIONSHIP MODEL

```text
Universal PUDO Engine
│
├── Carrier Catalog
│
├── Provider Implementations
│
└── Pickup Point Search
        ▲
        │
EngineSearchService
        ▲
        │
CarrierCatalogService
        ▲
        │
OrganisationSearchService
        ▲
        │
MultiCarrierSearchService
        ▲
        │
Search Platform
```

Organisation ownership:

```text
Organisation
│
├── CarrierAccount
│       │
│       └── CarrierCredential
│
└── Future Search Platform
```

Carrier mapping:

```text
CarrierAccount.carrier_code
        ↓
Engine Carrier.code
```

---

# AVAILABILITY WORKFLOW

## Step 1

Universal PUDO Engine exposes carriers through its carrier catalog.

Example:

```text
Colissimo
Mondial Relay
Chronopost
```

## Step 2

Universal PUDO SaaS consumes the Engine carrier catalog.

Example:

```text
CarrierCatalogService.list_available_carriers()
```

## Step 3

An Organisation Owner connects a carrier account.

Example:

```text
Organisation A
Connect Colissimo
Store carrier_code = COLISSIMO
```

## Step 4

The organisation can search pickup points through activated carriers.

Example:

```text
Organisation A
├── Colissimo account
└── Mondial Relay account
```

The search uses:

```text
MultiCarrierSearchService
```

which uses:

```text
OrganisationSearchService
```

---

# ARCHITECTURAL RULES

## Rule 1

Universal PUDO Engine owns carrier integrations.

## Rule 2

Universal PUDO SaaS does not persist carrier definitions.

## Rule 3

Universal PUDO SaaS references carriers through `carrier_code`.

## Rule 4

Universal PUDO SaaS owns carrier accounts.

## Rule 5

Universal PUDO SaaS owns carrier credentials.

## Rule 6

Carrier credentials must never be stored in the Engine Carrier Catalog.

## Rule 7

Universal PUDO SaaS must only model carrier concepts required for:

- pickup point access
- pickup point search
- pickup point visualization
- pickup point analytics
- pickup point consumption
- pickup point export

## Rule 8

Universal PUDO SaaS must not evolve into:

- an OMS
- a WMS
- a TMS
- a shipping platform
- a carrier execution platform

---

# OUTDATED MODEL REPLACED

The previous model introduced:

```text
CarrierIntegration
```

as a SaaS-owned platform entity.

This is no longer the target model.

Final decision:

```text
Carrier catalog belongs to Universal PUDO Engine.

Carrier accounts belong to Universal PUDO SaaS.

Carrier definitions are not persisted by Universal PUDO SaaS.
```

The SaaS may expose carrier availability views, but these views are derived from the Engine Carrier Catalog.

---

# SUCCESS CRITERIA

The carrier integration model is considered implemented when:

```text
✅ Universal PUDO Engine owns carrier catalog
✅ Universal PUDO SaaS does not persist carrier definitions
✅ CarrierAccount exists
✅ CarrierCredential exists
✅ CarrierAccount references Engine carrier through carrier_code
✅ CarrierCatalogService lists available carriers
✅ CarrierCatalogService lists organisation carriers
✅ OrganisationSearchService searches through organisation carriers
✅ MultiCarrierSearchService provides a SaaS search boundary
✅ Tests validate the model
✅ Documentation remains synchronized
```

Current status:

```text
Implemented through Phase 15.
```

---

# CHANGE HISTORY

2026-07-25

Initial Carrier Integration Model created.

The initial model separated:

- Carrier Integration
- Carrier Account

---

2026-07-27

Carrier Integration Model updated after Universal PUDO Engine Integration.

Updated decisions:

- Universal PUDO Engine owns carrier catalog
- Universal PUDO SaaS does not persist carrier definitions
- Universal PUDO SaaS owns CarrierAccount
- Universal PUDO SaaS owns CarrierCredential
- CarrierAccount references Engine carriers through carrier_code
- CarrierIntegration is no longer the active SaaS implementation model
- MultiCarrierSearchService becomes the SaaS search entry point

Validated through Phase 15.
