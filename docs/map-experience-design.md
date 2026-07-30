# Universal PUDO SaaS - Map Experience Design

Version: 1.0.0
Status: Phase 17.1 Design Freeze
Last Updated: 2026-07-30

## PURPOSE

This document defines the Map Experience domain for Universal PUDO SaaS.

The objective of Map Experience is to provide a visual representation of pickup point search results while preserving all previously established SaaS and Engine ownership boundaries.

Map Experience must:

- consume SearchResult
- display pickup points on a map
- allow pickup point selection
- provide a consistent user search experience
- remain independent from carrier implementations
- preserve Universal PUDO Engine ownership
- prepare future analytics capabilities

Map Experience is a presentation concern.

Map Experience is not a carrier execution concern.

## DESIGN OBJECTIVES

The Map Experience exists to:

- visualize SearchResult data
- simplify pickup point discovery
- support pickup point comparison
- improve result navigation
- prepare future analytics
- prepare future frontend experiences

The Map Experience must not introduce new business ownership.

SearchResult remains the authoritative search contract.

## OWNERSHIP MODEL

### Universal PUDO SaaS Owns

Universal PUDO SaaS owns:

- Map Experience
- pickup point visualization
- pickup point selection
- carrier visual branding
- future carrier display preferences
- future map analytics
- future map user experience settings

### Universal PUDO Engine Owns

Universal PUDO Engine owns:

- carrier integrations
- provider execution
- carrier search execution
- pickup point normalization
- pickup point retrieval
- carrier definitions
- carrier metadata
- public carrier availability

The Map Experience must never duplicate Engine responsibilities.

## RELATIONSHIP WITH SEARCH PLATFORM

Map Experience consumes Search Platform outputs.

Logical architecture:

```text
SearchPlatformService
        |
        v
SearchResult
        |
        v
Map Experience
```

Map Experience must never directly consume:

```text
OrganisationSearchService
MultiCarrierSearchService
EngineSearchService
Universal PUDO Engine
```

SearchPlatformService remains the official SaaS search boundary.

## SEARCH RESULT PRINCIPLE

SearchResult remains the unique business contract for search results.

The following models are explicitly forbidden during Phase 17:

```text
MapSearchResult
MapPickupPoint
MapCarrier
MapSearchResponse
```

Map Experience consumes:

```text
SearchResult
    -> PickupPoint
```

directly.

No duplicate search contract is introduced.

No duplicate pickup point contract is introduced.

No map-specific business model is introduced.

## CURRENT SEARCH CONTRACT

The current SearchResult contains:

```text
pickup_points
total_results
executed_carriers
failed_carriers
metadata
```

The current PickupPoint contains:

```text
pickup_id
carrier_id
name
pickup_type
address
geolocation
active
opening_hours
phone_number
email
services
```

Map Experience may use only the data exposed by SearchResult and PickupPoint.

If information is not available in the existing contract, Phase 17.1 must not invent it.

## PICKUP POINT VISUALIZATION

Each PickupPoint may be represented visually on a map.

Required map marker data:

```text
pickup_id
carrier_id
name
pickup_type
geolocation.latitude
geolocation.longitude
```

Optional display data:

```text
address
opening_hours
carrier branding
```

The map layer remains a presentation layer.

The map layer does not modify PickupPoint data.

The map layer does not enrich PickupPoint data.

The map layer does not persist PickupPoint data.

## PICKUP POINT SELECTION MODEL

### Purpose

The selection model allows the user to select one pickup point from displayed search results.

### Selection Strategy

Current strategy:

```text
Single Selection
```

Only one pickup point may be selected at a time.

### Selection Lifecycle

Selection is:

```text
not persisted
not exported
not shared
not stored
not synchronized with an external system
```

Selection exists only within the current user interface state.

### Search Result Refresh Rule

When a new SearchResult is loaded:

```text
Current selection is reset.
```

Reason:

A selected pickup point belongs to the current SearchResult context.

A new SearchResult represents a new search context.

The previous selection must not survive across search executions.

## PICKUP POINT POPUP DESIGN

### Purpose

The pickup point popup provides quick access to the most relevant pickup point information.

### Visible Information

The popup may display:

```text
carrier logo
carrier name if available
pickup point name
address
opening hours
pickup type
distance if already present in the existing SearchResult or PickupPoint contract
more information link
```

### Hidden Information

The popup must not display during Phase 17:

```text
phone number
email
services
```

These fields may exist in the PickupPoint model, but they are not part of the Phase 17 popup display scope.

### Distance Rule

Distance may be displayed only if already provided by the existing SearchResult or PickupPoint contract.

Phase 17 must not introduce:

```text
distance calculation
ranking by distance
distance enrichment
geospatial business logic
```

## MORE INFORMATION LINK

The popup may expose a "More information" link.

The purpose of this link is to open a more complete pickup point detail view in a future user interface.

Phase 17.1 defines the concept only.

Phase 17.1 does not implement:

```text
frontend navigation
pickup point detail page
modal component
routing
API endpoint
```

## CARRIER BRANDING STRATEGY

Carrier branding belongs to Universal PUDO SaaS.

Carrier branding includes:

```text
carrier logo
carrier icon
carrier display color
future carrier display rules
```

Carrier branding is not owned by Universal PUDO Engine.

Universal PUDO Engine remains the owner of:

```text
carrier_code
carrier_name
carrier_definition
carrier_capabilities
carrier lifecycle
carrier publication status
```

This preserves the existing Engine and SaaS ownership boundaries.

## ADMINISTRATION OWNERSHIP

Carrier branding configuration belongs to the future Administration module.

Only the SaaS administration scope may manage:

```text
carrier logos
carrier colors
carrier icons
map branding options
future carrier display rules
```

Organisation users consume branding configuration.

Organisation users do not define platform-level carrier branding.

Phase 17.1 does not implement carrier branding administration.

## CARRIER AVAILABILITY STRATEGY

Carrier availability is determined by:

```text
published Engine carrier
+
active Organisation CarrierAccount
```

Only available carriers may appear in the Map Experience.

A carrier that is not published by the Engine must not be displayed.

A carrier that has no active CarrierAccount for the organisation must not be displayed.

A carrier that is not available to the organisation must not be selectable in map display settings.

## CARRIER VISIBILITY STRATEGY

Carrier availability and carrier visibility are different concepts.

### Carrier Availability

Carrier availability defines which carriers the organisation can use.

It is derived from:

```text
Engine publication rules
Organisation CarrierAccount activation
```

### Carrier Visibility

Carrier visibility defines which available carriers the user chooses to display on the map.

Future examples:

```text
show Colissimo
show Mondial Relay
hide Chronopost
show InPost
```

A user may configure visibility only for carriers available to the organisation.

The user must never be able to display a carrier that is not connected to the organisation.

## DEFAULT USER EXPERIENCE

The default layout is:

```text
Map With Side Panel
```

The side panel may contain:

```text
pickup point list
selected pickup point summary
carrier filters
future display settings
```

Phase 17.1 defines the layout concept only.

No frontend layout is implemented in Phase 17.1.

## FUTURE LAYOUT MODES

The design prepares support for the following future layout modes:

```text
Map With Side Panel
List And Map
Map Only
```

These are future user experience options.

Phase 17.1 does not implement:

```text
layout switcher
frontend state management
user preference persistence
responsive UI
mobile UI
```

## FRONTEND STRATEGY

No frontend currently exists in the project.

Therefore Phase 17.1 must not introduce:

```text
Next.js application
React component
Leaflet integration
OpenStreetMap integration
CSS styling
frontend routing
frontend state management
```

Frontend implementation remains planned for a later phase.

Map Experience design must remain compatible with the future frontend stack:

```text
Next.js
React
TypeScript
Leaflet
OpenStreetMap
```

## FUTURE ANALYTICS PREPARATION

The selected pickup point represents a future business event.

Future analytics may include:

```text
selection statistics
carrier usage analytics
search behaviour analytics
pickup point popularity
map interaction analytics
dashboard metrics
recommendation signals
```

Phase 17.1 must not implement analytics.

Phase 17.1 must not introduce event persistence.

Phase 17.1 only preserves the possibility of future analytics by keeping the selection concept explicit.

## PLUGIN BOUNDARY

Universal PUDO SaaS remains a standalone SaaS product.

Universal PUDO SaaS is not a Shopify plugin.

Universal PUDO SaaS is not a WooCommerce plugin.

Universal PUDO SaaS is not a Prestashop plugin.

Universal PUDO SaaS is not a Magento plugin.

Future plugins must be developed as separate projects.

The SaaS may later expose capabilities consumed by plugins, but plugin development is not part of the SaaS repository scope.

## OUT OF SCOPE FOR PHASE 17.1

Phase 17.1 must not introduce:

```text
frontend code
React components
Next.js application
Leaflet integration
OpenStreetMap integration
SQLAlchemy models
Alembic migrations
database tables
search persistence
map persistence
selection persistence
analytics persistence
export behaviour
public API behaviour
carrier branding administration
user preference persistence
ranking algorithm
distance calculation
Engine modification
carrier provider logic
```

## ALLOWED ARTIFACTS FOR PHASE 17.1

Phase 17.1 may introduce documentation only.

Allowed artifact:

```text
docs/map-experience-design.md
```

No Python implementation is required during Phase 17.1.

No frontend implementation is required during Phase 17.1.

No database implementation is required during Phase 17.1.

## DESIGN PRINCIPLES

### P001 - SearchResult First

Map Experience consumes SearchResult directly.

### P002 - No Contract Duplication

Map Experience must not introduce MapSearchResult or MapPickupPoint.

### P003 - Presentation Layer Only

Map Experience is a user experience layer, not a business execution layer.

### P004 - Engine Boundary Protection

Map Experience must not access Engine internals or duplicate Engine responsibilities.

### P005 - No Persistence In Phase 17

Map selection and map display state are not persisted during Phase 17.1.

### P006 - Admin-Owned Branding

Carrier branding belongs to SaaS administration, not to Universal PUDO Engine.

### P007 - User-Controlled Visibility

Users may eventually choose which available carriers are visible on the map.

### P008 - Analytics-Ready Without Analytics Implementation

Pickup point selection is documented as a future analytics-relevant event, but no analytics implementation is introduced.

## LOGICAL USER FLOW

Target user flow:

```text
User enters search criteria
        |
        v
SearchPlatformService executes search
        |
        v
SearchResult is returned
        |
        v
Map Experience displays PickupPoints
        |
        v
User opens a pickup point popup
        |
        v
User selects one PickupPoint
        |
        v
Selected PickupPoint becomes the current UI selection
```

The selected PickupPoint is not persisted.

The selected PickupPoint is not exported.

The selected PickupPoint is not sent to a public API during Phase 17.

## PHASE 17.1 EXIT CRITERIA

Phase 17.1 is complete when:

```text
Map Experience scope is defined
SearchResult consumption rule is defined
No duplicate map contracts are confirmed
Pickup point selection model is defined
Popup information scope is defined
Carrier branding ownership is defined
Carrier availability and visibility are separated
Default layout strategy is defined
Future analytics preparation is documented
Out-of-scope boundaries are documented
Documentation is synchronized
```

## NEXT PHASE

### Phase 17.2 - Map Models Foundation

Expected focus:

```text
Define presentation-oriented map structures only if required.
Preserve SearchResult as the unique business contract.
Avoid SQLAlchemy models.
Avoid persistence.
Avoid frontend implementation unless explicitly planned later.
```

Phase 17.2 must not start until Phase 17.1 is validated, documented, committed and pushed.

## RELATED DOCUMENTS

- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md
- docs/project-memory.md
- docs/project-status.md
- docs/search-platform-design.md
- docs/carrier-integration-model.md
- docs/adr/ADR-0007-carrier-catalog-ownership.md
- docs/adr/ADR-0008 - Public Engine Contract.md
- docs/adr/ADR-0009 - Carrier Publication Rules.md

## CHANGE HISTORY

2026-07-30
Initial Map Experience Design created.
Defined:

- SearchResult as unique Map Experience input
- no MapSearchResult rule
- no MapPickupPoint rule
- single pickup point selection
- selection reset on new SearchResult
- popup display scope
- SaaS-owned carrier branding
- admin-owned branding configuration
- carrier availability versus carrier visibility
- standalone SaaS boundary from future plugin projects
- analytics-ready selection concept without analytics implementation
