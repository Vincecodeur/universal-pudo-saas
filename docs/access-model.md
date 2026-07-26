# Universal PUDO SaaS - Access Model

Version: 1.0.0

Status: Approved

Last Updated: 2026-07-25

---

# PURPOSE

This document defines how users access and interact with Universal PUDO SaaS.

It describes:

- user types
- responsibilities
- permissions
- ownership boundaries
- future access strategy

This document must be approved before implementing Roles & Permissions.

---

# PRODUCT VISION

Universal PUDO SaaS is a multi-tenant platform built on top of Universal PUDO Engine.

The primary purpose of the platform is to allow organizations to:

- connect their carrier accounts
- search pickup points
- consume normalized PUDO data
- monitor usage and coverage
- expose PUDO services to their internal systems

User management is not the product.

User management only exists to control access to the product.

---

# ACCESS PHILOSOPHY

The platform follows a simple access model.

Users should be separated according to their responsibilities.

The objective is to distinguish:

- who operates the SaaS
- who owns a tenant
- who consumes the service

The platform intentionally avoids complex enterprise RBAC during V1.

---

# USER TYPES

The platform currently defines three user types:

1. SaaS Administrator
2. Owner
3. Viewer

---

# SAAS ADMINISTRATOR

Scope:

Entire platform

Represents:

Platform operator

Examples:

- SaaS owner
- platform administrator
- support team
- operations team

---

## Responsibilities

SaaS Administrators are responsible for:

- creating organisations
- suspending organisations
- managing subscriptions
- managing quotas
- monitoring platform health
- managing the carrier integration catalog
- making carrier integrations available to organisation Owners
- enabling carrier integrations at platform level
- disabling carrier integrations at platform level
- support operations
- billing management

---

## Permissions

Can:

✅ Create organisations

✅ Suspend organisations

✅ Manage subscriptions

✅ Manage quotas

✅ Access platform-wide statistics

✅ Manage the carrier integration catalog

✅ Publish carrier integrations

✅ Make carrier integrations available to organisation Owners

✅ Enable carrier integrations at platform level

✅ Disable carrier integrations at platform level

✅ Access support tooling

✅ View all tenants

---

## Carrier Integration Catalog Ownership

The SaaS Administrator owns the platform-level carrier integration catalog.

This means the SaaS Administrator decides which carrier integrations are available on the platform.

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- DPD
- future carrier integrations

The SaaS Administrator makes these integrations available to organisation Owners.

The SaaS Administrator does not configure customer-specific carrier accounts.

Customer-specific carrier credentials and carrier account configuration remain the responsibility of the organisation Owner.

---

Cannot:

❌ Act as organisation owner without explicit impersonation mechanism

---

# OWNER

Scope:

Single organisation

Represents:

Customer account owner

Examples:

- IT manager
- logistics manager
- transport manager
- e-commerce director
- business owner

---

## Responsibilities

The Owner is responsible for configuring the tenant.

The Owner transforms an empty tenant into an operational PUDO platform.

---

## Permissions

Can:

✅ Create Viewer accounts

✅ Remove Viewer accounts

✅ Activate Viewer accounts

✅ Deactivate Viewer accounts

✅ Connect carrier accounts

✅ Configure carrier credentials

✅ Update carrier credentials

✅ Test carrier connectivity

✅ Enable carriers

✅ Disable carriers

✅ Configure future external APIs

✅ Access organisation statistics

✅ Access organisation analytics

✅ Configure dashboards

✅ Select displayed KPIs

✅ Manage organisation settings

---

## Transporter Ownership

Carrier configuration belongs to the Owner.

Examples:

- Colissimo account
- Mondial Relay account
- DPD account
- Chronopost account
- future carrier integrations

Viewer users must never modify carrier connectivity.

---

## Carrier Availability Boundary

The Owner can only configure carrier integrations that have been made available by the SaaS Administrator.

The Owner cannot publish a new carrier integration to the platform.

The Owner cannot make a carrier integration available to other organisations.

The Owner manages only organisation-specific carrier accounts and credentials.

---

## Dashboard Ownership

The dashboard configuration belongs to the Owner.

Examples:

- selected KPIs
- displayed charts
- coverage dashboards
- usage dashboards
- custom widgets

Different organisations may configure completely different dashboards.

---

# VIEWER

Scope:

Single organisation

Represents:

Operational user

Examples:

- logistics operator
- customer service operator
- warehouse user
- transport analyst
- project member

---

## Responsibilities

Viewer users consume the service.

Viewer users do not administer the platform.

---

## Permissions

Can:

✅ Search pickup points

✅ Filter search results

✅ View dashboards

✅ View statistics

✅ Consume PUDO data

✅ Access configured carriers

✅ View organisation data

✅ Export search results

---

Cannot:

❌ Create users

❌ Remove users

❌ Modify permissions

❌ Configure carriers

❌ Modify carrier credentials

❌ Enable transporters

❌ Disable transporters

❌ Configure dashboards

❌ Modify organisation settings

---

# ACCESS MODEL SUMMARY

| Capability                                    | SaaS Admin | Owner | Viewer |
| --------------------------------------------- | ---------- | ----- | ------ |
| Manage Carrier Integration Catalog            | ✅         | ❌    | ❌     |
| Publish Carrier Integrations                  | ✅         | ❌    | ❌     |
| Make Carrier Integrations Available to Owners | ✅         | ❌    | ❌     |
| Connect Organisation Carrier Accounts         | ❌         | ✅    | ❌     |
| Modify Organisation Carrier Credentials       | ❌         | ✅    | ❌     |
| Use Available Carrier Integrations            | ❌         | ✅    | ✅     |
| Create Organisation                           | ✅         | ❌    | ❌     |
| Manage Subscription                           | ✅         | ❌    | ❌     |
| Create Users                                  | ❌         | ✅    | ❌     |
| Disable Users                                 | ❌         | ✅    | ❌     |
| Connect Carriers                              | ❌         | ✅    | ❌     |
| Modify Carrier Credentials                    | ❌         | ✅    | ❌     |
| Configure Dashboard                           | ❌         | ✅    | ❌     |
| View Dashboard                                | ✅         | ✅    | ✅     |
| Search PUDO                                   | ✅         | ✅    | ✅     |
| Export Search Results                         | ✅         | ✅    | ✅     |
| View Statistics                               | ✅         | ✅    | ✅     |
| Manage Platform Integrations                  | ✅         | ❌    | ❌     |

---

# FUTURE EVOLUTION

The V1 model intentionally remains simple.

Future versions may introduce:

- Organisation Admin
- API User
- Service Account
- Read-Only Auditor

These roles are not part of the current scope.

They will only be introduced if a validated business need emerges.

---

# ARCHITECTURAL CONSEQUENCES

The following entities are expected to be associated with an Organisation:

- Users
- Carrier Accounts
- Dashboard Configurations
- Search History
- API Credentials

Ownership:

Owner manages:

- Users
- Carrier Accounts
- Dashboard Configuration
- API Credentials

Viewer consumes:

- Searches
- Results
- Dashboards
- Statistics

---

# SUCCESS CRITERIA

The access model is considered implemented when:

✅ Users can authenticate

✅ Organisations can have Owners

✅ Owners can create Viewers

✅ Owners can connect carrier accounts

✅ Owners can configure dashboards

✅ Viewers can search pickup points

✅ Viewers cannot modify configuration

✅ Permissions are enforced by automated tests

---

# CHANGE HISTORY

2026-07-25

Initial access model definition created.

Validated user types:

- SaaS Administrator
- Owner
- Viewer

Owner confirmed as carrier account owner and dashboard owner.

Viewer confirmed as operational service consumer.
