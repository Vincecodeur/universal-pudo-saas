# Changelog

All notable changes to this project will be documented in this file.

---

# [0.1.0-draft] - 2026-07-22

## Added

ADR-0001 Repository Structure Strategy

ADR-0002 Authentication Strategy

ADR-0003 Credential Storage Strategy

ADR-0004 Multi-Tenant Strategy

ADR-0005 Module Boundary Strategy

ADR-0006 Self-Hosted Compatibility Strategy

docs/domain-model.md

docs/database-model.md

docs/persistence-decisions.md

## Accepted Decisions

- UUID Strategy
- BaseEntity Strategy
- Timestamp Strategy
- Soft Delete Strategy
- Audit Strategy
- SearchResult Persistence
- OrganisationSettings
- Role Ownership Through Membership

## Project Progress

ADR Foundation completed.

Domain Model completed.

Database Model completed.

Persistence Decisions completed.
``

## Added

Initial project documentation.

Created:

- README.md
- CHANGELOG.md
- docs/project-memory.md
- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md
- docs/project-status.md

---

## Architecture Decisions

Accepted:

- Core repository remains independent
- Universal PUDO Engine acts as carrier intelligence layer
- Credentials owned by SaaS
- Next.js selected as frontend framework
- React selected as frontend library
- TypeScript selected as frontend language
- FastAPI selected as backend framework
- PostgreSQL selected as primary database
- Leaflet selected for map rendering
- OpenStreetMap selected for map provider
- SaaS-first deployment strategy
- Self-host-ready architecture
- Organisation-centric tenancy model
- Super Admin model
- One carrier account per carrier and organisation

---

## Roadmap

Phase 1:

Documentation Foundation

Status:

Documentation Review

---

## Repository State

Backend:

Not Started

Frontend:

Not Started

Database:

Not Started

Authentication:

Not Started

Carrier Accounts:

Not Started

Exports:

Not Started

Administration:

Not Started

---

## Known Backlog

- Billing
- Multiple Carrier Accounts
- SSO
- Self-Hosted Distribution
- Analytics
- Recommendation Engine
- Webhooks

## Changed

Repository initialized locally.

GitHub repository created:

https://github.com/Vincecodeur/universal-pudo-saas

Initial commit completed:

docs: initialize project documentation foundation

Primary branch renamed to:

main

Remote origin configured.

First push completed.

Repository structure strategy validated:

Monorepo

Target structure:

backend/
frontend/

Phase 1 officially completed.

Phase 2 officially opened.
