# Universal PUDO SaaS - Leaflet Component Foundation

Version: 1.0.0

Status: Phase 17.5 Planning Freeze

Last Updated: 2026-07-30

---

# PURPOSE

This document defines the first frontend-facing Leaflet component foundation for Universal PUDO SaaS.

The objective of Phase 17.5 is to prepare the future map rendering layer that consumes MapProjectionResult.

Leaflet Component Foundation must remain a presentation-layer concern.

It must not introduce business search logic.

It must not modify SearchResult.

It must not modify MapService.

It must not modify Universal PUDO Engine.

---

# ARCHITECTURAL POSITION

```text
SearchResult
        ↓
MapService
        ↓
MapProjectionResult
        ↓
Leaflet Component Foundation
        ↓
Leaflet Map Rendering
```

The Leaflet component consumes:

```text
MapProjectionResult
```

The Leaflet component must not consume:

```text
SearchResult
Universal PUDO Engine
EngineSearchService
OrganisationSearchService
MultiCarrierSearchService
CarrierCatalogService
```

---

# PHASE OBJECTIVES

Phase 17.5 defines the first frontend-facing map component foundation.

The phase prepares:

- Leaflet map component structure
- MapProjectionResult consumption strategy
- MapMarker rendering strategy
- MapPopup rendering strategy
- marker click handling
- single selection handling
- popup opening and closing behavior
- empty map state strategy
- frontend-only responsibility boundary

Phase 17.5 must preserve all boundaries defined in Phase 17.4.

---

# INPUT CONTRACT

The only accepted input contract is:

```text
MapProjectionResult
```

MapProjectionResult contains:

```text
markers
popups
view_state
total_markers
executed_carriers
failed_carriers
```

The frontend must treat MapProjectionResult as a presentation contract.

The frontend must not reinterpret SearchResult.

The frontend must not rebuild business search results.

---

# MARKER INPUT

Markers are consumed from:

```text
MapProjectionResult.markers
```

Each MapMarker contains:

```text
pickup_point_id
latitude
longitude
carrier_code
carrier_display_name
carrier_logo_url
carrier_color
```

Each MapMarker may produce one Leaflet marker.

---

# POPUP INPUT

Popups are consumed from:

```text
MapProjectionResult.popups
```

Each MapPopup contains:

```text
pickup_point_id
pickup_point_name
carrier
address
distance
opening_hours
details_link
```

A popup is resolved by:

```text
pickup_point_id
```

The Leaflet component must not create popup data from SearchResult.

---

# VIEW STATE INPUT

View state is consumed from:

```text
MapProjectionResult.view_state
```

MapViewState may expose:

```text
map_center
map_zoom
user_location
selected_pickup_point_id
visible_carriers
```

Phase 17.5 does not persist map view state.

MapViewState remains frontend interaction state.

---

# PROPOSED FRONTEND STRUCTURE

The future frontend structure may include:

```text
frontend/
└── map/
    ├── components/
    │   └── LeafletMap.tsx
    ├── adapters/
    │   └── leafletAdapter.ts
    ├── types/
    │   └── mapProjection.ts
    └── __tests__/
        └── LeafletMap.test.tsx
```

This structure is proposed for frontend implementation.

No backend package should be modified for Leaflet rendering.

---

# LEAFLET MAP COMPONENT

## Purpose

The Leaflet map component renders a map from MapProjectionResult.

## Responsibility

The component owns:

```text
map display
marker rendering
popup rendering
marker click handling
selection display
empty state display
```

The component does not own:

```text
search execution
carrier filtering business rules
carrier account activation
carrier credentials
pickup point normalization
database persistence
```

---

# LEAFLET ADAPTER

## Purpose

The Leaflet adapter translates presentation data into Leaflet-specific rendering instructions.

## Input

```text
MapProjectionResult
```

## Output

```text
Leaflet marker configuration
Leaflet popup configuration
Leaflet map view configuration
```

## Constraint

The adapter must not modify the input MapProjectionResult.

---

# MARKER RENDERING STRATEGY

## Rendering Rule

```text
MapMarker
        ↓
Leaflet Marker
```

One MapMarker produces one Leaflet marker.

## Marker Identity

The stable marker identity is:

```text
pickup_point_id
```

## Marker Coordinates

Leaflet marker coordinates come from:

```text
latitude
longitude
```

If latitude or longitude is missing, the marker must not be rendered.

The invalid marker should not crash the whole map.

---

# POPUP RENDERING STRATEGY

## Rendering Rule

```text
MapPopup
        ↓
Leaflet Popup
```

The popup is linked to a marker through:

```text
pickup_point_id
```

## Popup Content

The popup may display:

```text
pickup_point_name
carrier
address
distance
opening_hours
details_link
carrier_logo_url
carrier_color
```

Carrier logo and carrier color may be provided through the related marker.

---

# SELECTION STRATEGY

Only one pickup point may be selected at a time.

Selection is represented by:

```text
MapViewState.selected_pickup_point_id
```

## Selection Workflow

```text
User clicks marker
        ↓
Selected pickup point changes
        ↓
Popup opens
```

## Replacement Workflow

```text
Current selected pickup point
        ↓
User clicks another marker
        ↓
Previous selection replaced
```

## Reset Workflow

```text
New MapProjectionResult
        ↓
Selected pickup point not found in markers
        ↓
Selection reset
```

---

# EMPTY STATE STRATEGY

If MapProjectionResult contains no markers:

```text
markers = []
total_markers = 0
```

The component should display an empty map state.

The frontend may display a message such as:

```text
No pickup points available for this search.
```

This is a presentation decision.

No backend change is required.

---

# CARRIER BRANDING RENDERING

The component may use:

```text
carrier_logo_url
carrier_color
carrier_display_name
```

from MapMarker.

Carrier branding rules remain owned by SaaS Administration.

The Leaflet component only renders branding values already provided by the backend projection.

---

# MAP REFRESH STRATEGY

When a new MapProjectionResult is received:

```text
Existing rendered markers removed
        ↓
Existing popups closed
        ↓
New markers rendered
        ↓
Map view refreshed
```

Phase 17.5 does not require incremental diffing.

Full refresh is acceptable.

---

# ERROR HANDLING STRATEGY

The component should avoid crashing when optional data is missing.

Examples:

```text
missing carrier_logo_url
missing carrier_color
missing opening_hours
missing details_link
```

These missing optional fields should not prevent marker rendering.

Missing coordinates should prevent only the affected marker from rendering.

---

# OUT OF SCOPE

Phase 17.5 does not include:

```text
backend API routes
search execution logic
SearchResult changes
MapService changes
SQLAlchemy models
Alembic migrations
PostgreSQL changes
Universal PUDO Engine changes
carrier administration UI
marker clustering
routing
turn-by-turn navigation
geocoding
reverse geocoding
analytics persistence
map preference persistence
production styling
advanced responsive layout
```

---

# VALIDATED BOUNDARIES

Phase 17.5 must preserve:

```text
SearchResult remains the business contract
MapProjectionResult remains the presentation contract
Leaflet consumes MapProjectionResult
MapService remains the backend projection layer
Leaflet remains a frontend rendering layer
No MapSearchResult
No MapPickupPoint
No persistence
No SQLAlchemy
No Alembic migration
No Engine modification
```

---

# SUCCESS CRITERIA

Phase 17.5 Planning Freeze is complete when:

```text
Leaflet component responsibility is defined
MapProjectionResult consumption is defined
marker rendering strategy is defined
popup rendering strategy is defined
selection strategy is defined
empty state strategy is defined
branding rendering strategy is defined
map refresh strategy is defined
out-of-scope boundaries are documented
Phase 17.6 is identified
```

---

# NEXT PHASE

## Phase 17.6 - Map Experience Validation

Expected focus:

```text
Validate the complete Map Experience foundation.
Validate SearchResult boundary.
Validate MapService boundary.
Validate MapProjectionResult consumption.
Validate Leaflet rendering strategy.
Validate marker lifecycle.
Validate popup lifecycle.
Validate selection lifecycle.
Confirm no persistence introduced.
Confirm no Engine modification introduced.
Synchronize documentation.
Prepare Phase 17 closure.
```

Phase 17.6 must not start until Phase 17.5 is validated, documented, committed and pushed.

---

# RELATED DOCUMENTS

- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md
- docs/project-memory.md
- docs/project-status.md
- docs/map-experience-design.md
- docs/map-models-foundation.md
- docs/leaflet-integration-design.md
- backend/src/universal_pudo_saas/map_service/models.py
- backend/src/universal_pudo_saas/map_service/service.py

---

# CHANGE HISTORY

2026-07-30

Initial Leaflet Component Foundation created.

Defined:

- Leaflet component responsibility
- MapProjectionResult input contract
- MapMarker rendering strategy
- MapPopup rendering strategy
- MapViewState usage
- selection lifecycle
- empty state strategy
- carrier branding rendering
- map refresh strategy
- frontend responsibility boundary
- backend boundary preservation
- out-of-scope implementation rules
- Phase 17.6 as next phase
