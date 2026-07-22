# ADR-0002 - Authentication Strategy

Status: Accepted

Date: 2026-07-22

Authors:

- Vincent Gueret
- Microsoft Copilot

---

# Context

Universal PUDO SaaS is a multi-tenant platform.

The platform requires:

- user authentication
- organisation management
- permissions management
- future administration capabilities
- future API access

Authentication is a foundational architectural decision because it impacts:

- User Model
- Organisation Model
- Permissions
- Public API
- Security Architecture
- Future SSO integrations

The authentication strategy must support the current project scope while avoiding unnecessary complexity.

---

# Problem Statement

Which authentication strategy should be used for V1?

Option A

Email + Password

JWT authentication

---

Option B

External Identity Provider Only

Examples:

- Azure AD
- Google
- Okta

---

Option C

Hybrid Authentication

Email + Password

plus

External Identity Providers

from the beginning.

---

# Decision

Accepted Option:

Option A

Email + Password

with JWT Authentication.

---

# Rationale

The current project objective is to build:

Universal PUDO SaaS

The current objective is not to build:

an Identity Platform.

Option A provides:

- low implementation complexity
- high developer productivity
- predictable behaviour
- sufficient functionality for V1

while remaining compatible with future identity integrations.

---

# Authentication Model

Users authenticate using:

```text
Email
Password
```

Successful authentication produces:

```text
JWT Access Token
```

Future support for:

```text
Refresh Token
```

may be introduced later.

---

# User Identity Model

A user account contains:

```text
Email
Password Hash
Status
Organisation Memberships
Role
```

Passwords must never be stored in plain text.

Only password hashes may be stored.

---

# Session Strategy

V1 Strategy:

```text
JWT Access Token
```

The platform remains stateless.

No server-side session storage is required.

---

# API Compatibility

This authentication strategy supports future API development.

Future scenario:

```text
User
↓
Authentication
↓
JWT
↓
API Access
```

This is compatible with the API-first vision defined in product-vision.md.

---

# Organisation Compatibility

Authentication remains separate from organisation management.

Relationship:

```text
User
│
└── Membership
       │
       └── Organisation
```

A user may authenticate before organisation permissions are evaluated.

This separation simplifies future role management.

---

# Future Identity Provider Compatibility

The chosen strategy must not prevent adoption of:

```text
Azure AD
Google
OIDC
SSO
```

Future identity providers should be added as authentication mechanisms.

They should not require redesigning the user model.

---

# Rejected Alternatives

---

## Option B

External Identity Provider Only

Status:

Rejected

Reason:

Introduces unnecessary complexity.

Requires additional configuration and operational requirements.

Not justified for V1.

---

## Option C

Hybrid Authentication From Day One

Status:

Rejected

Reason:

Adds implementation complexity without immediate business value.

Can be introduced later without redesigning the architecture.

---

# Security Considerations

Passwords:

```text
Never Stored Plain Text
```

Requirements:

```text
Password Hashing
Credential Protection
Access Control
Tenant Isolation
```

Future possibilities:

```text
MFA
SSO
Audit Logs
```

---

# Positive Consequences

```text
Simple V1 implementation
Compatible with SaaS architecture
Compatible with Public API strategy
Compatible with future SSO
Compatible with future Azure AD
```

---

# Negative Consequences

```text
Password management remains our responsibility
Future SSO work still required
Future MFA work still required
```

These drawbacks are acceptable.

---

# Architectural Constraints

This ADR does not authorize:

```text
Custom Identity Provider Development
Authentication Logic Inside Frontend
Direct Permission Checks Inside UI Components
```

Authentication must remain a backend responsibility.

---

# Future Re-evaluation

This ADR should be revisited when:

```text
SSO becomes a requirement
Azure AD support is requested
Enterprise deployments appear
```

Current expectation:

The strategy remains valid throughout V1.

---

# Related Documents

- docs/project-memory.md
- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md
- docs/project-status.md

---

# Related Future ADRs

ADR-0003

Credential Storage Strategy

ADR-0005

Public API Strategy

ADR-0006

Multi-Tenant Strategy

---

# Status History

2026-07-22

Accepted.
