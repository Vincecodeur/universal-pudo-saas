# SaaS Consumption Plan

Version: 1.0

Status: Accepted

Last Updated: 2026-07-26

Location:

docs/ecosystem/saas-consumption-plan.md

---

# Purpose

This document defines how Universal PUDO SaaS consumes Universal PUDO Engine v1.0.0.

The objective is to align the SaaS architecture with the actual Engine implementation.

This document reflects the current Engine reality and must be updated whenever Engine public contracts evolve.

---

# Scope

Repository:

universal-pudo-saas

This document describes:

- what the SaaS consumes
- what the Engine owns
- how carrier discovery works
- how carrier activation works
- what SaaS must not implement

This document does not describe Engine implementation details.

---

# Engine v1.0.0 Reality

The Engine already provides a carrier catalogue.

Known public concepts include:

- Carrier
- CarrierCapability
- CarrierLifecycle
- ProviderFactory

Known public use cases include:

- GetCarrierUseCase
- ListCarriersUseCase
- SearchLivePickupPointsUseCase
- SearchHybridPickupPointsUseCase
- SyncCarrierPickupPointsUseCase

Known API endpoints include:

- GET /carriers
- GET /carriers/{carrier_id}

The Engine already owns carrier discovery.

The SaaS does not need to discover carriers independently.

---

# Ownership Boundary

## Engine Owns

- carrier catalogue
- carrier metadata
- carrier lifecycle
- carrier capabilities
- carrier integrations
- carrier implementations
- provider execution
- pickup point normalization
- pickup point search
- synchronization
- provider health

The Engine is the single source of truth for carrier functionality.

---

## SaaS Owns

- users
- organisations
- memberships
- permissions
- authentication
- carrier accounts
- carrier credentials
- administration
- user experience
- dashboards
- future billing

The SaaS is the system of record for customer configuration.

---

# Carrier Discovery Strategy

The SaaS retrieves carriers from the Engine.

Recommended flow:

Engine
↓
Carrier Catalogue
↓
ListCarriersUseCase
or
GET /carriers
↓
Carrier
↓
SaaS User Interface

The SaaS must not:

- scan provider packages
- inspect Engine source code
- discover carriers independently
- maintain a separate carrier catalogue

The Engine remains responsible for catalogue management.

---

# Carrier Model Consumption

The SaaS should consider Carrier as the reference transport carrier model.

Available attributes include:

- carrier_id
- code
- name
- lifecycle
- supported_countries
- capabilities

The SaaS must reference carriers using Engine identifiers.

---

# Carrier Lifecycle Consumption

CarrierLifecycle communicates transport carrier availability.

Supported values:

ACTIVE

DEPRECATED

UNLISTED

SUNSET

REMOVED

Recommended SaaS behavior:

ACTIVE

→ Normal display and activation

DEPRECATED

→ Visible with a warning

UNLISTED

→ Hidden from normal users

SUNSET

→ Visible with end-of-life warning

REMOVED

→ Not available for activation

Business rules may evolve in future versions.

---

# Carrier Capability Consumption

CarrierCapability describes what a carrier supports.

Engine remains responsible for capability definitions.

The SaaS may use capabilities for:

- UI filtering
- feature visibility
- validation rules
- onboarding assistance
- activation workflows

The SaaS must not define its own capability catalogue.

---

# Carrier Activation Strategy

The SaaS does not create carriers.

The SaaS activates Engine carriers.

Recommended flow:

Carrier exists in Engine
↓
Carrier visible in SaaS
↓
Owner selects Carrier
↓
CarrierAccount created
↓
CarrierCredential stored
↓
Carrier becomes usable

The Engine remains responsible for carrier behavior.

The SaaS remains responsible for carrier configuration.

---

# Carrier Account Ownership

CarrierAccount belongs to the SaaS.

CarrierAccount represents:

Customer-specific access to an Engine carrier.

The CarrierAccount must reference an existing Engine carrier.

The SaaS must never create custom carrier definitions.

---

# Carrier Credential Ownership

CarrierCredential belongs to the SaaS.

The Engine remains credential-agnostic.

The Engine does not own:

- API keys
- passwords
- tokens
- carrier accounts
- credential vaults

Credential ownership strategy follows:

ADR-0002
Carrier Credential Ownership Strategy

---

# Allowed Dependencies

The SaaS may depend on:

- Carrier
- CarrierCapability
- CarrierLifecycle
- ProviderFactory
- SearchLivePickupPointsUseCase
- SearchHybridPickupPointsUseCase
- SyncCarrierPickupPointsUseCase
- GET /carriers
- GET /carriers/{carrier_id}

These elements represent the current publicly consumable Engine surface.

---

# Forbidden Dependencies

The SaaS must not depend directly on:

- CarrierModel
- CarrierRepository
- SQLAlchemy models
- database sessions
- infrastructure layer
- provider clients
- provider parsers
- provider mappers
- carrier payloads

These remain internal Engine implementation details.

---

# SaaS Design Rules

Rule 1

The Engine owns carrier functionality.

---

Rule 2

The SaaS owns carrier configuration.

---

Rule 3

The SaaS consumes the Engine catalogue.

---

Rule 4

The SaaS never duplicates carrier definitions.

---

Rule 5

The SaaS never implements provider-specific logic.

---

Rule 6

The SaaS must treat the Engine as the source of truth for carrier metadata.

---

# Current SaaS Alignment

Validated decisions:

- CarrierAccount belongs to SaaS
- CarrierCredential belongs to SaaS
- Engine owns carrier catalogue
- Engine owns carrier capabilities
- Engine owns carrier lifecycle

These decisions are aligned with Engine v1.0.0.

---

# Future Evolution Candidates

The following topics may be revisited during future Engine releases:

- richer carrier metadata
- expanded capability catalogue
- improved carrier visibility controls
- enhanced lifecycle semantics
- new public Engine contracts

These are future considerations and are not required for current SaaS implementation.

---

# Decision Summary

Universal PUDO SaaS consumes Universal PUDO Engine.

The Engine owns carrier functionality.

The SaaS owns customer configuration.

The Engine owns the carrier catalogue.

The SaaS consumes the carrier catalogue.

The SaaS must not duplicate carrier definitions, implement provider logic, or depend on Engine internals.

Current SaaS development should be based entirely on the Engine v1.0.0 public surface.
