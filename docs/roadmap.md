# Universal PUDO SaaS - Roadmap

Version: 0.2.0

Status: Phase 1 Documentation Review

Last Updated: 2026-07-22

---

# ROADMAP PHILOSOPHY

This roadmap is not a task list.

It is an execution roadmap used to guide architectural and product development decisions.

The objective is to build a production-grade SaaS platform on top of Universal PUDO Engine while preserving:

- Core independence
- SaaS scalability
- Self-host compatibility
- Security
- Maintainability

Every phase must produce:

- clear deliverables
- documented decisions
- validated architecture
- updated documentation

---

# PROJECT COMPLETION CRITERIA

The project is considered successful when an organisation can:

- create an account
- authenticate
- manage users
- connect carrier accounts
- search pickup points
- visualize pickup points
- export search results
- administer the platform

using Universal PUDO Engine as the carrier integration layer.

---

# PHASE 1

Documentation Foundation

Status:

Documentation Review

Goal:

Create and validate project foundations before implementation.

---

## Deliverables

project-memory.md

product-vision.md

architecture.md

roadmap.md

project-status.md

---

## Definition Of Done

- all documents created
- all documents reviewed
- review findings integrated
- project vision validated
- architecture validated

---

# PHASE 2

Repository Foundation

Goal:

Create repository foundations.

No business implementation.

---

## Deliverables

Git initialization

README

.gitignore

Backend initialization

Frontend initialization

Base project configuration

---

## Success Criteria

Frontend starts successfully.

Backend starts successfully.

No business functionality exists yet.

---

# PHASE 3

Architecture Foundation

Goal:

Implement the architectural skeleton.

---

## Deliverables

Backend structure

Frontend structure

Service layer structure

Core adapter foundation

Configuration strategy

---

## Success Criteria

Architecture visible in code.

No business logic implemented.

---

# PHASE 4

ADR Foundation

Goal:

Formalize major architectural decisions before business development.

---

## Expected ADRs

ADR-0001
Core Dependency Strategy

ADR-0002
Authentication Strategy

ADR-0003
Credential Storage Strategy

ADR-0004
Module Boundary Strategy

ADR-0005
Public API Strategy

ADR-0006
Multi-Tenant Strategy

---

## Success Criteria

All foundational ADRs approved.

---

# PHASE 5

Domain Model Design

Goal:

Design the business model.

No implementation.

---

## Deliverables

Organisation Model

User Model

Role Model

Carrier Account Model

Search Model

Export Model

Administration Model

---

## Success Criteria

Business entities validated.

Responsibilities clearly defined.

---

# PHASE 6

Database Model Design

Goal:

Design persistence before coding features.

---

## Deliverables

Entity Relationships

Database Schema

Migration Strategy

Index Strategy

Multi-Tenant Model

---

## Success Criteria

Database structure validated.

No major open modeling questions remain.

---

# PHASE 7

Authentication

Goal:

Secure platform access.

---

## Features

Register

Login

Logout

Password Reset

Session Management

---

## Future Compatibility

OIDC

Azure AD

Google

SSO

---

## Success Criteria

Users can authenticate.

Protected routes operational.

---

# PHASE 8

Organisation Management

Goal:

Introduce tenancy.

---

## Features

Organisation Creation

Organisation Management

Membership Management

Invitations

---

## Success Criteria

All users belong to organisations.

---

# PHASE 9

Roles And Permissions

Goal:

Implement platform security model.

---

## Roles

Super Admin

Organisation Admin

Organisation User

---

## Success Criteria

Role restrictions enforced.

Tenant isolation verified.

---

# PHASE 10

Carrier Account Management

Goal:

Connect carrier credentials.

---

## Supported V1

Colissimo

Mondial Relay

Chronopost

---

## Features

Add Account

Edit Account

Disable Account

Credential Validation

Connectivity Tests

---

## V1 Limitation

One carrier account per carrier per organisation.

---

## Success Criteria

Carrier credentials usable.

Secure storage implemented.

---

# PHASE 11

Universal PUDO Engine Integration

Goal:

Connect SaaS and Core.

---

## Repository

Universal PUDO Engine

Current known version:

v1.0.0

---

## Deliverables

Dependency Integration

Core Adapter Layer

Search Adapter

Error Handling

Version Management

---

## Success Criteria

SaaS consumes Core.

No duplicated carrier logic.

---

# PHASE 12

Search Platform

Goal:

Expose pickup point capabilities.

---

## Features

Postal Code Search

City Search

Coordinate Search

Carrier Filter

Multi-Carrier Search

---

## Success Criteria

Searches execute successfully.

Results normalized by Core.

---

# PHASE 13

Map Experience

Goal:

Visual pickup point exploration.

---

## Technology

Leaflet

OpenStreetMap

---

## Features

Markers

Carrier Identification

Pickup Point Details

Navigation Support

---

## Success Criteria

Map experience operational.

---

# PHASE 14

Export Platform

Goal:

Operational reuse of search results.

---

## Candidate Formats

CSV

Excel

JSON

---

## Success Criteria

Users can download reusable exports.

---

# PHASE 15

Public API Foundation

Goal:

Prepare API-first evolution.

---

## Deliverables

API Strategy

API Security

API Versioning

Usage Model

API Documentation

---

## Success Criteria

Platform ready for future external consumption.

---

# PHASE 16

Administration Portal

Goal:

Provide platform governance.

---

## Features

Organisation Management

User Management

Search Monitoring

Carrier Monitoring

Diagnostics

---

## Success Criteria

Super Admin functionality operational.

---

# PHASE 17

Observability And Audit

Goal:

Prepare operational usage.

---

## Features

Audit Events

Error Tracking

Search Monitoring

Operational Diagnostics

---

## Success Criteria

Platform behaviour observable.

---

# PHASE 18

Testing And Quality

Goal:

Establish long-term quality framework.

---

## Deliverables

Unit Testing

Integration Testing

API Testing

Security Verification

Test Coverage Metrics

---

## Success Criteria

Quality framework established.

---

# PHASE 19

Security Hardening

Goal:

Strengthen platform security.

---

## Candidate Features

MFA

Audit Logs

Advanced Session Controls

Secret Rotation

Credential Security Review

---

## Success Criteria

Security review completed.

---

# PHASE 20

Core Upgrade Strategy

Goal:

Prepare future Core evolution.

---

## Topics

Version Tracking

Dependency Upgrades

Compatibility Validation

Upgrade Procedure

Rollback Strategy

---

## Success Criteria

Core evolution process documented.

---

# PHASE 21

Release Preparation

Goal:

Prepare V1 release.

---

## Activities

Architecture Review

Security Review

Performance Review

Documentation Review

Dependency Review

---

## Success Criteria

Release Candidate validated.

---

# PHASE 22

Universal PUDO SaaS v1.0.0

Goal:

First production release.

---

## Deliverables

Git Tag

Release Notes

Documentation

Deployment Package

---

## Success Criteria

Universal PUDO SaaS v1.0.0 released.

---

# POST V1 BACKLOG

Items intentionally postponed.

---

## Billing

Status:

Backlog

Reason:

Business model not yet decided.

---

## Multiple Carrier Accounts

Status:

Backlog

Example:

Multiple Colissimo accounts per organisation.

---

## SSO

Status:

Backlog

---

## Self Hosted Deployment

Status:

Backlog

Architecture prepared.

Implementation postponed.

---

## Analytics

Status:

Backlog

---

## Recommendation Engine

Status:

Backlog

---

## Webhooks

Status:

Backlog

---

# PHASE REVIEW RULE

At the end of every phase:

1. validate deliverables
2. validate architecture
3. update project-status.md
4. update project-memory.md
5. update ADRs
6. identify lessons learned
7. validate next phase

---

# DEFINITION OF DONE

A phase is complete only when:

- implementation completed
- documentation updated
- tests pass
- ADRs updated when required
- next phase validated

---

# CURRENT PHASE

Phase:

1

Name:

Documentation Foundation

Status:

Documentation Review

Next Milestone:

Phase 1 Validation

---

# CHANGE HISTORY

2026-07-22

V1 created.

2026-07-22

V2 review consolidation applied.

Added:

- ADR Phase
- Domain Model Phase
- Database Model Phase
- Public API Phase
- Testing Strategy
- Core Upgrade Strategy
