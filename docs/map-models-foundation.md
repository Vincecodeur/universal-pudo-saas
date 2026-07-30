# Universal PUDO SaaS - Map Models Foundation

Version: 1.0.0

Status: Phase 17.2 Planning Freeze

Last Updated: 2026-07-30

---

# PURPOSE

This document defines the presentation-oriented models used by Map Experience.

The purpose of Phase 17.2 is to define UI-facing map structures while preserving the existing Search Platform contract.

Map Experience remains a presentation layer.

SearchResult remains the unique business contract.

---

# PHASE OBJECTIVES

Phase 17.2 must:

- define map presentation structures
- define marker projection structures
- define popup projection structures
- define user selection structures
- define carrier visibility structures
- preserve SearchResult

Phase 17.2 must not:

- introduce MapSearchResult
- introduce MapPickupPoint
- introduce persistence
- introduce SQLAlchemy models
- introduce database tables
- introduce Alembic migrations
- modify Universal PUDO Engine

---

# ARCHITECTURAL PRINCIPLES

## AP-001

SearchResult remains the unique business contract.

Map Experience consumes SearchResult.

Map Experience does not redefine SearchResult.

---

## AP-002

Map Experience is a presentation layer.

Business logic remains inside Search Platform services.

---

## AP-003

Map state is UI state.

Map state is not persisted.

---

## AP-004

Carrier visibility is a user preference.

Carrier visibility is independent from carrier availability.

---

## AP-005

Pickup point selection is UI state.

Selection is not persisted.

---

# MAP STATE MODEL

Purpose:

Represents current user interaction with the map.

Structure:

map_center

map_zoom

user_location

selected_pickup_point_id

visible_carriers

Characteristics:

- presentation only
- non persistent
- resettable
- frontend oriented

---

# MARKER PROJECTION MODEL

Purpose:

Represents how SearchResult pickup points are visualized on the map.

Projection Source:

SearchResult

Displayed Information:

pickup_point_id

latitude

longitude

carrier_code

carrier_display_name

carrier_logo_url

carrier_color

Rules:

- derived from SearchResult
- no independent lifecycle
- no persistence

---

# POPUP PROJECTION MODEL

Purpose:

Represents information displayed when a marker is selected.

Displayed Information:

pickup_point_name

carrier

address

distance

opening_hours

details_link

Rules:

- derived from SearchResult
- presentation only
- no persistence

---

# CARRIER VISIBILITY MODEL

Purpose:

Allows users to control which available carriers are displayed.

Definitions:

Available Carrier

Carrier available to the organisation through:

- Engine publication
- active CarrierAccount

Visible Carrier

Carrier currently displayed on the map.

Decision:

Available Carrier

≠

Visible Carrier

A carrier may be available but hidden from map rendering.

---

# PICKUP POINT SELECTION MODEL

Purpose:

Represents current map selection.

Rules:

Only one PickupPoint may be selected at a time.

New selection replaces previous selection.

Selection lifecycle:

No selection
↓
Marker click
↓
PickupPoint selected
↓
New marker click
↓
Previous selection replaced

---

# SEARCH RESULT RESET STRATEGY

Decision:

A new SearchResult invalidates previous map selections.

Workflow:

SearchResult A
↓
PickupPoint Selected
↓
SearchResult B
↓
Selection Reset

Reason:

Prevent invalid references to pickup points that no longer exist in the current result set.

---

# ANALYTICS BOUNDARY

Purpose:

Prepare future analytics without introducing persistence.

Potential Future Event:

PickupPointSelected

Phase 17.2 Rules:

- no event storage
- no analytics implementation
- no database impact
- no persistence

Future phases may reuse map interactions for analytics purposes.

---

# OUT OF SCOPE

Phase 17.2 does not include:

- Leaflet implementation
- OpenStreetMap implementation
- marker rendering
- clustering
- geolocation services
- API endpoints
- SQLAlchemy models
- exports
- analytics persistence
- dashboard integration

---

# VALIDATED DECISIONS

Inherited from Phase 17.1:

✅ SearchResult remains the unique business contract

✅ No MapSearchResult

✅ No MapPickupPoint

✅ Single pickup point selection

✅ Selection reset on new SearchResult

✅ Carrier visibility separated from carrier availability

✅ Carrier branding owned by SaaS Administration

✅ Analytics-ready architecture

✅ No persistence

✅ No Engine modification

---

# SUCCESS CRITERIA

Phase 17.2 is completed when:

✅ Map presentation structures are defined

✅ SearchResult remains unchanged

✅ No new business contract is introduced

✅ No persistence is introduced

✅ No SQLAlchemy model is introduced

✅ No migration is introduced

✅ No Engine modification is introduced

✅ Documentation is synchronized

✅ Phase 17.3 is defined

---

# NEXT PHASE

Phase 17.3

Map Service Foundation

Objectives:

- transform SearchResult into map-ready projections
- prepare frontend consumption
- preserve SearchResult
- avoid persistence
- avoid Engine modifications
