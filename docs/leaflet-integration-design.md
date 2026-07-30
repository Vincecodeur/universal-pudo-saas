# Universal PUDO SaaS - Leaflet Integration Design

Version: 1.0.0

Status: Phase 17.4 Planning Freeze

Last Updated: 2026-07-30

---

# PURPOSE

This document defines how MapProjectionResult will be displayed using Leaflet.

The objective is to connect the existing Map Service layer to a future map user experience.

Leaflet is a presentation technology.

Leaflet must not become a business layer.

---

# ARCHITECTURAL POSITION

```text
SearchResult
        ↓
MapService
        ↓
MapProjectionResult
        ↓
Leaflet Adapter
        ↓
Leaflet Map
```

Leaflet consumes MapProjectionResult.

Leaflet does not consume SearchResult directly.

Leaflet does not consume Universal PUDO Engine directly.

---

# PHASE OBJECTIVES

Phase 17.4 defines:

- Leaflet integration strategy
- marker rendering strategy
- popup rendering strategy
- carrier logo display strategy
- map refresh strategy
- selection lifecycle strategy
- frontend ownership boundary
- out-of-scope implementation boundaries

Phase 17.4 prepares future frontend implementation.

Phase 17.4 does not implement a frontend yet unless explicitly planned in a later phase.

---

# OWNERSHIP MODEL

## Universal PUDO SaaS Backend Owns

- SearchResult
- MapService
- MapProjectionResult
- MapMarker
- MapPopup
- MapViewState

## Universal PUDO SaaS Frontend Will Own

- Leaflet map rendering
- marker display
- popup display
- user click handling
- visual map state
- future frontend interaction state

## Universal PUDO Engine Owns

- carrier provider execution
- pickup point retrieval
- pickup point normalization
- carrier definitions
- carrier capabilities

Leaflet must never access Universal PUDO Engine directly.

---

# LEAFLET CONSUMPTION RULE

Leaflet must consume:

```text
MapProjectionResult
```

Leaflet must not consume:

```text
SearchResult
Universal PUDO Engine
EngineSearchService
MultiCarrierSearchService
OrganisationSearchService
CarrierCatalogService
```

Reason:

MapProjectionResult is the presentation contract prepared by the SaaS backend.

SearchResult remains the business contract.

Leaflet remains a rendering layer.

---

# MARKER LIFECYCLE

## Input

Leaflet receives markers from:

```text
MapProjectionResult.markers
```

Each marker contains:

```text
pickup_point_id
latitude
longitude
carrier_code
carrier_display_name
carrier_logo_url
carrier_color
```

## Rendering Rule

One MapMarker produces one Leaflet marker.

```text
MapMarker
        ↓
Leaflet Marker
```

## Marker Identity

The stable marker identifier is:

```text
pickup_point_id
```

## Marker Refresh Strategy

When a new MapProjectionResult is received:

```text
Existing markers removed
        ↓
New markers rendered
```

No incremental marker update is required in the first Leaflet integration phase.

Full refresh is acceptable.

---

# POPUP LIFECYCLE

## Input

Leaflet receives popup data from:

```text
MapProjectionResult.popups
```

Each popup contains:

```text
pickup_point_id
pickup_point_name
carrier
address
distance
opening_hours
details_link
```

## Popup Opening

A popup opens when the user selects a marker.

```text
User clicks marker
        ↓
pickup_point_id identified
        ↓
MapPopup retrieved
        ↓
Popup rendered
```

## Popup Closing

A popup closes when:

```text
User closes popup
or
New MapProjectionResult is loaded
or
Selected pickup point is reset
```

---

# CARRIER LOGO STRATEGY

Carrier logos are provided through:

```text
MapMarker.carrier_logo_url
```

Carrier logo ownership remains with:

```text
SaaS Administration
```

Leaflet may display carrier logos in:

```text
marker popup
future carrier legend
future carrier filter panel
```

Leaflet must not manage carrier branding configuration.

Leaflet must not persist carrier branding.

Leaflet must not define carrier branding rules.

---

# CARRIER COLOR STRATEGY

Carrier colors are provided through:

```text
MapMarker.carrier_color
```

Carrier colors may be used for:

```text
marker styling
popup accent color
future carrier legend
future carrier filter UI
```

If no carrier color is provided, the frontend may use a neutral default display.

The default color rule belongs to the frontend presentation layer.

---

# MAP REFRESH STRATEGY

## Trigger

Map refresh is triggered by:

```text
New SearchResult
        ↓
New MapProjectionResult
```

## Workflow

```text
User executes search
        ↓
SearchResult created
        ↓
MapService builds MapProjectionResult
        ↓
Frontend receives MapProjectionResult
        ↓
Leaflet clears existing markers
        ↓
Leaflet renders new markers
```

## Initial Strategy

Use full map refresh.

No incremental diffing is required in Phase 17.4.

No frontend cache is required in Phase 17.4.

---

# SELECTION STRATEGY

Selection remains single-selection only.

## Source

Selection is represented by:

```text
MapViewState.selected_pickup_point_id
```

## User Interaction

```text
User clicks marker
        ↓
Selected pickup point changes
        ↓
Popup opens
```

## Replacement Rule

```text
Existing selection
        ↓
User selects another marker
        ↓
Previous selection replaced
```

## Reset Rule

A new MapProjectionResult resets invalid selections.

If the selected pickup point is not present in the new marker list:

```text
selected_pickup_point_id = None
```

---

# MAP VIEW STRATEGY

MapViewState may expose:

```text
map_center
map_zoom
user_location
selected_pickup_point_id
visible_carriers
```

Leaflet may use these values to initialize or update the map view.

Phase 17.4 does not require persistent user map preferences.

The following are not persisted:

```text
map center
map zoom
selected pickup point
visible carriers
user location
```

---

# FRONTEND BOUNDARY

Frontend Leaflet implementation may later include:

```text
Leaflet map component
marker adapter
popup adapter
carrier logo renderer
carrier filter UI
selection event handler
```

Phase 17.4 defines the integration design only.

Phase 17.4 does not create:

```text
React components
Next.js pages
Leaflet adapter code
CSS styling
frontend routing
```

unless explicitly approved in a later implementation phase.

---

# BACKEND BOUNDARY

The backend already provides:

```text
MapService
MapProjectionResult
MapMarker
MapPopup
MapViewState
```

Phase 17.4 must not require backend persistence.

Phase 17.4 must not require SQLAlchemy models.

Phase 17.4 must not require database migrations.

Phase 17.4 must not require Universal PUDO Engine changes.

---

# OUT OF SCOPE

Phase 17.4 does not include:

```text
marker clustering
routing
turn-by-turn navigation
geocoding
reverse geocoding
heat maps
analytics persistence
user tracking
search persistence
map preference persistence
frontend implementation
React component implementation
Next.js route implementation
Leaflet adapter implementation
OpenStreetMap tile configuration
```

---

# VALIDATED BOUNDARIES

Phase 17.4 preserves the following validated boundaries:

```text
SearchResult remains the business contract
MapProjectionResult remains the presentation contract
Leaflet consumes MapProjectionResult
Map Experience remains presentation-only
No MapSearchResult
No MapPickupPoint
No persistence
No SQLAlchemy
No Alembic migration
No Engine modification
```

---

# SUCCESS CRITERIA

Phase 17.4 Planning Freeze is complete when:

```text
Leaflet architecture is defined
Marker lifecycle is defined
Popup lifecycle is defined
Carrier logo strategy is defined
Carrier color strategy is defined
Map refresh strategy is defined
Selection strategy is defined
Frontend boundary is defined
Backend boundary is preserved
Out-of-scope rules are documented
Phase 17.5 is identified
```

---

# NEXT PHASE

## Phase 17.5 - Leaflet Component Foundation

Expected focus:

```text
Create the first frontend-facing Leaflet integration artifacts.
Consume MapProjectionResult.
Render markers.
Render popups.
Preserve SearchResult boundary.
Preserve MapService boundary.
Avoid persistence.
Avoid Engine modifications.
```

Phase 17.5 must not start until Phase 17.4 is validated, documented, committed and pushed.

---

# RELATED DOCUMENTS

- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md
- docs/project-memory.md
- docs/project-status.md
- docs/map-experience-design.md
- docs/map-models-foundation.md
- backend/src/universal_pudo_saas/map_service/models.py
- backend/src/universal_pudo_saas/map_service/service.py

---

# CHANGE HISTORY

2026-07-30

Initial Leaflet Integration Design created.

Defined:

- Leaflet architectural position
- MapProjectionResult consumption rule
- Marker lifecycle
- Popup lifecycle
- Carrier logo strategy
- Carrier color strategy
- Map refresh strategy
- Selection strategy
- Frontend boundary
- Backend boundary
- Out-of-scope implementation rules
- Phase 17.5 as next phase
