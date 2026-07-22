# Universal PUDO SaaS - Architecture

Version: 0.2.0

Status: Phase 1 Documentation Review

Last Updated: 2026-07-22

---

# PURPOSE

This document defines the target architecture of Universal PUDO SaaS.

Its objectives are:

- support long-term SaaS growth
- preserve Core reusability
- maintain clear responsibility boundaries
- remain self-host compatible
- prevent architectural drift

This architecture describes the intended platform design prior to implementation.

Source code remains the final source of truth once development begins.

---

# ARCHITECTURAL PRINCIPLES

## Principle 1

Core First

Universal PUDO Engine remains the carrier intelligence layer.

The SaaS consumes the Core.

The SaaS never reimplements carrier integrations.

---

## Principle 2

Clear Responsibility Boundaries

Every capability has a single owner.

Responsibilities must not be duplicated between SaaS and Core.

---

## Principle 3

Multi-Tenant By Design

The platform is organisation-centric.

Every business object belongs to an organisation.

---

## Principle 4

SaaS First

The first delivery target is:

Multi-Tenant SaaS

The architecture remains compatible with future self-hosting.

---

## Principle 5

API First

The platform should not be designed exclusively around the web interface.

Long-term principle:

```text
UI
+
API
```

Capabilities should remain accessible through service contracts rather than only through screens.

---

## Principle 6

Security First

Credentials are considered sensitive assets.

Security considerations are architecture requirements, not future enhancements.

---

# CORE / SAAS BOUNDARY

---

## Core Responsibilities

Owned by Universal PUDO Engine.

```text
Carrier Integrations
Provider Implementations
ProviderFactory
Payload Mapping
Payload Parsing
Pickup Point Normalization
Hybrid Search
Synchronization
Carrier Abstractions
```

---

## SaaS Responsibilities

Owned by Universal PUDO SaaS.

```text
Authentication
Users
Organisations
Permissions
Carrier Credentials
Administration
Exports
Dashboards
Monitoring
```

---

## Forbidden SaaS Responsibilities

```text
Carrier API Clients
Carrier Parsers
Carrier Mappers
Provider Implementations
Carrier Synchronization
```

---

# HIGH LEVEL ARCHITECTURE

```text
┌─────────────────────┐
│      Browser        │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│       Next.js       │
│      Frontend       │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│       FastAPI       │
│      SaaS API       │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│ Application Layer   │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│  Core Adapter Layer │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│ Universal PUDO Core │
└─────────────────────┘

           │
           ▼

┌─────────────────────┐
│     PostgreSQL      │
└─────────────────────┘
```

---

# TECHNOLOGY STACK

## Frontend

```text
Next.js
React
TypeScript
```

Reason:

Long-term SaaS orientation.

---

## Backend

```text
FastAPI
```

Reason:

Alignment with Universal PUDO Engine.

---

## Database

```text
PostgreSQL
```

---

## ORM

```text
SQLAlchemy
Alembic
```

---

## Mapping

```text
Leaflet
OpenStreetMap
```

---

# MODULE BOUNDARIES

The SaaS application is expected to evolve around dedicated business modules.

---

## Module: Auth

Responsibilities:

```text
Authentication
Sessions
Password Management
Future SSO
```

---

## Module: Organisations

Responsibilities:

```text
Organisations
Memberships
Organisation Settings
```

---

## Module: Users

Responsibilities:

```text
Profiles
User Administration
```

---

## Module: Carrier Accounts

Responsibilities:

```text
Credential Storage
Connectivity Validation
Carrier Configuration
```

---

## Module: Searches

Responsibilities:

```text
Search Requests
Search History
Search Execution
```

---

## Module: Exports

Responsibilities:

```text
Data Export
Export History
```

---

## Module: Administration

Responsibilities:

```text
Platform Management
Diagnostics
Monitoring
```

---

# UNIVERSAL PUDO ENGINE DEPENDENCY STRATEGY

Repository:

```text
https://github.com/Vincecodeur/universal-pudo-engine
```

Current Version:

```text
v1.0.0
```

---

## Initial Strategy

Development Phase:

Git dependency

---

## Future Strategy

Potential migration to:

```text
PyPI dependency
```

or

```text
Private Package Registry
```

---

## Architectural Constraint

The SaaS must depend on public Core interfaces.

The SaaS must never directly consume:

```text
Provider internals
Internal parsers
Internal mappers
```

---

# CORE ADAPTER LAYER

A dedicated adapter layer must exist between SaaS services and the Core.

Target architecture:

```text
FastAPI
↓
Application Services
↓
Core Adapter
↓
Universal PUDO Engine
```

Benefits:

```text
Reduced coupling
Core replacement flexibility
Upgrade flexibility
```

---

# TENANCY MODEL

Relationship:

```text
Organisation
│
├── Users
├── Carrier Accounts
├── Searches
├── Exports
└── Permissions
```

All business objects belong to an organisation.

---

# STORAGE STRATEGY

Expected PostgreSQL ownership:

```text
Users
Organisations
Memberships
Carrier Accounts
Search History
Export History
Platform Settings
Audit Data
```

Database ownership may evolve.

The SaaS database must not duplicate Core carrier data.

---

# AUTHENTICATION ARCHITECTURE

V1:

```text
Email
Password
```

Future:

```text
Google
Azure AD
OIDC
SSO
```

Architecture must remain compatible with future additions.

---

# CREDENTIAL STORAGE STRATEGY

Credentials belong to the organisation.

The SaaS stores credentials.

The Core consumes credentials.

Required future properties:

```text
Encryption
Access Control
Auditability
```

---

# PUBLIC API STRATEGY

Current Delivery:

```text
UI First
```

Long-Term Architecture:

```text
UI
+
API
```

Future Public API should expose selected search and export capabilities.

Public API is not part of V1 scope.

---

# SECURITY ARCHITECTURE

Security Domains:

```text
Identity
Organisation Data
Carrier Credentials
Exports
Administration
```

Required Principles:

```text
Least Privilege
Role Segregation
Tenant Isolation
Credential Protection
Traceability
```

Future Features:

```text
MFA
Audit Logs
SSO
```

---

# SELF-HOSTED COMPATIBILITY CONSTRAINTS

The platform does not support self-hosting in V1.

However architecture must remain compatible.

Design Constraints:

```text
Environment-Based Configuration
External Secrets
Deployment Portability
Storage Independence
```

---

# FUTURE ADR CANDIDATES

ADR-0001

Core Dependency Strategy

---

ADR-0002

Authentication Strategy

---

ADR-0003

Credential Storage Strategy

---

ADR-0004

Module Boundary Strategy

---

ADR-0005

Public API Strategy

---

ADR-0006

Multi-Tenant Strategy

---

ADR-0007

Self-Hosted Compatibility Strategy

---

# CURRENT PROJECT STRUCTURE

```text
UNIVERSAL-PUDO-SAAS/
│
└── docs/
    ├── project-memory.md
    ├── product-vision.md
    ├── architecture.md
    ├── roadmap.md
    └── project-status.md
```

---

# NEXT STEP

Phase 1 Review Completion

Then:

Repository Foundation

---

# CHANGE HISTORY

2026-07-22

V1 created.

2026-07-22

V2 review consolidation applied.

Added:

- Module Boundaries
- Dependency Strategy
- Core Adapter Layer
- Storage Strategy
- Public API Strategy
- Security Architecture
- Self-Hosted Constraints# Universal PUDO SaaS - Architecture

Version: 0.2.0

Status: Phase 1 Documentation Review

Last Updated: 2026-07-22

---

# PURPOSE

This document defines the target architecture of Universal PUDO SaaS.

Its objectives are:

- support long-term SaaS growth
- preserve Core reusability
- maintain clear responsibility boundaries
- remain self-host compatible
- prevent architectural drift

This architecture describes the intended platform design prior to implementation.

Source code remains the final source of truth once development begins.

---

# ARCHITECTURAL PRINCIPLES

## Principle 1

Core First

Universal PUDO Engine remains the carrier intelligence layer.

The SaaS consumes the Core.

The SaaS never reimplements carrier integrations.

---

## Principle 2

Clear Responsibility Boundaries

Every capability has a single owner.

Responsibilities must not be duplicated between SaaS and Core.

---

## Principle 3

Multi-Tenant By Design

The platform is organisation-centric.

Every business object belongs to an organisation.

---

## Principle 4

SaaS First

The first delivery target is:

Multi-Tenant SaaS

The architecture remains compatible with future self-hosting.

---

## Principle 5

API First

The platform should not be designed exclusively around the web interface.

Long-term principle:

```text
UI
+
API
```

Capabilities should remain accessible through service contracts rather than only through screens.

---

## Principle 6

Security First

Credentials are considered sensitive assets.

Security considerations are architecture requirements, not future enhancements.

---

# CORE / SAAS BOUNDARY

---

## Core Responsibilities

Owned by Universal PUDO Engine.

```text
Carrier Integrations
Provider Implementations
ProviderFactory
Payload Mapping
Payload Parsing
Pickup Point Normalization
Hybrid Search
Synchronization
Carrier Abstractions
```

---

## SaaS Responsibilities

Owned by Universal PUDO SaaS.

```text
Authentication
Users
Organisations
Permissions
Carrier Credentials
Administration
Exports
Dashboards
Monitoring
```

---

## Forbidden SaaS Responsibilities

```text
Carrier API Clients
Carrier Parsers
Carrier Mappers
Provider Implementations
Carrier Synchronization
```

---

# HIGH LEVEL ARCHITECTURE

```text
┌─────────────────────┐
│      Browser        │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│       Next.js       │
│      Frontend       │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│       FastAPI       │
│      SaaS API       │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│ Application Layer   │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│  Core Adapter Layer │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│ Universal PUDO Core │
└─────────────────────┘

           │
           ▼

┌─────────────────────┐
│     PostgreSQL      │
└─────────────────────┘
```

---

# TECHNOLOGY STACK

## Frontend

```text
Next.js
React
TypeScript
```

Reason:

Long-term SaaS orientation.

---

## Backend

```text
FastAPI
```

Reason:

Alignment with Universal PUDO Engine.

---

## Database

```text
PostgreSQL
```

---

## ORM

```text
SQLAlchemy
Alembic
```

---

## Mapping

```text
Leaflet
OpenStreetMap
```

---

# MODULE BOUNDARIES

The SaaS application is expected to evolve around dedicated business modules.

---

## Module: Auth

Responsibilities:

```text
Authentication
Sessions
Password Management
Future SSO
```

---

## Module: Organisations

Responsibilities:

```text
Organisations
Memberships
Organisation Settings
```

---

## Module: Users

Responsibilities:

```text
Profiles
User Administration
```

---

## Module: Carrier Accounts

Responsibilities:

```text
Credential Storage
Connectivity Validation
Carrier Configuration
```

---

## Module: Searches

Responsibilities:

```text
Search Requests
Search History
Search Execution
```

---

## Module: Exports

Responsibilities:

```text
Data Export
Export History
```

---

## Module: Administration

Responsibilities:

```text
Platform Management
Diagnostics
Monitoring
```

---

# UNIVERSAL PUDO ENGINE DEPENDENCY STRATEGY

Repository:

```text
https://github.com/Vincecodeur/universal-pudo-engine
```

Current Version:

```text
v1.0.0
```

---

## Initial Strategy

Development Phase:

Git dependency

---

## Future Strategy

Potential migration to:

```text
PyPI dependency
```

or

```text
Private Package Registry
```

---

## Architectural Constraint

The SaaS must depend on public Core interfaces.

The SaaS must never directly consume:

```text
Provider internals
Internal parsers
Internal mappers
```

---

# CORE ADAPTER LAYER

A dedicated adapter layer must exist between SaaS services and the Core.

Target architecture:

```text
FastAPI
↓
Application Services
↓
Core Adapter
↓
Universal PUDO Engine
```

Benefits:

```text
Reduced coupling
Core replacement flexibility
Upgrade flexibility
```

---

# TENANCY MODEL

Relationship:

```text
Organisation
│
├── Users
├── Carrier Accounts
├── Searches
├── Exports
└── Permissions
```

All business objects belong to an organisation.

---

# STORAGE STRATEGY

Expected PostgreSQL ownership:

```text
Users
Organisations
Memberships
Carrier Accounts
Search History
Export History
Platform Settings
Audit Data
```

Database ownership may evolve.

The SaaS database must not duplicate Core carrier data.

---

# AUTHENTICATION ARCHITECTURE

V1:

```text
Email
Password
```

Future:

```text
Google
Azure AD
OIDC
SSO
```

Architecture must remain compatible with future additions.

---

# CREDENTIAL STORAGE STRATEGY

Credentials belong to the organisation.

The SaaS stores credentials.

The Core consumes credentials.

Required future properties:

```text
Encryption
Access Control
Auditability
```

---

# PUBLIC API STRATEGY

Current Delivery:

```text
UI First
```

Long-Term Architecture:

```text
UI
+
API
```

Future Public API should expose selected search and export capabilities.

Public API is not part of V1 scope.

---

# SECURITY ARCHITECTURE

Security Domains:

```text
Identity
Organisation Data
Carrier Credentials
Exports
Administration
```

Required Principles:

```text
Least Privilege
Role Segregation
Tenant Isolation
Credential Protection
Traceability
```

Future Features:

```text
MFA
Audit Logs
SSO
```

---

# SELF-HOSTED COMPATIBILITY CONSTRAINTS

The platform does not support self-hosting in V1.

However architecture must remain compatible.

Design Constraints:

```text
Environment-Based Configuration
External Secrets
Deployment Portability
Storage Independence
```

---

# FUTURE ADR CANDIDATES

ADR-0001

Core Dependency Strategy

---

ADR-0002

Authentication Strategy

---

ADR-0003

Credential Storage Strategy

---

ADR-0004

Module Boundary Strategy

---

ADR-0005

Public API Strategy

---

ADR-0006

Multi-Tenant Strategy

---

ADR-0007

Self-Hosted Compatibility Strategy

---

# CURRENT PROJECT STRUCTURE

```text
UNIVERSAL-PUDO-SAAS/
│
└── docs/
    ├── project-memory.md
    ├── product-vision.md
    ├── architecture.md
    ├── roadmap.md
    └── project-status.md
```

---

# NEXT STEP

Phase 1 Review Completion

Then:

Repository Foundation

---

# CHANGE HISTORY

2026-07-22

V1 created.

2026-07-22

V2 review consolidation applied.

Added:

- Module Boundaries
- Dependency Strategy
- Core Adapter Layer
- Storage Strategy
- Public API Strategy
- Security Architecture
- Self-Hosted Constraints
