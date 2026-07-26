# Carrier Account Implementation Plan

Version: 1.0

Status: Draft

Last Updated: 2026-07-25

---

# Purpose

This document defines the implementation sequence for Phase 14.

The objective is to implement Carrier Account Management incrementally while maintaining:

- passing tests
- migration safety
- documentation synchronization
- PostgreSQL validation

---

# Implementation Philosophy

Implement from the most stable entity to the most dependent entity.

Order:

CarrierIntegration
↓
CarrierAccount
↓
CarrierCredential
↓
Services
↓
API
↓
Documentation
↓
Release Validation

---

# Phase 14.7

Carrier Account Foundation

Objective:

Implement the platform carrier catalog.

---

# Phase 14.8

Carrier Credential Foundation

Objective:

Implement organisation-owned carrier accounts.

Deliverables:

carrier_accounts/models.py

Migration:

create_carrier_accounts_table

Validation:

- FK organisation_id
- FK carrier_integration_id
- PostgreSQL validated
- Tests passing

---

# Phase 14.9

Carrier Credential Foundation

Objective:

Implement credential persistence.

Deliverables:

carrier_credentials/models.py

Migration:

create_carrier_credentials_table

Validation:

- FK carrier_account_id
- CRUD validated
- PostgreSQL validated
- Tests passing

---

# Phase 14.10

Persistence Test Foundation

Objective:

Validate persistence workflows.

Deliverables:

test_carrier_integration_persistence.py

test_carrier_account_persistence.py

test_carrier_credential_persistence.py

Validation:

- session.add()
- session.commit()
- session.refresh()
- session.get()
- session.delete()

---

# Phase 14.11

Repository Foundation

Objective:

Create repository layer.

Deliverables:

carrier_integrations/repository.py

carrier_accounts/repository.py

carrier_credentials/repository.py

Validation:

- CRUD operations tested
- Repository tests passing

---

# Phase 14.12

Service Foundation

Objective:

Implement business services.

Deliverables:

carrier_accounts/service.py

Capabilities:

- create account
- deactivate account
- activate account

Validation:

- Service tests
- Integration tests

---

# Phase 14.13

API Foundation

Objective:

Expose carrier accounts through FastAPI.

Endpoints:

POST /carrier-accounts

GET /carrier-accounts

GET /carrier-accounts/{id}

PATCH /carrier-accounts/{id}

Validation:

- API tests
- Authentication integration
- Permission checks

---

# Phase 14.14

Documentation Synchronization

Required Updates:

README.md

CHANGELOG.md

architecture.md

database-model.md

domain-model.md

project-status.md

project-memory.md

roadmap.md

Validation:

Documentation reviewed before commit.

---

# Phase 14 Completion Criteria

Carrier Account Management is complete when:

- Carrier Accounts implemented
- Carrier Credentials implemented
- Carrier Catalog integration implemented
- Persistence tests passing
- Repository layer implemented
- Services implemented
- API implemented
- PostgreSQL validated
- Documentation synchronized
- Commit created
- Push completed
