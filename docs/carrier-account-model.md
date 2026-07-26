# Carrier Account Model

Version: 1.0

Status: Draft

Last Updated: 2026-07-25

---

# Purpose

This document defines the business model for carrier account management within Universal PUDO SaaS.

It establishes the responsibilities and ownership boundaries between:

- Universal PUDO SaaS
- Universal PUDO Engine
- Organisations
- Carrier Integrations
- Carrier Accounts
- Carrier Credentials

---

# Architectural Principle

Universal PUDO SaaS owns:

- Organisation management
- Carrier account management
- Carrier credential management
- User access management

Universal PUDO Engine owns:

- Carrier implementations
- API adapters
- Search orchestration
- Pickup point normalization
- Carrier business intelligence

The SaaS configures carriers.

The Engine executes carriers.

---

# Core Concepts

## Organisation

A tenant using Universal PUDO SaaS.

Examples:

- Acme Logistics
- Global Fulfillment
- Demo Organisation

Responsibilities:

- Own users
- Own memberships
- Own carrier accounts

Cardinality:

Organisation
→ 0..N Carrier Accounts

---

## Carrier Catalog

The carrier catalog is owned by Universal PUDO Engine.

Examples:

- mondialrelay
- colissimo
- chronopost
- ups
- dhl

Characteristics:

- Global catalog
- Shared across all organisations
- Owned by Universal PUDO Engine
- Not persisted by Universal PUDO SaaS

Universal PUDO SaaS consumes this catalog but does not store it.

---

## Carrier Account

A configuration owned by an organisation.

A carrier account represents the relationship between:

- one organisation
- one carrier code exposed by Universal PUDO Engine

Examples:

Organisation:
Acme Logistics

Carrier Code:
mondialrelay

Carrier Account:
Mondial Relay Sandbox

---

Organisation:
Acme Logistics

Carrier Code:
mondialrelay

Carrier Account:
Mondial Relay Sandbox

---

Characteristics:

- Belongs to one organisation
- References one carrier_code
- Contains operational settings
- References credentials

Cardinality:

Organisation
→ 0..N Carrier Accounts

Carrier Account
→ 1 Carrier Code

Carrier Code
→ 0..N Carrier Accounts

---

## Carrier Credentials

Secrets required to authenticate with a carrier.

Examples:

- API Key
- API Secret
- Username
- Password
- Account Number

Carrier credentials belong to a single Carrier Account.

Credentials are stored by the SaaS.

Credentials are consumed by the Engine.

---

# Ownership Model

Organisation
|
+-- Carrier Account
--- |
--- +-- Carrier Credentials

Universal PUDO Engine
|
+-- Carrier Catalog
|
+-- Referenced By Carrier Accounts

Universal PUDO Engine
|
+-- Consumes Carrier Credentials
|
+-- Executes Carrier API Calls

---

# Business Rules

## Rule 1

A Carrier Account must belong to exactly one Organisation.

---

## Rule 2

A Carrier Account must reference exactly one carrier_code exposed by Universal PUDO Engine.

---

## Rule 3

Multiple Carrier Accounts may reference the same carrier_code.

Example:

Acme → Mondial Relay Production

Acme → Mondial Relay Sandbox

Both accounts use:

mondialrelay

---

## Rule 4

Carrier Credentials may never be stored inside Universal PUDO Engine.

They are owned by Universal PUDO SaaS.

---

## Rule 5

Removing an Organisation removes ownership of Carrier Accounts.

Deletion strategy will be defined later.

---

## Rule 6

The Carrier Catalog is owned by Universal PUDO Engine.

Organisations cannot create carrier definitions.

Universal PUDO SaaS only activates and configures carriers exposed by the Engine.

---

## Rule 7

A carrier supported by Universal PUDO Engine is not automatically available to an Organisation.

The Organisation must explicitly activate and configure a Carrier Account before the carrier can be used.

---

# Future Extensions

Not part of Phase 14.1:

- Credential encryption
- Credential rotation
- Secret vault integration
- Connectivity testing workflows
- Audit logging
- Webhook management

These will be handled in future phases.

---

# Success Criteria

Carrier Account Design Foundation is complete when:

- Organisation ownership is defined
- Carrier Catalog role is defined
- Carrier Account role is defined
- Carrier Credential role is defined
- Boundaries between SaaS and Engine are defined
- Business rules are approved
