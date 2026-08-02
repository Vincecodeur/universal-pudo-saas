# ADR-0010 - Frontend Prioritization Before Export Platform

Status: Accepted

Date: 2026-08-02

Authors:
Universal PUDO SaaS Project

Decision Category:
Roadmap Prioritization

Related Documents:

- README.md
- CHANGELOG.md
- docs/architecture.md
- docs/product-vision.md
- docs/project-memory.md
- docs/project-status.md
- docs/roadmap.md
- docs/map-experience-closure.md

Supersedes:

None

Superseded By:

None

---

# PURPOSE

This ADR documents the decision to prioritize Frontend MVP before Export Platform.

The original roadmap positioned Export Platform immediately after Map Experience.

Following the completion of Phase 17 Map Experience, the roadmap was re-evaluated against actual business value, current product maturity, existing platform capabilities, and validated user needs.

The conclusion was that Frontend MVP provides significantly more immediate product value than Export Platform.

Export Platform remains part of the long-term roadmap but is deferred until after Observability And Audit.

---

# CONTEXT

At the end of Phase 17, Universal PUDO SaaS provides:

- authentication
- organisations
- memberships
- carrier accounts
- carrier credentials
- Search Platform
- SearchResult
- SearchExecutionMetadata
- MultiCarrierSearchService
- OrganisationSearchService
- Map Experience foundation
- MapProjectionResult
- MapMarker
- MapPopup
- MapViewState
- validated architecture
- validated boundaries
- fully tested backend foundations

The platform currently includes a mature backend foundation but does not yet provide a user-facing application.

The platform currently has:

- no frontend application
- no operational dashboard
- no audit platform
- no observability platform
- no reporting platform
- no analytics platform

Users cannot currently interact directly with:

- pickup point search
- pickup point visualization
- pickup point selection

despite these capabilities already existing inside the backend.

---

# PRODUCT VISION ALIGNMENT

Universal PUDO SaaS exists to provide:

- pickup point access
- pickup point search
- pickup point visualization
- pickup point consumption

The platform is intentionally focused on PUDO information access and consumption.

Frontend MVP directly supports that vision.

Frontend MVP allows users to:

- authenticate
- search pickup points
- visualize pickup points
- interact with maps
- consume search results
- select pickup points

Export Platform does not directly improve pickup point access, search, visualization or interaction at the current stage of product maturity.

Frontend MVP therefore provides a more direct path toward the core product vision.

---

# PROBLEM STATEMENT

The original roadmap positioned:

Phase 18 Export Platform

before:

Frontend implementation.

However no validated business requirement currently exists for Export Platform.

The following questions remain unanswered:

- who consumes exports?
- what data must be exported?
- why must that data be exported?
- what operational process depends on exports?
- what export formats are required?
- what business outcome is enabled by exports?

At the same time:

- Search Platform exists
- Map Experience exists
- SearchResult exists
- MapProjectionResult exists

but no user-facing experience exists.

This creates an imbalance between backend maturity and product usability.

---

# DECISION

Frontend MVP becomes the next implementation phase.

Export Platform is deferred.

The roadmap is updated as follows:

Phase 18 Frontend MVP

Phase 19 Administration Portal

Phase 20 Public API

Phase 21 Observability And Audit

Phase 22 Export Platform

Phase 23 Security Hardening

Export Platform moves from Phase 18 to Phase 22.

Frontend MVP becomes the first implementation phase after Phase 17 closure.

---

# BUSINESS RATIONALE

Frontend MVP creates immediate user-facing value.

Frontend MVP enables:

- product demonstrations
- UX validation
- search workflow validation
- map interaction validation
- stakeholder demonstrations
- future customer onboarding
- product adoption

Frontend MVP allows users to perform meaningful business workflows.

Export Platform does not currently solve a validated operational problem.

The current platform does not yet produce:

- observability reports
- audit events
- dashboard analytics
- operational reporting
- carrier performance reporting

As a result, Export Platform lacks validated export consumers and validated export datasets.

Frontend MVP therefore provides a better return on implementation effort.

---

# ALTERNATIVES CONSIDERED

Alternative A

Keep Export Platform in Phase 18.

Decision:

Rejected.

Reason:

- no validated export consumer
- no validated export workflow
- no validated reporting requirement
- limited immediate value

---

Alternative B

Remove Export Platform from the roadmap.

Decision:

Rejected.

Reason:

Export remains a valid long-term capability.

Deferral is preferred over removal.

---

Alternative C

Move Frontend MVP before Export Platform.

Decision:

Accepted.

Reason:

Frontend MVP delivers immediate and visible product value.

---

# EXPECTED BENEFITS

Frontend MVP will provide:

- user-visible product progress
- usable product workflows
- UX feedback opportunities
- stakeholder demonstrations
- future onboarding support
- higher confidence in future roadmap decisions

The platform becomes usable before additional support capabilities are developed.

---

# ROADMAP IMPACT

Previous Roadmap

Phase 18 Export Platform

Phase 19 Administration Portal

Phase 20 Public API

Phase 21 Observability And Audit

Phase 22 Security Hardening

Phase 23 Frontend

Updated Roadmap

Phase 18 Frontend MVP

Phase 19 Administration Portal

Phase 20 Public API

Phase 21 Observability And Audit

Phase 22 Export Platform

Phase 23 Security Hardening

---

# ARCHITECTURAL IMPACT

No architectural boundary changes.

No database changes.

No migration changes.

No Universal PUDO Engine changes.

No SearchResult changes.

No MapProjectionResult changes.

No MapService changes.

No authentication changes.

No tenancy changes.

No API contract changes.

This decision affects roadmap sequencing only.

Existing architecture remains valid.

---

# NON-GOALS

This ADR does not:

- redesign Search Platform
- redesign Map Experience
- redesign SearchResult
- redesign MapProjectionResult
- redesign MapService
- redesign authentication
- redesign tenancy
- redesign carrier account management
- introduce persistence
- create new database entities
- create database migrations
- modify Universal PUDO Engine
- remove Export Platform

Export Platform remains part of the roadmap.

---

# RISKS

Risk 1

Frontend complexity before Administration Portal.

Mitigation:

Frontend MVP remains limited to:

- authentication
- search consumption
- map consumption
- pickup point interaction

Administration remains Phase 19.

---

Risk 2

Export requirements may emerge before Phase 22.

Mitigation:

Export Platform remains in the roadmap and may be reprioritized if a validated business need appears.

---

Risk 3

Frontend implementation creates pressure for backend redesign.

Mitigation:

The following contracts remain frozen:

- SearchResult
- MapProjectionResult
- MapService

No backend redesign is authorized by this ADR.

---

Risk 4

Roadmap drift after reprioritization.

Mitigation:

All documentation must be synchronized before Phase 18 begins.

---

# EXPORT PLATFORM FUTURE POSITION

Export Platform remains planned.

Export Platform will be revisited during Phase 22.

Before implementation, Phase 22 must validate:

- export consumers
- export use cases
- export datasets
- export formats
- reporting requirements
- audit export requirements
- analytics export requirements

Export Platform must be driven by real platform usage rather than assumptions.

---

# PHASE 18 DEFINITION

Phase 18

Frontend MVP

Objectives:

- create frontend application foundation
- create authentication-aware frontend shell
- create application routing foundation
- create navigation foundation
- prepare pickup point search workflow
- consume Search Platform
- consume SearchResult through existing APIs
- consume MapProjectionResult
- display pickup points
- render markers
- render popups
- implement pickup point selection
- preserve backend boundaries
- preserve SearchResult contract
- preserve MapService contract
- preserve MapProjectionResult contract
- avoid backend persistence changes
- avoid Universal PUDO Engine modifications

Expected Deliverables:

- frontend repository structure
- frontend architecture documentation
- application shell
- routing foundation
- authentication-aware layout
- search interface foundation
- map interface foundation
- frontend integration strategy
- frontend documentation

---

# SUCCESS CRITERIA

This roadmap reprioritization is successful when:

- Phase 18 Frontend MVP begins
- Frontend consumes existing Search Platform capabilities
- Frontend consumes existing Map Experience capabilities
- SearchResult remains unchanged
- MapProjectionResult remains unchanged
- MapService remains unchanged
- no backend redesign is required
- Export Platform remains deferred to Phase 22
- documentation remains synchronized

---

# VALIDATION CRITERIA

This ADR is considered implemented when:

- roadmap.md is updated
- README.md is updated
- project-memory.md is updated
- project-status.md is updated
- architecture.md is updated
- product-vision.md is updated
- CHANGELOG.md is updated
- map-experience-closure.md is updated

Documentation must consistently reference:

Phase 18 Frontend MVP

Phase 22 Export Platform

---

# CONSEQUENCES

Positive

- immediate user-facing value
- faster product validation
- better demonstrations
- improved UX feedback loop
- improved roadmap alignment
- reduced risk of premature export architecture

Negative

- export capabilities arrive later
- export use cases remain deferred
- reporting-related exports remain unavailable until later phases

Accepted.

---

# FINAL DECISION

Frontend MVP becomes the next implementation phase.

Export Platform is postponed until Phase 22.

Approved Roadmap:

Phase 18 Frontend MVP

Phase 19 Administration Portal

Phase 20 Public API

Phase 21 Observability And Audit

Phase 22 Export Platform

Phase 23 Security Hardening

Status:

ACCEPTED

---

# CHANGE HISTORY

2026-08-02

Initial ADR created.

Decision:

- Move Frontend MVP before Export Platform
- Move Export Platform to Phase 22

Status:

Accepted.

Prepared:

- Phase 18 Frontend MVP
- Roadmap synchronization
- Documentation synchronization
- Phase 18 planning preparation
