# Universal PUDO SaaS

Status: Planning Phase

Universal PUDO SaaS is a multi-tenant platform built on top of Universal PUDO Engine.

The objective of the platform is to allow organisations to:

- manage users
- manage organisations
- connect carrier accounts
- search pickup points
- visualize pickup points
- export pickup point data
- administer platform usage

without implementing carrier-specific integrations.

---

# Relationship With Universal PUDO Engine

Universal PUDO SaaS depends on:

Universal PUDO Engine

Repository:

https://github.com/Vincecodeur/universal-pudo-engine

Universal PUDO Engine remains responsible for:

- carrier integrations
- provider implementations
- pickup point normalization
- carrier abstraction
- carrier synchronization

Universal PUDO SaaS remains responsible for:

- authentication
- users
- organisations
- permissions
- carrier credentials
- exports
- administration

The SaaS must never duplicate Core responsibilities.

---

# Current Status

Current Phase:

Phase 1 - Documentation Foundation

Current State:

Documentation only.

No implementation exists.

No backend exists.

No frontend exists.

No database exists.

No tests exist.

---

# Target Technology Stack

Frontend

- Next.js
- React
- TypeScript

Backend

- FastAPI

Database

- PostgreSQL
- SQLAlchemy
- Alembic

Maps

- Leaflet
- OpenStreetMap

---

# Target Customer Profiles

Universal PUDO SaaS is designed for:

- Logistics Providers (3PL)
- E-commerce Merchants
- Software Vendors

Examples:

- OMS vendors
- WMS vendors
- TMS vendors
- Fulfillment providers
- Retailers

---

# Product Scope

V1 Objectives:

- user management
- organisation management
- carrier account management
- pickup point search
- map visualization
- exports
- administration

Out of Scope:

- carrier integration development
- OMS implementation
- WMS implementation
- TMS implementation
- billing

---

# Deployment Strategy

Official Decision:

SaaS-first

Self-host-ready

Current Scope:

Multi-tenant SaaS

Future Possibility:

Enterprise self-hosted deployments.

---

# Documentation

Project documentation is located in:

docs/

Current Documents:

- project-memory.md
- product-vision.md
- architecture.md
- roadmap.md
- project-status.md

---

# Roadmap Status

Current Status:

Phase 1 Documentation Review

Next Goal:

Validate documentation.

Open Phase 2 Repository Foundation.

---

# License

To Be Defined.
`
