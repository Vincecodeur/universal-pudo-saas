# Universal PUDO SaaS - Project Memory

Version: 0.6.0

Status: Active

Last Updated: 2026-07-23

---

# PURPOSE

This document preserves the long-term memory of the project.

It contains:

- strategic decisions
- architectural direction
- validated assumptions
- completed milestones
- lessons learned
- current state
- next milestones

This document complements:

- source code
- ADRs
- roadmap
- project-status

Source of Truth Priority:

1. Source Code
2. Database Schema
3. Approved ADRs
4. Architecture Documents
5. Project Documentation

When conflicts exist, source code wins.

---

# PROJECT SUMMARY

Universal PUDO SaaS is a multi-tenant SaaS platform built on top of Universal PUDO Engine.

The SaaS owns:

- authentication
- organisations
- users
- memberships
- permissions
- carrier accounts
- exports
- administration

Universal PUDO Engine owns:

- carrier integrations
- provider implementations
- search orchestration
- normalization
- carrier intelligence

The SaaS must consume the Core.

The SaaS must never duplicate Core logic.

---

# PROJECT REPOSITORIES

## Universal PUDO SaaS

Role:

Application Layer

Status:

Active Development

Repository:

universal-pudo-saas

---

## Universal PUDO Engine

Role:

Carrier Intelligence Layer

Status:

Integrated

Version:

v1.0.0

Repository:

https://github.com/Vincecodeur/universal-pudo-engine

---

# STRATEGIC ARCHITECTURAL DECISIONS

## D001

Hosting Strategy

Decision:

SaaS-first

Self-host-ready

Status:

Accepted

ADR:

ADR-0006

---

## D002

Repository Strategy

Decision:

Monorepo

Status:

Accepted

ADR:

ADR-0001

---

## D003

Authentication

Decision:

Email + Password

JWT

Status:

Accepted

ADR:

ADR-0002

---

## D004

Credential Ownership

Decision:

Credentials managed by SaaS.

Core consumes credentials.

Status:

Accepted

ADR:

ADR-0003

---

## D005

Multi-Tenant Strategy

Decision:

Tenant = Organisation

Status:

Accepted

ADR:

ADR-0004

---

## D006

Module Boundaries

Decision:

Business Modules

Status:

Accepted

ADR:

ADR-0005

---

# VALIDATED TECHNOLOGY STACK

Frontend

- Next.js
- React
- TypeScript

Status:

Planned

---

Backend

- FastAPI
- Python 3.14

Status:

Validated

---

Database

- PostgreSQL 17

Status:

Validated

---

ORM

- SQLAlchemy

Status:

Validated

---

Migrations

- Alembic

Status:

Validated

---

Maps

- Leaflet
- OpenStreetMap

Status:

Planned

---

# DATABASE OWNERSHIP STRATEGY

## Universal PUDO Engine Database

Database:

universal_pudo

Owner:

Universal PUDO Engine

Status:

Validated

---

## Universal PUDO SaaS Database

Database:

universal_pudo_saas

Owner:

Universal PUDO SaaS

Status:

Validated

Created:

2026-07-23

---

## Architectural Rule

Core and SaaS databases remain independent.

Benefits:

- migration isolation
- deployment isolation
- ownership clarity
- upgrade flexibility
- lower coupling

This decision is now considered validated.

---

# IMPLEMENTED FOUNDATIONS

## Documentation Foundation

Status:

Completed

---

## Repository Foundation

Status:

Completed

---

## Architecture Foundation

Status:

Completed

---

## ADR Foundation

Status:

Completed

Approved ADRs:

ADR-0001

ADR-0002

ADR-0003

ADR-0004

ADR-0005

ADR-0006

---

## Domain Model Design

Status:

Completed

---

## Database Model Design

Status:

Completed

---

## Persistence Decisions

Status:

Completed

---

## Backend Foundation

Status:

Completed

Deliverables:

✅ FastAPI

✅ Health Endpoint

✅ Configuration Layer

✅ Project Structure

✅ Tests Foundation

---

## Database Configuration Foundation

Status:

Completed

Deliverables:

✅ SQLAlchemy Base

✅ BaseEntity

✅ SessionLocal

✅ Environment Configuration

✅ .env.example

✅ Runtime DATABASE_URL

---

## Alembic Foundation

Status:

Completed

Deliverables:

✅ Alembic Installed

✅ alembic.ini

✅ env.py

✅ SQLAlchemy Metadata Integration

✅ PostgreSQL Integration

✅ Dedicated SaaS Database

✅ alembic current Validation

---

# IMPLEMENTED PERSISTENCE DECISIONS

UUID Strategy

Implemented

---

BaseEntity Strategy

Implemented

---

Timestamp Strategy

Implemented

---

Soft Delete Strategy

Implemented

---

Audit Strategy

Designed

Not Implemented

---

Search Persistence Strategy

Designed

Not Implemented

---

Membership Ownership Strategy

Designed

Not Implemented

---

# CURRENT TEST STATUS

Validated Tests:

test_main.py

test_entities.py

test_settings.py

---

Current Result:

3 passed

0 failed

---

# CURRENT CODE STATUS

Implemented:

✅ FastAPI Startup

✅ Health Endpoint

✅ Settings

✅ PostgreSQL Configuration

✅ SQLAlchemy Base

✅ BaseEntity

✅ Session Factory

✅ Alembic

✅ Dedicated SaaS Database

---

Not Implemented:

❌ Organisation

❌ Membership

❌ User

❌ Authentication

❌ Carrier Accounts

❌ Searches

❌ Exports

❌ Administration

❌ Frontend

---

# LESSONS LEARNED

## Lesson 001

Infrastructure First Works

Observation:

Building the foundations before business entities reduced rework.

Validated Sequence:

Documentation

↓

Architecture

↓

ADR

↓

Persistence

↓

Business Entities

---

## Lesson 002

Alembic Must Be Installed Before First Entity

Observation:

Creating entities before validating Alembic would have increased migration risk.

Decision:

Always validate migrations before creating business tables.

---

## Lesson 003

The Real Source Of Truth Is The Code

Observation:

Several documents drifted from reality during implementation.

Decision:

Code + validated documentation are the source of truth.

Documentation must be synchronized after each phase.

---

## Lesson 004

Separate Databases Early

Observation:

The Universal PUDO Engine database already existed.

Discussion revealed the risk of sharing it with the SaaS.

Decision:

One database per product.

Validated Structure:

universal_pudo

→ Core

universal_pudo_saas

→ SaaS

---

## Lesson 005

PostgreSQL Validation Prevents False Assumptions

Observation:

Initial debugging suggested a credential problem.

Root Cause:

The SaaS database did not exist yet.

Decision:

Always validate:

- PostgreSQL service
- credentials
- database existence

before modifying application code.

---

## Lesson 006

Documentation Must Be Updated Before Forward

Observation:

Several phases were technically complete but not documented.

Decision:

A phase is complete only after:

Development

↓

Validation

↓

Documentation

↓

Commit

↓

Push

↓

Forward

---

## Lesson 007

Core And SaaS Boundaries Must Stay Explicit

Observation:

Several implementation decisions naturally pushed toward higher coupling.

Decision:

The SaaS consumes the Core.

The SaaS never reimplements:

- providers
- carrier clients
- normalization
- carrier intelligence

---

# CURRENT PROJECT WORKFLOW

For every phase:

1. Production

2. Auto-Critique

3. Validation

4. Documentation Update

5. Commit

6. Push

7. Forward

No phase is considered complete before documentation synchronization.

---

# CURRENT PROJECT STATE

Completed:

✅ Documentation Foundation

✅ Repository Foundation

✅ Architecture Foundation

✅ ADR Foundation

✅ Domain Model Design

✅ Database Model Design

✅ Persistence Decisions

✅ Backend Foundation

✅ Database Configuration Foundation

✅ Alembic Foundation

---

Current Focus:

Organisation Foundation

---

# NEXT MILESTONE

Organisation Foundation

Objectives:

- Create Organisation ORM Model
- Create First Business Table
- Create First Alembic Migration
- Execute alembic revision --autogenerate
- Execute alembic upgrade head
- Validate End-To-End Persistence

---

# FUTURE MILESTONES

Organisation

↓

Membership

↓

Users

↓

Authentication

↓

Roles & Permissions

↓

Carrier Accounts

↓

Search Platform

↓

Map Experience

↓

Export Platform

↓

Administration

↓

Public API

↓

Frontend

↓

Universal PUDO SaaS v1.0.0

---

# LONG-TERM OBJECTIVE

Universal PUDO SaaS v1.0.0

An organisation can:

- authenticate
- manage users
- manage memberships
- manage carrier accounts
- search pickup points
- visualize results
- export results
- administer the platform

while Universal PUDO Engine remains the dedicated carrier intelligence layer.

---

# CHANGE HISTORY

2026-07-22

Initial Project Memory created.

---

2026-07-22

ADR Foundation completed.

---

2026-07-22

Backend Foundation completed.

---

2026-07-22

Database Configuration Foundation completed.

---

2026-07-23

Alembic Foundation completed.

---

2026-07-23

Dedicated SaaS PostgreSQL database created.

---

2026-07-23

Alembic successfully connected to PostgreSQL.

---

2026-07-23

Lessons Learned section added.

---

2026-07-23

Organisation Foundation defined as next milestone.
