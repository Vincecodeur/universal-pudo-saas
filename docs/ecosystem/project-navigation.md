# Project Navigation

Version: 1.0

Status: Accepted

Last Updated: 2026-07-26

Location:

docs/ecosystem/project-navigation.md

---

# Purpose

This document exists to prevent confusion between:

- universal-pudo-engine
- universal-pudo-saas

When a new idea, feature, bug, or architectural discussion appears, this document helps determine where the work belongs.

---

# Repositories

## Universal PUDO Engine

Repository:

universal-pudo-engine

Role:

Reusable Core

Owns:

- carrier integrations
- providers
- provider factory
- pickup point search
- pickup point normalization
- synchronization
- hybrid search
- provider health
- carrier capabilities
- carrier lifecycle

Does NOT own:

- users
- organisations
- memberships
- authentication
- carrier credentials
- carrier accounts
- administration
- frontend

---

## Universal PUDO SaaS

Repository:

universal-pudo-saas

Role:

SaaS Product

Owns:

- users
- organisations
- memberships
- authentication
- permissions
- carrier accounts
- carrier credentials
- administration
- dashboards
- frontend

Does NOT own:

- carrier integrations
- provider implementations
- provider mapping
- carrier normalization

---

# Quick Decision Matrix

Question:

Add a new carrier integration

Repository:

universal-pudo-engine

---

Question:

Fix a carrier provider

Repository:

universal-pudo-engine

---

Question:

Add a carrier capability

Repository:

universal-pudo-engine

---

Question:

Change pickup point normalization logic

Repository:

universal-pudo-engine

---

Question:

Create a Carrier Account

Repository:

universal-pudo-saas

---

Question:

Store carrier credentials

Repository:

universal-pudo-saas

---

Question:

Add authentication

Repository:

universal-pudo-saas

---

Question:

Add organisation management

Repository:

universal-pudo-saas

---

Question:

Add user permissions

Repository:

universal-pudo-saas

---

Question:

Add administration screens

Repository:

universal-pudo-saas

---

Question:

Define how the SaaS consumes Engine data

Location:

docs/ecosystem/

---

Question:

Define Engine ↔ SaaS responsibilities

Location:

docs/ecosystem/

---

Question:

Define Engine ↔ SaaS integration rules

Location:

docs/ecosystem/

---

# Navigation Rule

Before starting any work, identify the active scope.

Examples:

[REPOSITORY ACTIF]
universal-pudo-engine

or

[REPOSITORY ACTIF]
universal-pudo-saas

or

[SUJET]
ENGINE ↔ SAAS CONTRACT

No implementation should begin without identifying the active scope.

---

# Golden Rule

If the topic concerns:

carrier behavior

↓

universal-pudo-engine

If the topic concerns:

user experience
configuration
administration
credentials

↓

universal-pudo-saas

If the topic concerns:

how SaaS consumes Engine capabilities

↓

docs/ecosystem/

---

# Decision Summary

universal-pudo-engine owns carrier functionality.

universal-pudo-saas owns SaaS functionality.

docs/ecosystem owns the Engine ↔ SaaS contract documentation.

When uncertain:

Carrier concern → Engine

User concern → SaaS

Integration concern → Ecosystem contract
