# Carrier Account ORM Model

Version: 1.0

Status: Draft

Last Updated: 2026-07-25

---

# Purpose

This document defines the future SQLAlchemy ORM implementation for Carrier Account Management.

No implementation is performed at this stage.

This document only defines:

- entities
- fields
- relationships
- constraints
- ownership rules

---

# CarrierAccount

Module

carrier_accounts/models.py

Purpose

Represents an organisation-specific carrier configuration.

Fields

id

UUID

Primary Key

---

organisation_id

UUID

FK → organisations.id

Required

---

carrier_code

String(100)

Required

Must reference a carrier exposed by Universal PUDO Engine.

---

name

String(255)

Required

Examples:

Mondial Relay Production

UPS Sandbox

---

is_active

Boolean

Default:

True

---

created_at

Datetime

---

updated_at

Datetime

---

Relationships

Organisation

→ 0..N CarrierAccounts

Carrier Code

→ 0..N CarrierAccounts

CarrierAccount

→ 0..N CarrierCredentials

---

# CarrierCredential

Module

carrier_credentials/models.py

Purpose

Stores carrier authentication values.

Fields

id

UUID

Primary Key

---

carrier_account_id

UUID

FK → carrier_accounts.id

Required

---

credential_key

String(100)

Required

Examples:

API_KEY

API_SECRET

USERNAME

PASSWORD

ACCOUNT_NUMBER

---

credential_value

Text

Required

---

created_at

Datetime

---

updated_at

Datetime

---

Relationships

CarrierAccount

→ 0..N CarrierCredentials

---

# Relationship Summary

Organisation
|
+----- CarrierAccount
**\_\_\_\_** |
**\_\_\_\_** +----- CarrierCredential

Universal PUDO Engine
|
+----- Carrier Catalog
**\_\_\_\_** |
**\_\_\_\_** +----- referenced by carrier_code

---

# Ownership Rules

Rule 1

Organisation owns CarrierAccount.

---

Rule 2

CarrierAccount owns CarrierCredential.

---

Rule 3

Carrier Catalog is owned by Universal PUDO Engine.

Carrier definitions are not persisted by Universal PUDO SaaS.

---

Rule 4

Universal PUDO Engine never owns credentials.

---

# Unique Constraints

CarrierAccount

No unique constraint initially.

Multiple accounts for the same carrier are allowed.

Examples:

Mondial Relay Production

Mondial Relay Sandbox

---

# Cascade Strategy

Not yet decided.

Will be documented during implementation phase.

Current status:

Undecided

---

# Security Boundary

CarrierCredential stores values.

Encryption is NOT part of this phase.

Encryption belongs to:

Phase 22
Security Hardening

---

# Validation Criteria

ORM Design Foundation is complete when:

- ORM entities identified
- field types identified
- relationships identified
- ownership rules identified
- future implementation structure defined
