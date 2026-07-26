# Universal PUDO SaaS - Architecture

Version: 1.2.0

Status: Carrier Repository Foundation Completed

Last Updated: 2026-07-25

---

# PURPOSE

This document defines the target architecture of Universal PUDO SaaS.

The objective is to:

- isolate business responsibilities

- separate SaaS concerns from carrier intelligence

- support multi-tenancy

- support future self-hosted deployments

- preserve long-term maintainability

- keep the product focused on PUDO information access and consumption

This document describes the target architecture, validated implementation decisions, and current architectural direction.

---

# SOLUTION OVERVIEW

Universal PUDO SaaS is a multi-tenant application built on top of Universal PUDO Engine.

Universal PUDO SaaS owns:

- authentication

- organisations

- users

- memberships

- tenant access model

- carrier account management

- dashboard configuration

- exports

- administration

- SaaS-level access control

Universal PUDO Engine owns:

- carrier provider implementations

- pickup point retrieval

- pickup point normalization

- carrier abstraction

- search orchestration

- carrier intelligence related to PUDO search

The SaaS consumes the Core.

The SaaS must never duplicate Core responsibilities.

---

# PRODUCT ARCHITECTURE PRINCIPLE

Universal PUDO SaaS is not a generic logistics platform.

Universal PUDO SaaS exists to provide access to PUDO information.

The platform must remain focused on:

- pickup point access

- pickup point search

- pickup point visualization

- pickup point analytics

- pickup point consumption

- pickup point data export

The following concepts are out of scope unless directly required for PUDO access or PUDO consumption:

- shipment creation

- label generation

- tracking management

- delivery orchestration

- transport rating

- transport execution

- carrier product catalog management

- carrier service catalog management

- non-PUDO carrier capabilities

This rule protects the product from drifting toward a generic OMS, WMS, TMS, or shipping platform.

---

# HIGH LEVEL ARCHITECTURE

+-----------------------------+
| Frontend |
| Next.js |
| React |
+-------------+---------------+
|
v
+-----------------------------+
| FastAPI Backend |
| Universal PUDO SaaS |
+-------------+---------------+
|
v
+-----------------------------+
| PostgreSQL |
| universal_pudo_saas |
+-------------+---------------+
|
v
+-----------------------------+
| Universal PUDO Engine |
| PUDO Carrier Core |
+-------------+---------------+
|
v
+-----------------------------+
| Carrier APIs |
+-----------------------------+

---

# ARCHITECTURAL PRINCIPLES

## P001

Single Responsibility

Each module owns a specific business domain.

---

## P002

Clear Separation

Universal PUDO SaaS manages users, tenants, access, and customer-facing workflows.

Universal PUDO Engine manages carrier-specific PUDO retrieval and normalization.

---

## P003

Independent Databases

Each product owns its own schema and lifecycle.

Universal PUDO SaaS uses:

universal_pudo_saas

Universal PUDO Engine uses:

universal_pudo

---

## P004

Security First

Authentication, tenant access, and credential ownership must be designed before carrier account management.

---

## P005

Documentation Driven Development

Documentation must be synchronized before phase closure.

---

## P006

Product Scope Discipline

The SaaS must only model carrier concepts required for PUDO information access and consumption.

---

# DEPLOYMENT STRATEGY

Current Strategy:

SaaS-first

Future Strategy:

Self-host-ready

Status:

Validated

ADR:

ADR-0006

---

# REPOSITORY STRATEGY

Decision:

Monorepo

Status:

Validated

ADR:

ADR-0001

---

# MULTI-TENANT STRATEGY

Decision:

Tenant = Organisation

Status:

Validated

ADR:

ADR-0004

Relationship:

Organisation

    ▲
    │

Membership
│
▼
User

---

# ACCESS MODEL ARCHITECTURE

The access model is business-driven.

The platform supports three user types in V1:

SAAS_ADMIN

OWNER

VIEWER

---

## SaaS Administrator

Scope:

Platform

Storage Strategy:

users.is_platform_admin

Responsibilities:

- create organisations

- suspend organisations

- manage subscriptions

- manage quotas

- manage billing

- manage platform operations

- carrier account management

- carrier credential management

- make carrier integrations available to organisation Owners

- monitor platform usage

The SaaS Administrator is not scoped to a single organisation.

---

## Owner

Scope:

Organisation

Storage Strategy:

memberships.role = OWNER

Responsibilities:

- create Viewer users

- remove Viewer users

- connect carrier accounts

- configure carrier credentials

- test carrier connectivity

- enable or disable organisation carrier accounts

- configure dashboards

- configure API access

- manage organisation analytics

The Owner uses only carrier integrations made available by the SaaS Administrator.

---

## Viewer

Scope:

Organisation

Storage Strategy:

memberships.role = VIEWER

Responsibilities:

- search pickup points

- view dashboards

- view analytics

- export search results

- consume PUDO data

Viewer users cannot modify tenant configuration.

---

# ROLE STORAGE STRATEGY

Official decision:

SAAS_ADMIN -> users.is_platform_admin

OWNER -> memberships.role

VIEWER -> memberships.role

Rejected strategy:

roles table

permissions table

role_permissions table

dynamic RBAC

Reason:

The product currently needs a simple, business-aligned access model.

The V1 roles are fixed and known in advance.

A dynamic RBAC model would introduce unnecessary complexity.

---

# DOMAIN ARCHITECTURE

Implemented domains:

Organisation

User

Membership

Authentication Model

Authentication Service

Authentication API

User Lookup Foundation

Persistence Test Foundation

Validated product domains:

CarrierAccount

CarrierCredential

Future domains:

Roles & Permissions Enforcement

Carrier Account Management

Search Platform

Exports

Administration

Public API

Frontend

---

# CURRENT DOMAIN MODEL

## Organisation

Purpose:

Business tenant.

Status:

Implemented

Persisted

Persistence Validated

Responsibilities:

- owns memberships

- owns carrier accounts

- owns dashboard configuration

- owns search history

- owns API credentials

---

## User

Purpose:

Platform identity.

Status:

Implemented

Persisted

Authentication Ready

Persistence Validated

Validated fields:

email
first_name
last_name
password_hash
is_active
is_verified
last_login_at

Implemented field:

is_platform_admin

Purpose:
Stores whether a user is a SaaS Administrator.

---

## Membership

Purpose:

Connect users to organisations.

Status:
Implemented

Persisted

Persistence Validated

Current fields:
organisation_id
user_id
role

Role strategy:
OWNER
VIEWER

Membership owns organisation-level role assignment.

---

## CarrierIntegration

Purpose:

Represents a carrier integration available on the SaaS platform.

Scope:

Platform

Owner:

SaaS Administrator

Examples:

COLISSIMO
MONDIAL_RELAY
CHRONOPOST
DPD
GLS
UPS

Responsibilities:

- identify available PUDO carrier integrations

- expose integrations to organisation Owners

- control platform-level carrier availability

Important boundary:

CarrierIntegration must not store customer credentials.

---

## CarrierAccount

Purpose:

Represents an organisation-specific carrier account.

Scope:

Organisation

Owner:

Organisation Owner

Examples:

Spriiint Colissimo account

PrintChic Mondial Relay account

Responsibilities:

- store organisation carrier configuration
- store customer credentials
- test carrier connectivity
- enable or disable carrier usage for the organisation

---

## DashboardConfiguration

Purpose:

Represents dashboard configuration for an organisation.

Scope:

Organisation

Owner:

Organisation Owner

Responsibilities:

- selected KPIs
- displayed charts
- dashboard layout
- reporting preferences

---

## ApiCredential

Purpose:

Represents organisation API access configuration.

Scope:

Organisation

Owner:

Organisation Owner

Responsibilities:

- external API access
- tenant-level API credentials
- future integration access

---

## SearchHistory

Purpose:

Represents historical PUDO searches.

Scope:

Organisation

Owner:

Organisation

Responsibilities:

- usage analytics
- auditability
- reporting
- future operational insights

---

# TARGET DOMAIN RELATIONSHIP MODEL

Target future model:
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

---

# BACKEND ARCHITECTURE

Technology:

FastAPI

Python 3.14

Status:

Validated

Current structure:

src/universal_pudo_saas/
├── auth/
│ ├── **init**.py
│ ├── routes.py
│ ├── schemas.py
│ └── service.py
├── carrier_accounts/
│ ├── models.py
│ └── repository.py
├── carrier_credentials/
│ ├── models.py
│ └── repository.py
├── core/
├── database/
│ ├── base.py
│ ├── metadata.py
│ └── session.py
├── memberships/
│ └── models.py
├── organisations/
│ └── models.py
├── security/
│ ├── passwords.py
│ └── tokens.py
├── shared/
│ └── entities.py
├── users/
│ ├── models.py
│ └── repository.py
└── main.py

Planned structure:

carrier_integrations/

carrier_accounts/

dashboard_configurations/

api_credentials/

search/

roles/

permissions/

exports/

administration/

---

# DATABASE ARCHITECTURE

Technology:

PostgreSQL 17

SQLAlchemy

Alembic

Status:

Validated

Database:

universal_pudo_saas

Current tables:

alembic_version

organisations

users

memberships

carrier_accounts

carrier_credentials

Planned tables:

carrier_integrations

dashboard_configurations

api_credentials

search_history

Planned columns:

memberships.role with values:

- OWNER

- VIEWER

---

# DATABASE OWNERSHIP

## universal_pudo_saas

Owner:

Universal PUDO SaaS

Responsibilities:

- identities

- organisations

- memberships

- tenant access

- carrier accounts

- dashboard configuration

- API credentials

- search history

- administration data

---

## universal_pudo

Owner:

Universal PUDO Engine

Responsibilities:

- carrier provider implementations

- PUDO search execution

- pickup point normalization

- provider-specific carrier logic

---

# TEST ARCHITECTURE

Current test suites:

test_main.py

test_settings.py

test_entities.py

test_organisation.py

test_user.py

test_membership.py

test_passwords.py

test_tokens.py

test_auth_service.py

test_auth_api.py

test_organisation_persistence.py

test_user_persistence.py

test_membership_persistence.py

test_carrier_credential_persistence.py

test_carrier_account_repository.py

test_carrier_credential_repository.py

test_carrier_account.py

test_carrier_account_persistence.py

test_carrier_credential.py

Current result:

77 passed

0 failed

---

# TESTING STRATEGY

## Level 1

Model Tests

Status:

Implemented

---

## Level 2

Persistence Tests

Status:

Implemented

Validated:

session.add()

session.commit()

session.refresh()

session.get()

session.delete()

---

## Level 3

Service Tests

Status:

Implemented

---

## Level 4

API Tests

Status:

Implemented

---

## Level 5

Permission Tests

Status:

Planned

---

## Level 6

Integration Tests

Status:

Planned

---

# PERSISTENCE ARCHITECTURE

Validated operations:

session.add()

session.commit()

session.refresh()

session.get()

session.delete()

Validated persistence layers:

Organisation Persistence

User Persistence

Membership Persistence

CarrierAccount Persistence

CarrierCredential Persistence

CarrierAccount Repository

CarrierCredential Repository

Validated database operations:

PostgreSQL Write

PostgreSQL Read

Entity Retrieval

Entity Deletion

Foreign Key Persistence

---

# SECURITY ARCHITECTURE

Validated dependencies:

passlib 1.7.4

bcrypt 4.3.0

python-jose

cryptography

Current status:

Authentication API Foundation completed.

Implemented:

Password Hashing Service

hash_password()

verify_password()

JWT Service

create_access_token()

decode_access_token()

Authentication Service

authenticate_user()

create_user_token()

Authentication API

POST /auth/login

GET /auth/me

JWT Authentication Flow

User Lookup Foundation

Repository-Based Authentication

Not yet implemented:

Role Enforcement

Permission Enforcement

Refresh Tokens

Password Reset

Email Verification

---

# AUTHENTICATION ARCHITECTURE

security/

├── passwords.py

└── tokens.py

auth/

├── **init**.py

├── schemas.py

├── routes.py

└── service.py

users/

└── repository.py

Endpoints:

POST /auth/login

GET /auth/me

Flow:

Login Request

↓

Repository Lookup

↓

authenticate_user()

↓

create_user_token()

↓

JWT

↓

GET /auth/me

↓

decode_access_token()

↓

CurrentUserResponse

---

# ACCESS CONTROL ARCHITECTURE

Current status:

Documented

Implemented in code:

✅ users.is_platform_admin

✅ memberships.role strategy

Permission enforcement remains planned.

Validated documents:

product-vision.md

access-model.md

permission-matrix.md

carrier-integration-model.md

role-strategy.md

Planned implementation:

users.is_platform_admin

memberships.role

Role values:

OWNER

VIEWER

Platform admin flag:

is_platform_admin

Permission enforcement:

Planned

---

# CARRIER INTEGRATION ARCHITECTURE

The platform separates two concepts:

CarrierIntegration

CarrierAccount

## CarrierIntegration

Scope:

Platform

Owner:

SaaS Administrator

Represents:

A carrier integration available in the SaaS platform.

Status:

Planned

---

## CarrierAccount

Status:

Implemented
Persisted
Persistence Validated

Purpose:

Organisation-specific carrier configuration.

Reference:

carrier_code

Boundary:

Carrier catalog remains owned by Universal PUDO Engine.

---

## CarrierCredential

Status:

Implemented
Persisted
Persistence Validated

Purpose:

Stores carrier authentication values attached to a CarrierAccount.

Security boundary:

Encryption is not part of this phase.

---

# ROADMAP ALIGNMENT

Completed:

Documentation Foundation

Repository Foundation

Architecture Foundation

ADR Foundation

Domain Model Design

Database Model Design

Persistence Decisions

Backend Foundation

Database Configuration Foundation

Alembic Foundation

Organisation Foundation

Users Foundation

Membership Foundation

Authentication Model Foundation

Password Hashing Foundation

JWT Foundation

Authentication Service Foundation

Authentication API Foundation

Persistence Test Foundation

Current:

Carrier Account Management

Carrier Repository Foundation Completed

Carrier Account Service Foundation Planned

Future:

Carrier Account Service Foundation

Carrier Credential Service Foundation

Carrier Account API Foundation

Carrier Credential API Foundation

Permission Enforcement Foundation

Search Platform

Exports

Administration

Public API

Frontend

Search Platform

Exports

Administration

Public API

Frontend

---

# CURRENT STATE

Architecture Status:

Stable

Database Status:

Stable

Authentication Status:

Completed

Persistence Status:

Completed

Access Model Status:

Documented

Role Storage Strategy:

Approved

Testing Status:

77 passed

0 failed

Documentation Status:

In Progress

---

# NEXT ARCHITECTURAL MILESTONE

Carrier Account Service Foundation

Deliverables:

carrier_accounts/service.py

carrier_credentials/service.py

Business validation rules

Service tests

Success Criteria:

Carrier Account service created

Carrier Credential service created

Business validation rules implemented

Service tests passing

Services ready for API layer

No dynamic RBAC tables introduced

Automated tests passing

---

# ARCHITECTURAL DECISIONS

## AD-001

SaaS Administrator storage

Decision:

users.is_platform_admin

Reason:

SaaS Administrator is platform-scoped and not organisation-scoped.

---

## AD-002

Owner and Viewer storage

Decision:

memberships.role

Reason:

Owner and Viewer roles are organisation-specific.

---

## AD-003

No dynamic RBAC for V1

Decision:

No role table, permission table, or role-permission table for V1.

Reason:

The platform currently supports fixed business roles.

---

## AD-004

Carrier Integration and Carrier Account separation

Decision:

CarrierIntegration and CarrierAccount remain separate entities.

Reason:

Platform carrier availability and customer carrier configuration are different business concepts.

---

## AD-005

PUDO scope guardrail

Decision:

The SaaS only models carrier concepts required for PUDO access and consumption.

Reason:

Avoid drifting toward a generic shipping, OMS, WMS, TMS, or carrier capability platform.

---

# CHANGE HISTORY

2026-07-25

Authentication API Foundation completed.

Implemented:

POST /auth/login

GET /auth/me

JWT Authentication Flow

User Lookup Foundation

Repository-Based Authentication

42 automated tests passing.

---

2026-07-25

Persistence Test Foundation completed.

Implemented:

test_organisation_persistence.py

test_user_persistence.py

test_membership_persistence.py

Validated:

session.add()

session.commit()

session.refresh()

session.get()

session.delete()

PostgreSQL reads

PostgreSQL writes

Foreign key persistence

52 automated tests passing.

---

2026-07-25

Tenant Access Foundation started.

Validated documents:

product-vision.md

access-model.md

permission-matrix.md

carrier-integration-model.md

role-strategy.md

Validated decisions:

SAAS_ADMIN -> users.is_platform_admin

OWNER -> memberships.role

VIEWER -> memberships.role

CarrierIntegration != CarrierAccount

Universal PUDO SaaS remains PUDO-focused

2026-07-25

Carrier Account Persistence Foundation completed.

Implemented:

- carrier_accounts/models.py
- carrier_credentials/models.py
- carrier_accounts table
- carrier_credentials table
- Carrier Account persistence tests
- Carrier Credential persistence tests

Validated:

- carrier_code strategy
- Engine-owned Carrier Catalog
- SaaS-owned Carrier Accounts
- SaaS-owned Carrier Credentials

73 automated tests passing.

---

2026-07-25

Carrier Account Repository Foundation completed.

Implemented:

- carrier_accounts/repository.py
- test_carrier_account_repository.py

Validated:

- get_carrier_account()
- list_carrier_accounts_by_organisation()

Result:

75 passed

0 failed

---

2026-07-25

Carrier Credential Repository Foundation completed.

Implemented:

- carrier_credentials/repository.py
- test_carrier_credential_repository.py

Validated:

- get_carrier_credential()
- list_credentials_by_carrier_account()

Result:

77 passed

0 failed
