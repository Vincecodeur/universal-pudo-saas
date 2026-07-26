# Universal PUDO SaaS - Domain Model

Version: 2.0.0

Status: Approved

Last Updated: 2026-07-25

---

# PURPOSE

This document defines the business domain model of Universal PUDO SaaS.

The objective is to identify:

- business entities
- ownership boundaries
- relationships
- responsibilities

The model is business-driven and independent from persistence implementation details.

---

# DOMAIN VISION

Universal PUDO SaaS enables organisations to:

- connect carrier accounts
- access pickup point information
- search pickup points
- visualize PUDO information
- consume normalized PUDO data

The platform is organisation-centric.

All business entities belong to an organisation except platform entities managed by the SaaS Administrator.

---

# DOMAIN ENTITIES

The platform currently contains two layers:

1. Platform Layer
2. Organisation Layer

---

# PLATFORM LAYER

Managed by:

SaaS Administrator

Entities:

```text
CarrierIntegration
```

---

## CarrierIntegration

Represents a carrier integration available on the platform.

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- DPD
- GLS
- UPS

Responsibilities:

- identify supported carriers
- expose available integrations
- control platform availability

Owner:

SaaS Administrator

---

# ORGANISATION LAYER

Managed by:

Organisation Owner

Entities:

```text
Organisation

User

Membership

CarrierAccount

DashboardConfiguration

ApiCredential

SearchHistory
```

---

## Organisation

Represents a customer tenant.

Examples:

- Spriiint
- PrintChic
- Retailer ABC

Responsibilities:

- owns users
- owns carrier accounts
- owns dashboards
- owns searches
- owns credentials

---

## User

Represents a platform user.

A User may belong to multiple organisations.

A User has no role by itself.

Roles are organisation-specific.

---

## Membership

Represents the relationship between:

Organisation
↔
User

Responsibilities:

- organisation membership
- access control
- role assignment

Owner:

Organisation

Role values:

```text
OWNER

VIEWER
```

Note:

SAAS_ADMIN exists outside tenant scope.

---

## CarrierAccount

Represents an organisation-owned carrier configuration.

A CarrierAccount references a carrier exposed by Universal PUDO Engine through carrier_code.

Owner:

Organisation

---

## CarrierCredential

Represents credentials attached to a CarrierAccount.

Owner:

CarrierAccount

Security note:

Credential encryption is not part of the current phase.

---

## DashboardConfiguration

Represents dashboard configuration for an organisation.

Responsibilities:

- selected KPIs
- dashboard layout
- reporting preferences

Owner:

Organisation Owner

---

## ApiCredential

Represents organisation API access configuration.

Responsibilities:

- API access
- authentication
- application integration

Owner:

Organisation Owner

---

## SearchHistory

Represents historical PUDO searches.

Responsibilities:

- usage analytics
- auditability
- reporting

Owner:

Organisation

---

# RELATIONSHIP MODEL

```text
CarrierIntegration
        │
        │ 1
        │
        ▼
CarrierAccount
        ▲
        │
        │ N
        │
Organisation
        │
        ├── Membership
        │       │
        │       ▼
        │      User
        │
        ├── DashboardConfiguration
        │
        ├── ApiCredential
        │
        └── SearchHistory
```

---

# ROLE OWNERSHIP

Platform scope:

```text
SAAS_ADMIN
```

Organisation scope:

```text
OWNER

VIEWER
```

Role ownership is managed through Membership.

---

# PRODUCT GUARDRAIL

The domain model must remain focused on:

- pickup point access
- pickup point search
- pickup point consumption

The following concepts are intentionally excluded:

- shipment creation
- labels
- tracking
- carrier services
- transport execution
- TMS functionalities

These concepts belong outside Universal PUDO SaaS.

---

# SUCCESS CRITERIA

The domain model is valid when:

✅ Organisation ownership is clear

✅ Platform ownership is clear

✅ Carrier Integration and Carrier Account remain separate

✅ Membership owns organisation roles

✅ PUDO-focused scope remains enforced
