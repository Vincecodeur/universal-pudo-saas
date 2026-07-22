# Universal PUDO SaaS - Project Memory

Version: 0.2.0

Status: Phase 1 Documentation Review

Last Updated: 2026-07-22

---

# PURPOSE OF THIS DOCUMENT

This document is the central memory of the project.

Its role is not to replace:

- source code
- tests
- ADRs
- architecture.md
- product-vision.md
- roadmap.md
- project-status.md

Its role is to preserve knowledge.

The objective is to allow:

- Vincent
- Copilot
- future project contributors

to rebuild the project context quickly without rereading months of conversations.

This document may grow indefinitely.

Information should be added over time.

Information should not be removed unless proven incorrect or obsolete.

---

# PROJECT TRUTH MODEL

Project truth is distributed.

No single file is considered the sole source of truth.

The hierarchy of trust is:

1. Source Code
2. Automated Tests
3. ADRs
4. architecture.md
5. product-vision.md
6. roadmap.md
7. project-status.md
8. project-memory.md

When contradictions exist:

Source Code wins.

Tests are considered strong evidence of behaviour.

Documentation must remain aligned with reality.

Never assume undocumented behaviour.

When uncertain:

Request the real file.

---

# PROJECT OVERVIEW

Project Name:

Universal PUDO SaaS

Repository Role:

Application Layer

Primary Purpose:

Provide a hosted platform allowing organisations to access pickup point capabilities without building carrier-specific integrations.

The platform is built on top of:

Universal PUDO Engine

which acts as the technical Core.

---

# REPOSITORY REFERENCES

---

## Universal PUDO SaaS

Repository Status:

Planning and Documentation

Version:

0.1.0-draft

Repository Role:

Application Layer

---

## Universal PUDO Engine

Repository URL:

https://github.com/Vincecodeur/universal-pudo-engine

Repository Status:

Released

Current Known Version:

v1.0.0

Repository Role:

Core

---

# PRODUCT BOUNDARY

This section defines responsibilities that should remain stable over time.

---

## Always Core

These responsibilities belong permanently to Universal PUDO Engine.

Examples:

- carrier integrations
- provider implementations
- ProviderFactory
- carrier payload handling
- carrier API clients
- pickup point normalization
- synchronization
- hybrid search
- carrier abstraction

---

## Never SaaS

The SaaS must never:

- implement carrier APIs
- duplicate providers
- duplicate mappers
- duplicate payload parsers
- duplicate normalization logic

---

## Always SaaS

These responsibilities belong permanently to Universal PUDO SaaS.

Examples:

- authentication
- organisations
- users
- permissions
- carrier credentials
- administration
- exports
- dashboards
- platform monitoring

---

## Never Core

The Core must never:

- own users
- own organisations
- own tenants
- own billing
- own SaaS administration
- own credential management interfaces

---

# PROJECT VISION SUMMARY
