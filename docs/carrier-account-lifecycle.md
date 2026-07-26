# Carrier Account Lifecycle

Version: 1.0

Status: Draft

Last Updated: 2026-07-25

---

# Purpose

This document defines the business lifecycle of a Carrier Account.

A lifecycle describes:

- creation
- activation
- use
- credential updates
- deactivation
- deletion

---

# Lifecycle Overview

Draft
↓
Configured
↓
Validated
↓
Active
↓
Inactive
↓
Archived

---

# State: Draft

Purpose

Carrier Account has been created.

No credential has been configured.

Characteristics

- not usable
- not validated
- not active

Example

Carrier:
Mondial Relay

Account:
Production

Credentials:
Missing

---

# State: Configured

Purpose

Credentials have been stored.

Connectivity has not been verified.

Characteristics

- credentials present
- not tested
- not active

Example

API_KEY available

API_SECRET available

Connectivity unknown

---

# State: Validated

Purpose

Carrier connectivity successfully verified.

Characteristics

- credentials present
- connectivity verified
- ready for activation

---

# State: Active

Purpose

Carrier Account can be used by searches.

Characteristics

- activated
- available to services
- usable by Universal PUDO Engine

Only Active accounts should be used in production workflows.

---

# State: Inactive

Purpose

Carrier Account temporarily disabled.

Characteristics

- configuration preserved
- credentials preserved
- unavailable for searches

Examples

Contract suspended

Testing period

Temporary maintenance

---

# State: Archived

Purpose

Carrier Account retired.

Characteristics

- historical record preserved
- not usable
- not reactivated automatically

---

# Credential Lifecycle

No Credentials
↓
Credentials Stored
↓
Validation Attempt
↓
Validated Credentials
↓
Credential Rotation
↓
Revalidation

---

# Credential Rotation

Purpose

Replace sensitive carrier credentials.

Examples

- API key renewal
- password renewal
- account migration

Rules

Old credentials remain auditable.

New credentials require validation.

---

# Connectivity Validation

Purpose

Verify credentials against carrier systems.

Possible Results

Success

Failure

Unknown

Validation implementation is not part of this phase.

Only lifecycle rules are defined here.

---

# Ownership Rules

Organisation owns:

- Carrier Account

Carrier Account owns:

- Carrier Credentials

Platform owns:

- Carrier Integrations

Universal PUDO Engine consumes:

- validated Carrier Accounts

---

# Business Events

Create Carrier Account

Store Credentials

Update Credentials

Validate Connectivity

Activate Account

Deactivate Account

Archive Account

---

# Future Extensions

Not part of Phase 14.4

- automated credential testing
- scheduled validation
- audit logs
- approval workflow
- credential encryption
- secret vault integration

---

# Validation Criteria

Lifecycle Foundation is complete when:

- lifecycle states defined
- transitions defined
- credential lifecycle defined
- activation rules defined
- ownership rules verified
