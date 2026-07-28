# Universal PUDO SaaS - Product Vision

Version: 1.0.0

Status: Approved

Last Updated: 2026-07-28

---

# EXECUTIVE SUMMARY

Universal PUDO SaaS is a multi-tenant platform that enables organisations to connect their carrier accounts and access pickup point information through a unified interface.

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

- connect carrier accounts
- search pickup points
- visualize pickup points
- export pickup point data
- consume normalized PUDO information

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

## For Logistics Providers

Instead of integrating and maintaining multiple carriers independently:

Connect carrier accounts once and access pickup point information through a unified platform.

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

Consume pickup point information through a stable platform.

Benefits:

- reduced development costs
- reduced carrier dependency
- faster feature delivery

---

# TARGET CUSTOMERS

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
- a PUDO information platform

Universal PUDO SaaS is NOT:

- a carrier
- a transport management system
- an order management system
- a warehouse management system
- an ERP

---

# PRODUCT SCOPE

Universal PUDO SaaS is a PUDO-focused platform.

The purpose of the platform is to make pickup point information available through a unified SaaS experience.

The platform focuses on:

- carrier account connectivity
- pickup point discovery
- pickup point visualization
- pickup point analytics
- pickup point data consumption
- pickup point data export

The platform must remain focused on PUDO usage and administration.

Universal PUDO SaaS is not intended to become a generic logistics platform.

---

# OUT OF SCOPE

The following capabilities are outside the current product scope:

- shipment creation
- shipping label generation
- tracking management
- delivery orchestration
- transport rating
- transport execution
- customs management
- carrier product management
- carrier service management
- non-PUDO carrier capabilities

These responsibilities belong to:

- OMS platforms
- WMS platforms
- TMS platforms
- carrier execution systems

Universal PUDO SaaS focuses exclusively on pickup point information.

---

# PRODUCT BOUNDARIES

## Responsibilities Owned By The SaaS

The SaaS owns:

- users
- organisations
- authentication
- permissions
- carrier credential management
- carrier account management
- carrier activation workflows
- dashboard administration
- exports
- administration
- operational interfaces

---

## Responsibilities Not Owned By The SaaS

The SaaS does not own:

- carrier integrations implementation logic
- provider implementations
- carrier API clients
- pickup point normalization
- synchronization logic

These remain inside:

Universal PUDO Engine

---

# PRODUCT GUARDRAIL

Universal PUDO SaaS exists to provide access to PUDO information.

Any new feature must support:

- pickup point access
- pickup point search
- pickup point visualization
- pickup point analytics
- pickup point consumption

Features unrelated to PUDO information must be considered out of scope unless a strong business case is validated.

The platform must not evolve into a generic OMS, WMS, TMS, shipping or carrier execution platform.

---

# RELATIONSHIP WITH UNIVERSAL PUDO ENGINE

Universal PUDO Engine remains the Core.

Repository:

[Universal PUDO Engine Repository](https://github.com/Vincecodeur/universal-pudo-engine)

The SaaS consumes the Core.

The Core must remain reusable independently of the SaaS.

The SaaS must never duplicate Core responsibilities.

---

# ORGANISATION MODEL

The platform is organisation-centric.

Relationship:

```text
Organisation
│
├── Users
├── Carrier Accounts
├── Searches
├── Exports
├── Dashboard Configuration
└── API Credentials
```

All business data belongs to an organisation.

Users are not considered standalone entities.

---

# USER TYPES

The platform currently supports:

- SaaS Administrator
- Owner
- Viewer

---

## SaaS Administrator

Scope:

Entire platform

Responsibilities:

- manage organisations
- manage subscriptions
- manage quotas
- manage billing
- manage platform operations
- publish carriers
- manage carrier visibility
- manage carrier availability for organisations

---

## Owner

Scope:

Single organisation

Responsibilities:

- create Viewers
- remove Viewers
- connect carrier accounts
- configure carrier credentials
- manage organisation settings
- configure dashboards
- configure API access
- manage organisation analytics

---

## Viewer

Scope:

Single organisation

Responsibilities:

- search pickup points
- view dashboards
- view analytics
- export search results
- consume PUDO data

---

# CARRIER INTEGRATION MODEL

The platform distinguishes between:

- Carrier Integration
- Carrier Account

---

## Carrier Publication

Platform-level capability.

Carrier definitions remain owned by Universal PUDO Engine.

The SaaS Administrator controls:

- carrier publication
- carrier visibility
- carrier availability

without owning carrier implementations or carrier definitions.

---

## Carrier Account

Organisation-level entity.

Owned by the Organisation Owner.

Examples:

- Spriiint Colissimo account
- PrintChic Mondial Relay account
- Organisation A DPD account

The Owner may connect carrier accounts only for integrations made available by the SaaS Administrator.

The two concepts must remain separate.

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

The platform only provides access to PUDO information.

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

- Leaflet
- OpenStreetMap

Objectives:

- pickup point exploration
- pickup point comparison
- operational visibility

---

# EXPORT EXPERIENCE

Export capabilities are important because PUDO information must be reusable operationally.

Possible formats:

- CSV
- Excel
- JSON

Exports remain focused on PUDO information.

---

# API FIRST STRATEGY

The platform should not be designed exclusively around the user interface.

Long-term vision:

```text
UI
↓
API
```

Whenever reasonable:

Capabilities exposed through the UI should also be exposed through APIs.

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

No future capability should compromise the PUDO-focused scope of the platform.

---

# SUCCESS CRITERIA

Universal PUDO SaaS V1 is successful when an organisation can:

- authenticate
- manage users
- manage memberships
- manage roles
- manage carrier accounts
- search pickup points
- visualize pickup points
- export pickup point data
- administer the platform

without custom carrier development.

---

# CURRENT STATUS

Current Phase:

Phase 16.6

Status:

Search Platform Closure

Current Focus:

Search Platform Closure

- freeze Search Platform contract
- validate architecture boundaries
- confirm non-persistence strategy
- synchronize documentation
- prepare Phase 17 planning

---

# CHANGE HISTORY

2026-07-22

V1 created.

---

2026-07-22

V2 review consolidation applied.

Added:

- Value Proposition
- Product Boundaries
- API First Strategy
- Credential Ownership Rationale
- International Strategy
- Long-Term Expansion Principles

---

2026-07-25

Product scope clarified.

Validated concepts:

- SaaS Administrator
- Owner
- Viewer

Added:

- Product Scope
- Out Of Scope
- Product Guardrail
- Carrier Integration Model

Validated separation:

- Carrier Integration
- Carrier Account

Confirmed product focus:

PUDO information access, search, visualization and consumption.

---

2026-07-26

Carrier Catalog ownership realigned.

Validated:

- Universal PUDO Engine owns carrier catalog definitions.
- Universal PUDO SaaS consumes carrier catalog data.
- SaaS stores carrier accounts only.
- SaaS stores carrier credentials only.

---

2026-07-27

Search Platform introduced.

Validated:

- SearchRequest
- SearchResult
- SaaS-owned search abstraction layer
- Search Platform responsibility boundary

Result:

142 automated tests passing.

---

2026-07-28

Search Platform Service Foundation completed.

Validated:

- SearchPlatformService
- SearchRequest consumption
- SearchResult generation
- SaaS-owned search service boundary
- MultiCarrierSearchService delegation

Result:

145 automated tests passing.

2026-07-28

Search Result Enrichment Foundation completed.

Validated:

- SearchExecutionMetadata
- Result metadata enrichment
- Search execution metadata

Result:

150 automated tests passing.

---

2026-07-28

Search Platform Validation completed.

Validated:

- SearchRequest lifecycle
- SearchResult lifecycle
- SearchExecutionMetadata
- SearchPlatformService
- Search Platform boundaries

Result:

150 automated tests passing.
