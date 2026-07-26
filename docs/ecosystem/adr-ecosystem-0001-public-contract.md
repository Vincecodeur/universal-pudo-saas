# ADR-ECOSYSTEM-0001 - Public Contract Strategy

Status: Accepted

Date: 2026-07-26

---

# Context

Universal PUDO Engine is consumed by external repositories.

These repositories evolve independently.

Examples:

- universal-pudo-saas
- future SDK repositories
- future CMS plugins

A stable contract is required between the Engine and each consumer.

---

# Decision

Each consumer repository owns its own contract documentation.

Contracts are documented from the consumer perspective.

The Engine remains implementation-focused.

Consumers define which Engine capabilities they depend on.

---

# Benefits

- repository independence
- clear ownership
- isolated evolution
- easier version management

---

# Consequences

Changes in Engine capabilities may require updates to consumer contracts.

Each consumer remains responsible for documenting its expectations.

---

# Result

Contract documentation belongs to consumer repositories.

The Engine focuses on implementation and public interfaces.
