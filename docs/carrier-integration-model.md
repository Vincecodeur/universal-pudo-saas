# Universal PUDO SaaS - Carrier Integration Model

Version: 1.0.0

Status: Approved

Last Updated: 2026-07-25

---

# PURPOSE

This document defines the carrier integration model used by Universal PUDO SaaS.

The objective is to clearly separate:

- carrier integrations available on the platform
- carrier accounts configured by customers
- platform responsibilities
- organisation responsibilities

This separation is required to support multi-tenancy, future scalability, and clean ownership boundaries.

---

# BUSINESS VISION

Universal PUDO SaaS allows organisations to consume pickup point data from multiple carriers.

A carrier integration must be available on the platform before an organisation can connect its own carrier account.

This creates two distinct business concepts:

1. Carrier Integration
2. Carrier Account

These concepts must never be merged.

---

# CARRIER INTEGRATION

Scope:

Platform

Owner:

SaaS Administrator

Purpose:

Represents a carrier integration available within Universal PUDO SaaS.

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- DPD France
- DPD South Africa
- GLS
- UPS

A Carrier Integration defines:

- supported carrier
- supported API version
- capabilities
- documentation
- availability status

It does not contain customer credentials.

---

# CARRIER INTEGRATION RESPONSIBILITIES

The SaaS Administrator is responsible for:

- publishing integrations
- disabling integrations
- maintaining integrations
- exposing integrations to tenants
- controlling platform availability

Examples:

✅ Enable Colissimo integration

✅ Disable DPD South Africa integration

✅ Publish new GLS integration

✅ Upgrade Mondial Relay connector

Examples not allowed:

❌ Configure customer credentials

❌ Configure customer account numbers

❌ Configure tenant-specific settings

---

# CARRIER INTEGRATION ENTITY

Proposed entity:

CarrierIntegration

Fields:

```text
id

code

name

description

provider

engine_provider

documentation_url

status

is_enabled

created_at

updated_at
```

Example:

```text
id: 1

code: COLISSIMO

name: Colissimo

provider: La Poste

is_enabled: true
```

---

# CARRIER ACCOUNT

Scope:

Organisation

Owner:

Organisation Owner

Purpose:

Represents a customer account connected to an available carrier integration.

A Carrier Account belongs to exactly one organisation.

Examples:

Organisation A

- Colissimo Account
- Mondial Relay Account

Organisation B

- Chronopost Account

Organisation C

- DPD Account

---

# CARRIER ACCOUNT RESPONSIBILITIES

The Owner is responsible for:

- creating carrier accounts
- configuring credentials
- updating credentials
- testing connectivity
- enabling carrier accounts
- disabling carrier accounts

Examples:

✅ Configure Colissimo API credentials

✅ Configure Mondial Relay merchant account

✅ Test DPD connectivity

✅ Disable Chronopost account

Examples not allowed:

❌ Publish a new carrier integration

❌ Add a carrier to the SaaS catalog

❌ Make an integration available to other organisations

---

# CARRIER ACCOUNT ENTITY

Proposed entity:

CarrierAccount

Fields:

```text
id

organisation_id

carrier_integration_id

account_name

status

credentials

last_validation_at

created_at

updated_at
```

Example:

```text
Organisation:
Spriiint

Carrier:
Colissimo

Account:
Production Account
```

---

# OWNERSHIP MODEL

Carrier Integration ownership:

SaaS Administrator

```text
Carrier Integration Catalog

COLISSIMO
MONDIAL_RELAY
CHRONOPOST
DPD_FRANCE
```

---

Carrier Account ownership:

Organisation Owner

```text
Organisation

├── Colissimo Account
├── Mondial Relay Account
└── Chronopost Account
```

---

# RELATIONSHIP MODEL

```text
CarrierIntegration

    1
    │
    │
    ▼

CarrierAccount

    N
```

One Carrier Integration may be used by many organisations.

---

Example:

```text
COLISSIMO

├── Spriiint Account
├── PrintChic Account
├── Retailer A Account
└── Retailer B Account
```

---

# AVAILABILITY WORKFLOW

Step 1

SaaS Administrator publishes an integration.

Example:

```text
Colissimo
```

---

Step 2

The integration becomes visible to Owners.

Example:

```text
Available Integrations

✅ Colissimo

✅ Mondial Relay

✅ Chronopost
```

---

Step 3

The Owner connects a carrier account.

Example:

```text
Organisation

Connect Colissimo

Enter API credentials

Save
```

---

Step 4

Viewer users can consume data.

Example:

```text
Search pickup points

Carrier:
Colissimo
```

---

# FUTURE EVOLUTION

Future entities may include:

```text
CarrierCapability

CarrierProduct

CarrierService

CarrierOption

CarrierCoverage
```

Examples:

```text
Saturday Delivery

Hazmat

Signature

Age Verification

Relay Delivery
```

These are not part of the current scope.

---

# ARCHITECTURAL RULES

Rule 1

Carrier Integration and Carrier Account must remain separate entities.

---

Rule 2

Customer credentials must never be stored inside Carrier Integration.

---

Rule 3

Carrier Account must always belong to an Organisation.

---

Rule 4

Only the SaaS Administrator can manage the Carrier Integration Catalog.

---

Rule 5

Only the Organisation Owner can manage Carrier Accounts.

---

Rule 6

Universal PUDO SaaS is a PUDO platform.

The platform must only model carrier concepts required for:

- pickup point access
- pickup point search
- pickup point consumption

Non-PUDO carrier capabilities are out of scope.

---

# SUCCESS CRITERIA

The model is considered implemented when:

✅ Carrier Integration entity exists

✅ Carrier Account entity exists

✅ Ownership boundaries are enforced

✅ SaaS Administrator permissions are enforced

✅ Owner permissions are enforced

✅ Automated tests validate ownership rules

✅ Documentation remains synchronized

---

# CHANGE HISTORY

2026-07-25

Initial Carrier Integration Model created.

Validated business separation:

- Carrier Integration
- Carrier Account

Validated ownership model:

- SaaS Administrator
- Organisation Owner

Carrier Integration Catalog introduced as official platform entity.
