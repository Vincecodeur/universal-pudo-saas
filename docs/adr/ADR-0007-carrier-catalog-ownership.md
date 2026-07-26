# ADR-0007 - Carrier Catalog Ownership Strategy

Status: Accepted

Date: 2026-07-25

---

# Context

Universal PUDO SaaS introduces carrier-specific configuration through:

- CarrierAccount
- CarrierCredential

At the same time, Universal PUDO Engine already owns:

- carrier providers
- carrier integrations
- provider implementations
- carrier synchronization
- pickup point normalization
- carrier intelligence

A design decision is required to define which product owns the carrier catalog.

Without a clear ownership model, both products could start persisting carrier definitions independently, leading to:

- duplicated data
- ownership conflicts
- synchronization issues
- inconsistent carrier configurations
- unclear product boundaries

The project requires a single source of truth for carrier definitions.

---

# Decision

Universal PUDO Engine owns the carrier catalog.

Universal PUDO SaaS does not persist carrier definitions.

Universal PUDO SaaS references carriers through a logical identifier:

- carrier_code

CarrierAccount stores:

- organisation-specific carrier configuration

CarrierCredential stores:

- organisation-specific carrier credentials

Universal PUDO Engine remains responsible for:

- carrier catalog management
- carrier provider implementations
- carrier metadata
- provider capabilities
- carrier synchronization

Universal PUDO SaaS remains responsible for:

- tenant ownership
- carrier account configuration
- carrier credentials
- access control
- user-facing management workflows

---

# Consequences

## Positive

Single source of truth for carriers.

Clear ownership boundaries between Core and SaaS.

No carrier catalog duplication.

Simpler maintenance.

Simpler future carrier onboarding.

Better long-term separation of concerns.

Supports independent evolution of Universal PUDO Engine and Universal PUDO SaaS.

## Negative

Universal PUDO SaaS cannot operate independently from the carrier catalog exposed by Universal PUDO Engine.

CarrierAccount records must reference valid carrier_code values provided by the Core.

Future SaaS features relying on carrier metadata must retrieve that information from Universal PUDO Engine rather than persisting it locally.

---

# Alternatives Considered

## Option A - SaaS Owns Carrier Catalog

Description:

Universal PUDO SaaS persists carrier definitions and carrier metadata in its own database.

Rejected.

Reasons:

- duplicates Core responsibilities
- introduces synchronization complexity
- weakens product boundaries
- increases maintenance cost

---

## Option B - Shared Ownership

Description:

Both products persist carrier definitions.

Rejected.

Reasons:

- no clear source of truth
- conflict resolution required
- ownership ambiguity
- increased architectural complexity

---

## Option C - Core Owns Carrier Catalog

Description:

Universal PUDO Engine owns carrier definitions.

Universal PUDO SaaS references carriers through carrier_code.

Accepted.

Reason:

This option provides the clearest separation of responsibilities and preserves the intended architecture of the ecosystem.

---

# Implementation Impact

Implemented entities:

- CarrierAccount
- CarrierCredential

Implemented database tables:

- carrier_accounts
- carrier_credentials

Implemented reference strategy:

- carrier_code

Repository layer:

- carrier_accounts/repository.py
- carrier_credentials/repository.py

Validated during:

- Carrier Account Persistence Foundation
- Carrier Account Repository Foundation
- Carrier Credential Repository Foundation

---

# Related Documents

- ADR-0003 Credential Ownership
- architecture.md
- carrier-integration-model.md
- domain-model.md
- database-model.md
- project-memory.md

---

# Final Statement

Universal PUDO Engine is the authoritative source for carrier definitions.

Universal PUDO SaaS manages carrier usage by organisations but does not own the carrier catalog itself.
