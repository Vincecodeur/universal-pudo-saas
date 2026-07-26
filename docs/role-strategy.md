# Universal PUDO SaaS - Role Strategy

Version: 1.0.0

Status: Approved

Last Updated: 2026-07-25

---

# PURPOSE

This document defines the role strategy used by Universal PUDO SaaS.

The objective is to:

- define supported roles
- define role ownership
- define storage strategy
- avoid unnecessary RBAC complexity
- align access control with the business model

This document must be approved before implementing Roles & Permissions in the database model.

---

# BUSINESS PRINCIPLE

Universal PUDO SaaS is not a generic identity management platform.

The platform exists to allow organisations to:

- connect carrier accounts
- access pickup point information
- search PUDO data
- consume normalized pickup point information

Roles exist only to control access to these capabilities.

The role model must remain simple and business-oriented.

---

# SUPPORTED ROLES

Version 1 supports three roles.

```text
SAAS_ADMIN

OWNER

VIEWER
```

No additional roles are currently planned.

---

# ROLE DEFINITIONS

## SAAS_ADMIN

Scope:

Entire platform

Represents:

Platform operator

Examples:

- platform administrator
- operations team
- support team
- SaaS owner

Responsibilities:

- create organisations
- suspend organisations
- manage subscriptions
- manage quotas
- manage billing
- manage carrier integration catalog
- publish carrier integrations
- expose carrier integrations to Owners
- monitor platform operations

This role exists outside tenant boundaries.

---

## OWNER

Scope:

Single organisation

Represents:

Customer account owner

Examples:

- logistics manager
- transport manager
- IT manager
- business owner

Responsibilities:

- create Viewer users
- disable Viewer users
- remove Viewer users
- connect carrier accounts
- manage carrier credentials
- manage dashboards
- manage API access
- manage organisation settings
- manage organisation analytics

The Owner is responsible for transforming an empty tenant into an operational organisation.

---

## VIEWER

Scope:

Single organisation

Represents:

Operational user

Examples:

- logistics operator
- warehouse user
- customer service user
- transport analyst

Responsibilities:

- search pickup points
- view dashboards
- consume PUDO information
- export search results
- view analytics

Viewer users consume the service but do not administer it.

---

# STORAGE STRATEGY

Official decision:

Store roles directly inside Membership.

The platform will use:

```text
Membership

id

organisation_id

user_id

role
```

Example:

```text
Membership

organisation_id = 1

user_id = 10

role = OWNER
```

---

# REJECTED STRATEGY

The following design is intentionally rejected:

```text
Role Table

roles

permissions

role_permissions

dynamic role assignment
```

Reason:

The platform currently supports only three fixed business roles.

A dynamic RBAC model would introduce complexity without providing business value.

---

# WHY MEMBERSHIP OWNS THE ROLE

The role belongs to the relationship between:

```text
Organisation
↔
User
```

and not to the User itself.

Example:

```text
User A

Organisation X
Role = OWNER

Organisation Y
Role = VIEWER
```

Role assignment is organisation-specific.

Therefore the role naturally belongs to Membership.

---

# PROPOSED ENUM

```text
SAAS_ADMIN

OWNER

VIEWER
```

Database representation may be:

```text
Enum

or

String with validation
```

Final implementation decision will be made during database implementation.

---

# BUSINESS RULES

## Rule 1

Every organisation must have at least one OWNER.

---

## Rule 2

VIEWER users cannot modify platform configuration.

---

## Rule 3

Only OWNER users may manage carrier accounts.

---

## Rule 4

Only OWNER users may manage dashboards.

---

## Rule 5

Only SAAS_ADMIN users may manage the Carrier Integration Catalog.

---

## Rule 6

A user may belong to multiple organisations.

Role assignment is evaluated per organisation.

---

# EXAMPLE

```text
User: John

Organisation A
Role: OWNER

Organisation B
Role: VIEWER
```

Behaviour:

Organisation A:

✅ Manage carrier accounts

✅ Manage dashboards

✅ Manage users

Organisation B:

✅ Search pickup points

✅ View dashboards

❌ Modify configuration

---

# FUTURE EVOLUTION

The following roles may be introduced in future versions:

```text
ORG_ADMIN

API_USER

SERVICE_ACCOUNT

AUDITOR
```

These roles are explicitly out of scope for Version 1.

They must only be introduced after validation through a real business requirement.

---

# ARCHITECTURAL BENEFITS

This approach provides:

✅ Simplicity

✅ Clear ownership

✅ Small database footprint

✅ Simple migrations

✅ Simple testing

✅ Easy documentation

✅ Future extensibility

---

# SUCCESS CRITERIA

The role strategy is considered implemented when:

✅ Membership contains a role field

✅ Supported roles are enforced

✅ Ownership rules are enforced

✅ Automated tests validate permissions

✅ Documentation remains synchronized

---

# CHANGE HISTORY

2026-07-25

Initial role strategy created.

Validated roles:

- SAAS_ADMIN
- OWNER
- VIEWER

Validated storage strategy:

Membership.role

Rejected strategy:

- Role table
- Dynamic RBAC

Role ownership confirmed as organisation-specific.
