# Universal PUDO SaaS - Search Platform Design

Version: 1.0.0

Status: Phase 16.1 Design Freeze

Last Updated: 2026-07-27

---

# PURPOSE

This document defines the Search Platform domain for Universal PUDO SaaS.

The objective of the Search Platform is to provide a stable SaaS-owned search experience layer on top of Universal PUDO Engine.

The Search Platform must:

- remain independent from carrier implementations
- consume Universal PUDO Engine search capabilities
- provide a single SaaS search entry point
- prepare future search-related features
- preserve Engine ownership boundaries

This document is the design authority for Phase 16.1.

No implementation may begin before this design is validated.

---

# DESIGN OBJECTIVES

The Search Platform exists to:

- standardize search requests
- standardize search results
- centralize SaaS search orchestration
- prepare future enrichment features
- protect the SaaS from carrier-specific concerns

The Search Platform is a SaaS concern.

Carrier execution remains an Engine concern.

---

# OWNERSHIP MODEL

## Universal PUDO SaaS Owns

- SearchRequest
- SearchResult
- SearchPlatformService
- Search experience
- Future filtering
- Future ranking
- Future enrichment
- Future export integration
- Future map integration

---

## Universal PUDO Engine Owns

- Carrier integrations
- Provider execution
- Carrier-level search execution
- Pickup point normalization
- Pickup point retrieval
- Carrier intelligence

---

# HIGH LEVEL ARCHITECTURE

```text
Frontend
    │
    ▼
SearchPlatformService
    │
    ▼
MultiCarrierSearchService
    │
    ▼
OrganisationSearchService
    │
    ▼
EngineSearchService
    │
    ▼
Universal PUDO Engine
```

---

# SEARCH PLATFORM BOUNDARY

The Search Platform is the official SaaS search entry point.

Future consumers must not directly call:

- OrganisationSearchService
- EngineSearchService

Instead:

```text
Frontend
    ↓
SearchPlatformService
```

becomes the official search boundary.

---

# SEARCH REQUEST

## Purpose

SearchRequest represents a user search intention.

SearchRequest is a business DTO.

SearchRequest is not a database model.

SearchRequest is not persisted.

---

## Proposed Structure

```python
SearchRequest
```

Attributes:

```text
organisation_id

query

country_code

postal_code

city

latitude

longitude

radius_km

carrier_codes

limit
```

---

## Responsibilities

SearchRequest centralizes:

- search filters
- location information
- carrier restrictions
- search options

It does not perform any execution.

---

# SEARCH RESULT

## Purpose

SearchResult represents the outcome of a platform search.

SearchResult is a business DTO.

SearchResult is not a database entity.

SearchResult is not persisted.

---

## Proposed Structure

```python
SearchResult
```

Attributes:

```text
pickup_points

total_results

executed_carriers

failed_carriers
```

---

## Responsibilities

SearchResult provides:

- unified search response
- execution visibility
- future enrichment support

SearchResult does not contain persistence logic.

---

# OUT OF SCOPE

Phase 16.1 must not define or implement:

- Python models
- Python services
- FastAPI routes
- SQLAlchemy models
- Alembic migrations
- database tables
- search persistence
- map rendering
- export generation
- ranking algorithm
- carrier-specific logic

Phase 16.1 is a design-only phase.

---

# SEARCH PLATFORM SERVICE

## Purpose

SearchPlatformService becomes the official SaaS search orchestration layer.

---

## Responsibilities

SearchPlatformService:

- accepts SearchRequest
- delegates execution
- consolidates SearchResult
- prepares enrichment
- prepares ranking
- prepares export support

---

## Non Responsibilities

SearchPlatformService must never:

- execute carrier APIs
- implement provider logic
- perform normalization
- own carrier metadata

These responsibilities belong to Universal PUDO Engine.

---

# FUTURE EXTENSIONS

The Search Platform is designed to support future capabilities.

---

## Phase 16.4

Search Result Enrichment

Examples:

- carrier labels
- grouping
- search metadata

---

## Phase 17

Map Experience

Examples:

- marker generation
- map presentation
- clustering preparation

---

## Phase 18

Export Platform

Examples:

- CSV export
- Excel export
- API export

---

# PERSISTENCE BOUNDARY

Phase 16 is explicitly non-persistent.

The Search Platform must not introduce:

- SearchRequest table
- SearchResult table
- SearchHistory table
- SearchExecution table
- Alembic migrations
- SQLAlchemy entities

---

## Allowed Artifacts

Phase 16 may introduce:

```text
SearchRequest DTO

SearchResult DTO

SearchPlatformService
```

Only.

---

# DESIGN PRINCIPLES

## P001

Search Platform is SaaS-owned.

---

## P002

Carrier execution is Engine-owned.

---

## P003

Search Platform remains provider-agnostic.

---

## P004

Search Platform remains non-persistent.

---

## P005

Search Platform becomes the single search entry point.

---

# PHASE 16.1 EXIT CRITERIA

Design phase is complete when:

- Search Platform scope is defined
- SearchRequest is defined
- SearchResult is defined
- SearchPlatformService is defined
- SaaS ownership boundaries are documented
- Engine ownership boundaries are documented
- Persistence boundary is documented
- Documentation is synchronized
- Phase 16.2 is ready

---

# NEXT PHASE

## Phase 16.2

Search Platform Models Foundation

Status:

Planned

Deliverables:

```text
search_platform/

├── __init__.py
├── models.py
```

Expected artifacts:

```text
SearchRequest

SearchResult
```

No persistence.

No API.

No migration.

No database changes.
