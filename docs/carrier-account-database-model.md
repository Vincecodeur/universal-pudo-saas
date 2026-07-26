# Carrier Account Database Model

Version: 1.0

Status: Draft

Last Updated: 2026-07-25

---

# Purpose

This document defines the persistence model for carrier account management.

The model supports:

- Organisation-owned carrier accounts
- Carrier catalog consumption from Universal PUDO Engine
- Carrier credential storage
- Future carrier connectivity workflows

---

# Entity Overview

Universal PUDO Engine
|
+---- Carrier Catalog
**\_\_** |
**\_\_** +---- referenced by carrier_code
**\_\_** |
**\_\_** +---- CarrierCredential

Universal PUDO Engine
|
+---- Carrier Catalog
**\_** |
**\_** +---- referenced by carrier_code

---

# Table: carrier_accounts

Purpose:

Represents an organisation configuration for a carrier.

Ownership:

Organisation

Fields:

id
UUID
Primary Key

organisation_id
UUID
FK → organisations.id

carrier_code

String(100)

Required

References a carrier exposed by Universal PUDO Engine.

name
String(255)

is_active
Boolean

created_at
Datetime

updated_at
Datetime

---

Business Examples

Mondial Relay Production

Mondial Relay Sandbox

UPS Main Account

DHL Warehouse Account

---

Constraints

FK organisation_id

---

Cardinality

Organisation
→ 0..N Carrier Accounts

Carrier Code
→ 0..N Carrier Accounts

Carrier Account
→ 1 Carrier Code

---

# Table: carrier_credentials

Purpose:

Stores credential key/value pairs attached to a carrier account.

Ownership:

Carrier Account

Fields:

id
UUID
Primary Key

carrier_account_id
UUID
FK → carrier_accounts.id

credential_key
String(100)

credential_value
Text

created_at
Datetime

updated_at
Datetime

---

Business Examples

API_KEY

API_SECRET

ACCOUNT_NUMBER

USERNAME

PASSWORD

---

Constraints

FK carrier_account_id

---

Cardinality

Carrier Account
→ 0..N Credentials

Credential
→ 1 Carrier Account

---

# Relationship Diagram

organisations
|
+---- carrier_accounts
**\_** |
**\_** +---- carrier_credentials

Universal PUDO Engine
|
+---- Carrier Catalog
**\_** |
**\_** +---- referenced by carrier_accounts.carrier_code

---

# Security Boundary

Phase 14:

Credential persistence only.

Not included:

- encryption
- key rotation
- secret vault integration
- HSM integration

These concerns belong to:

Phase 22
Security Hardening

---

# ORM Mapping Strategy

Future SQLAlchemy Models:

carrier_accounts/models.py

carrier_credentials/models.py

---

# Migration Strategy

Migration 1

Create carrier_accounts

Migration 2

Create carrier_credentials

---

# Validation Criteria

Database Design Foundation is complete when:

- carrier catalog reference strategy defined
- carrier_accounts defined
- carrier_credentials defined
- foreign keys defined
- cardinalities defined
- ownership validated
- security boundary documented
