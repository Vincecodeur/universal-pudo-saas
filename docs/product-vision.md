# Universal PUDO SaaS - Product Vision

Version: 0.2.0

Status: Phase 1 Documentation Review

Last Updated: 2026-07-22

---

# EXECUTIVE SUMMARY

Universal PUDO SaaS is a multi-tenant platform that enables organisations to connect their carrier accounts and access pickup point capabilities through a unified interface.

The platform is built on top of:

Universal PUDO Engine

which acts as the Core carrier intelligence layer.

Universal PUDO SaaS acts as the application and customer-facing layer.

The project targets:

- logistics providers
- e-commerce merchants
- software vendors

while keeping carrier complexity hidden behind a unified platform.

---

# VISION

Our vision is to become the reference platform for pickup point discovery and operational usage.

Users should not need to:

- understand carrier APIs
- understand carrier payloads
- maintain carrier integrations
- normalize carrier data

Instead they should simply:

- connect carrier credentials
- search pickup points
- visualize pickup points
- export pickup point data
- consume pickup point services

through a single platform.

---

# WHY THIS PROJECT EXISTS

Every carrier exposes:

- different APIs
- different authentication methods
- different payloads
- different business rules
- different identifiers

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- DPD
- GLS
- UPS
- InPost

This creates duplicated work for:

- logistics operators
- merchants
- software vendors

Universal PUDO Engine solves the technical integration problem.

Universal PUDO SaaS solves the operational consumption problem.

---

# VALUE PROPOSITION

---

## For Logistics Providers

Instead of integrating and maintaining multiple carriers independently:

Connect carrier accounts once and access pickup point capabilities through a unified platform.

Benefits:

- reduced integration effort
- reduced maintenance effort
- faster onboarding

---

## For E-commerce Merchants

Instead of building custom carrier integrations:

Access pickup point information through a dedicated platform.

Benefits:

- faster operational deployment
- reduced technical complexity
- reusable pickup point data

---

## For Software Vendors

Instead of maintaining carrier-specific implementations:

Consume pickup point capabilities through a stable platform.

Benefits:

- reduced development costs
- reduced carrier dependency
- faster feature delivery

---

# TARGET CUSTOMERS

---

## Logistics Providers

Examples:

- 3PL operators
- fulfillment providers
- warehouse operators

---

## E-commerce Merchants

Examples:

- marketplace sellers
- brands
- retailers

---

## Software Vendors

Examples:

- OMS vendors
- WMS vendors
- TMS vendors
- custom software providers

---

# PRODUCT POSITIONING

Universal PUDO SaaS is:

- a platform
- an application layer
- a pickup point services platform

Universal PUDO SaaS is NOT:

- a carrier
- a transport management system
- an order management system
- a warehouse management system
- an ERP

---

# PRODUCT BOUNDARIES

---

## Responsibilities Owned By The SaaS

The SaaS owns:

- users
- organisations
- authentication
- permissions
- carrier credential management
- exports
- administration
- operational interfaces

---

## Responsibilities Not Owned By The SaaS

The SaaS does not own:

- carrier integrations
- provider implementations
- carrier API clients
- pickup point normalization
- synchronization logic

These remain inside:

Universal PUDO Engine

---

# RELATIONSHIP WITH UNIVERSAL PUDO ENGINE

Universal PUDO Engine remains the Core.

Repository:

https://github.com/Vincecodeur/universal-pudo-engine

The SaaS consumes the Core.

The Core must remain reusable independently of the SaaS.

The SaaS must never duplicate Core responsibilities.

---

# ORGANISATION MODEL

The platform is organisation-centric.

Relationship:

Organisation
│
├── Users
├── Carrier Accounts
├── Searches
├── Exports
└── Permissions

All business data belongs to an organisation.

Users are not considered standalone entities.

---

# USER TYPES

---

## Organisation User

Capabilities:

- searches
- exports
- operational usage

---

## Organisation Administrator

Capabilities:

- manage users
- manage carrier accounts
- manage organisation settings

---

## SaaS Super Administrator

Capabilities:

- manage organisations
- monitor platform operations
- investigate issues
- platform administration

Exists from V1.

---

# CARRIER ACCOUNT PHILOSOPHY

Customers bring their own carrier accounts.

Examples:

- Colissimo account
- Mondial Relay account
- Chronopost account
- DPD account

Universal PUDO SaaS is not a carrier reseller.

Universal PUDO SaaS is not responsible for carrier contracts.

The platform only provides access to technical capabilities.

---

# CREDENTIAL OWNERSHIP STRATEGY

Carrier credentials belong to the customer.

The SaaS stores and manages credentials.

The Core consumes credentials.

Benefits:

- clear responsibility separation
- reusable Core
- customer ownership

---

# SEARCH EXPERIENCE

Search is considered a primary platform capability.

Supported directions:

- postal code search
- city search
- location-based search
- carrier filtering
- multi-carrier search

The objective is not simply retrieving pickup points.

The objective is operational usability.

---

# MAP EXPERIENCE

Map functionality is a first-class feature.

Technology:

Leaflet

OpenStreetMap

Objectives:

- pickup point exploration
- pickup point comparison
- operational visibility

---

# EXPORT EXPERIENCE

Export capabilities are equally important as visualization.

Long-term objective:

Allow pickup point data to be reused operationally.

Future export formats may include:

- CSV
- Excel
- JSON

---

# API FIRST STRATEGY

The platform should not be designed exclusively around the user interface.

Long-term vision:

UI

- API

Whenever reasonable:

Capabilities exposed through the UI should also be exposable through APIs.

This principle must guide future architectural decisions.

---

# INTERNATIONAL STRATEGY

The platform is designed for international carrier ecosystems.

Initial implementations may focus on a limited set of carriers.

However the architecture must remain compatible with:

- EMEA expansion
- new carrier integrations
- country-specific transport ecosystems

The platform must not assume a single-country operating model.

---

# DEPLOYMENT STRATEGY

Official decision:

SaaS-first

Self-host-ready

---

## Current Scope

Multi-tenant SaaS

---

## Future Scope

Potential future support for:

- private deployments
- customer-managed infrastructure
- enterprise environments

---

## Architectural Constraint

Future self-hosted deployments must remain possible without major redesign.

---

# SECURITY PRINCIPLES

Sensitive information includes:

- carrier credentials
- organisation data
- user information

Security must be considered a first-class concern from the beginning of the project.

---

# BILLING

Status:

Backlog

Business model has not yet been decided.

Billing must not drive architectural decisions during V1.

---

# LONG-TERM EXPANSION PRINCIPLES

Potential future capabilities may include:

- public APIs
- analytics
- operational dashboards
- monitoring
- recommendation engines
- webhooks
- SSO
- enterprise deployment options
- billing

These capabilities must be evaluated individually.

No future capability should compromise Core/SaaS separation.

---

# SUCCESS CRITERIA

Universal PUDO SaaS V1 is successful when an organisation can:

- create an account
- create an organisation
- connect carrier accounts
- perform pickup point searches
- visualize results
- export results
- manage users

without custom carrier development.

---

# CURRENT STATUS

Current Phase:

Phase 1

Status:

Documentation Review

Next Major Objective:

Validate documentation and open Phase 2.

---

# CHANGE HISTORY

2026-07-22

V1 created.

2026-07-22

V2 review consolidation applied.

Added:

- Value Proposition
- Product Boundaries
- API First Strategy
- Credential Ownership Rationale
- International Strategy
- Long-Term Expansion Principles
