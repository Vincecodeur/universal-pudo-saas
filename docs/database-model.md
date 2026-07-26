# Universal PUDO SaaS - Database Model

Version: 2.0.0

Status: Approved

Last Updated: 2026-07-25

---

# PURPOSE

This document defines the persistence model used by Universal PUDO SaaS.

The objective is to describe:

- database entities
- relationships
- ownership boundaries
- database constraints

---

# DATABASE STRATEGY

Database:

```text
universal_pudo_saas
```

Technology:

```text
PostgreSQL 17
SQLAlchemy
Alembic
```

---

# TABLES

Current:

organisations
users
memberships
carrier_accounts
carrier_credentials

Planned:

```text
carrier_integrations
carrier_accounts
dashboard_configurations
api_credentials
search_history
```

---

# ORGANISATIONS

```text
organisations

id UUID PK

name

created_at

updated_at
```

---

# USERS

```text
users

id UUID PK

email

password_hash

is_active

is_verified

last_login_at

created_at

updated_at
```

---

# MEMBERSHIPS

```text
memberships

id UUID PK

organisation_id UUID FK

user_id UUID FK

role

created_at

updated_at
```

---

## Role Strategy

Official decision:

```text
Membership.role
```

Supported values:

```text
OWNER

VIEWER
```

SaaS Administrator remains platform-scoped and is intentionally not stored through organisation memberships.

---

## Constraints

```text
organisation_id + user_id

UNIQUE
```

A user may only have one role per organisation.

---

# CARRIER INTEGRATIONS

```text
carrier_integrations

id UUID PK

code

name

description

documentation_url

is_enabled

created_at

updated_at
```

---

## Ownership

Managed by:

```text
SAAS_ADMIN
```

---

## Examples

```text
COLISSIMO

MONDIAL_RELAY

CHRONOPOST

DPD
```

---

# CARRIER ACCOUNTS

carrier_accounts

id UUID PK

organisation_id UUID FK

carrier_code

name

is_active

created_at

updated_at

deleted_at

---

# CARRIER CREDENTIALS

carrier_credentials

id UUID PK

carrier_account_id UUID FK

credential_key

credential_value

created_at

updated_at

deleted_at

---

## Ownership

Managed by:

```text
OWNER
```

---

## Constraints

```text
Organisation
must exist

Carrier Integration
must exist
```

---

# DASHBOARD CONFIGURATIONS

```text
dashboard_configurations

id UUID PK

organisation_id UUID FK

name

configuration_json

created_at

updated_at
```

---

## Ownership

Managed by:

```text
OWNER
```

---

# API CREDENTIALS

```text
api_credentials

id UUID PK

organisation_id UUID FK

name

credential_hash

status

created_at

updated_at
```

---

## Ownership

Managed by:

```text
OWNER
```

---

# SEARCH HISTORY

```text
search_history

id UUID PK

organisation_id UUID FK

user_id UUID FK

carrier_account_id UUID FK

search_type

search_payload

result_count

created_at
```

---

# ENTITY RELATIONSHIPS

```text
Organisation
│
├── Membership
│       │
│       └── User
│
├── CarrierAccount
│       │
│       └── CarrierIntegration
│
├── DashboardConfiguration
│
├── ApiCredential
│
└── SearchHistory
```

---

# OWNERSHIP MODEL

Platform entities:

```text
carrier_integrations
```

Organisation entities:

```text
memberships

carrier_accounts

dashboard_configurations

api_credentials

search_history
```

---

# ARCHITECTURAL RULES

Rule 1

Carrier Integration and Carrier Account must remain separate entities.

---

Rule 2

Customer credentials must never be stored inside Carrier Integration.

---

Rule 3

Role ownership belongs to Membership.

---

Rule 4

Every Carrier Account belongs to exactly one Organisation.

---

Rule 5

Universal PUDO SaaS stores only concepts necessary for PUDO data access and consumption.

---

Rule 6

Universal PUDO SaaS does not persist carrier definitions.

Carrier definitions are owned by Universal PUDO Engine.

Universal PUDO SaaS stores carrier_code as a logical reference to the Engine carrier catalog.

---

# SUCCESS CRITERIA

The database model is considered valid when:

✅ Membership.role is implemented

✅ Carrier Integration exists

✅ Carrier Account exists

✅ Ownership boundaries are enforced

✅ PostgreSQL constraints are validated

✅ Documentation remains synchronized
