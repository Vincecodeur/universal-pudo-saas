# Universal PUDO SaaS - User Personas And User Journeys

Version: 1.0.0  
Status: Phase 18.2 User Personas And User Journeys  
Last Updated: 2026-08-03

## PURPOSE

This document defines the user personas and user journeys for the Universal PUDO SaaS Frontend MVP.

The objective of Phase 18.2 is to identify:

- technical roles
- real business personas
- primary user journeys
- secondary user journeys
- role-to-persona mapping
- UX implications
- unresolved product decisions for later frontend phases

This document does not define:

- final information architecture
- final screen structure
- final UI design
- final design system
- final frontend architecture
- final data fetching strategy
- final address search implementation
- final security UX implementation

No frontend code is introduced in this phase.  
No backend modification is introduced in this phase.  
No database change is introduced in this phase.  
No Universal PUDO Engine modification is introduced in this phase.

## PHASE CONTEXT

Phase 18 Frontend MVP is the first user-facing phase of Universal PUDO SaaS.

The Frontend MVP exists to allow an authenticated user to:

- search pickup points
- visualize pickup point results
- compare pickup point results
- inspect pickup point details
- select a pickup point

Official MVP definition:

"Allow an authenticated user to search, visualize and select a pickup point."

The product remains:

- search driven
- map enhanced
- focused on PUDO information access
- focused on pickup point search and selection

The product is not:

- a dashboard
- an administration portal
- a reporting tool
- a shipment creation tool
- a label generation tool
- a carrier workflow execution tool

## RELATIONSHIP WITH PHASE 18.1

Phase 18.1 defined the Frontend MVP product vision.

Phase 18.2 translates that product vision into:

- user personas
- role mapping
- user journeys
- UX implications
- future decision points

Phase 18.2 must remain consistent with the Phase 18.1 vision:

- Homepage after login is Search
- Search is the product entry point
- Map supports the search result experience
- Card-based results are preferred
- Pickup point detail is displayed in a side drawer
- Selection is the final MVP action
- Dashboard is out of scope
- Export Platform is out of scope

## TECHNICAL ROLES

Universal PUDO SaaS currently distinguishes three technical roles:

- Viewer
- Owner
- SaaS Administrator

These roles define permissions and access scope.

They are not the same thing as business personas.

## BUSINESS PERSONAS

Phase 18.2 distinguishes business personas from technical roles.

Validated business personas:

- Operations User
- Transport Configuration Manager
- Platform Administrator

Personas describe:

- user context
- business goals
- operational pain points
- success criteria
- expected product behavior

Roles describe:

- access level
- permissions
- platform scope
- organisation scope

## ROLE TO PERSONA MAPPING

| Technical Role     | Business Persona                | Primary MVP Relevance |
| ------------------ | ------------------------------- | --------------------- |
| Viewer             | Operations User                 | Primary MVP user      |
| Owner              | Transport Configuration Manager | Secondary MVP user    |
| SaaS Administrator | Platform Administrator          | Limited MVP user      |

## VIEWER ROLE

### Scope

The Viewer is an organisation-scoped user.

The Viewer can use the search experience.

### MVP Responsibilities

The Viewer can:

- access the Search page
- search pickup points
- view search results
- view results on a map
- inspect pickup point details
- select a pickup point

### MVP Limitations

The Viewer does not:

- configure carrier accounts
- configure carrier credentials
- manage users
- manage organisation settings
- administer the platform
- create shipments
- create labels
- reserve pickup points
- trigger carrier workflows

### UX Priority

Viewer workflows must be optimized first.

The Viewer should be able to complete the main journey without technical knowledge.

## OWNER ROLE

### Scope

The Owner is an organisation-scoped administrator.

The Owner manages organisation-level configuration.

### MVP Responsibilities

The Owner can:

- connect carrier accounts
- configure carrier credentials
- access pickup point search features
- use the same search workflow as a Viewer

### MVP Limitations

The Owner does not own platform-level administration.

The Owner does not control Universal PUDO Engine carrier definitions.

The Owner does not manage SaaS-wide carrier publication.

### UX Priority

The Owner needs two distinct experiences:

- operational search experience
- carrier account configuration experience

For the Frontend MVP, the search experience remains the priority.

Carrier account configuration is required only to support the empty state and search availability.

## SAAS ADMINISTRATOR ROLE

### Scope

The SaaS Administrator is platform-scoped.

The SaaS Administrator is not limited to a single organisation.

### MVP Responsibilities

The SaaS Administrator may need future access to:

- platform administration
- organisation management
- support workflows
- carrier availability controls
- system-level configuration

### MVP Limitations

The Administration Portal is not part of the Frontend MVP.

SaaS Administrator workflows are not the main focus of Phase 18.

### UX Priority

SaaS Administrator journeys should be acknowledged but not deeply implemented in the Frontend MVP.

Administration-specific workflows belong to Phase 19 Administration Portal.

## PERSONA 1 - OPERATIONS USER

### Description

The Operations User is the main product user for the Frontend MVP.

This persona represents users who need to find a pickup point quickly and reliably.

Possible real-world profiles:

- logistics operator
- warehouse operator
- customer service agent
- e-commerce operations user
- transport operations user

### Technical Role

Usually mapped to:

- Viewer

May also be mapped to:

- Owner

when an organisation administrator also performs operational searches.

### Main Goal

Find the most relevant pickup point for a given address.

### Typical Context

The Operations User needs to:

- enter an address
- launch a pickup point search
- compare available pickup points
- understand distance and availability
- inspect operational attributes
- select one pickup point

The search is independent from an order.

No OMS integration is required.  
No WMS integration is required.  
No shipment context is required.

### Needs

The Operations User needs:

- a simple search form
- clear results
- visible map context
- clear pickup point status
- readable carrier information
- distance visibility
- operational attributes
- quick access to pickup point details
- copyable address
- copyable relay ID

### Pain Points

The Operations User may struggle when:

- no carrier is connected
- too many pickup points are displayed without prioritization
- pickup point status is unclear
- distance is unclear
- carrier compatibility is unclear
- operational attributes are hidden
- the difference between search, visualization and selection is unclear

### Success Criteria

The Operations User succeeds when:

- an address can be searched easily
- results are understandable
- the map helps compare locations
- pickup point details are easy to inspect
- one pickup point can be selected
- the user understands that selection does not trigger a carrier workflow

### Key UX Principle

The Operations User should not need to understand carrier APIs, backend contracts or technical error messages.

## PERSONA 2 - TRANSPORT CONFIGURATION MANAGER

### Description

The Transport Configuration Manager manages the organisation's carrier access.

This persona represents users responsible for enabling the organisation to use carrier-based PUDO search.

Possible real-world profiles:

- transport manager
- logistics manager
- e-commerce operations manager
- OMS administrator
- WMS administrator
- organisation administrator

### Technical Role

Usually mapped to:

- Owner

### Main Goal

Connect and manage carrier accounts so that organisation users can search pickup points.

### Typical Context

The Transport Configuration Manager needs to:

- access carrier account configuration
- connect carrier accounts
- configure carrier credentials
- validate that carrier accounts are active
- ensure users can search pickup points
- use the search experience when needed

### Needs

The Transport Configuration Manager needs:

- clear empty state guidance
- clear link from Search to Carrier Accounts when no carrier is connected
- understandable carrier account status
- simple access to carrier configuration
- separation between operational search and configuration workflows

### Pain Points

The Transport Configuration Manager may struggle when:

- the product shows an empty map without explanation
- carrier activation status is unclear
- users cannot search and the reason is unclear
- configuration and search are mixed in the same workflow
- technical carrier credential errors are displayed without business explanation

### Success Criteria

The Transport Configuration Manager succeeds when:

- at least one carrier account is connected
- organisation users can search pickup points
- unavailable search states are clearly explained
- carrier account configuration is discoverable from the Search experience

### Key UX Principle

The Transport Configuration Manager must understand how carrier configuration enables search availability.

## PERSONA 3 - PLATFORM ADMINISTRATOR

### Description

The Platform Administrator manages the SaaS platform from a platform-level perspective.

This persona represents future platform operations and support users.

Possible real-world profiles:

- SaaS support user
- platform administrator
- internal operations administrator

### Technical Role

Mapped to:

- SaaS Administrator

### Main Goal

Maintain platform-level operations and support organisations.

### MVP Relevance

The Platform Administrator is not the primary user of the Frontend MVP.

The Administration Portal is planned for a later phase.

### Needs

The Platform Administrator may later need:

- organisation management
- platform-level carrier availability
- support visibility
- platform monitoring
- operational troubleshooting

### Pain Points

Information not found in the documents provided.

### Success Criteria

For the Frontend MVP, success is limited to acknowledging that this persona exists and that deeper workflows belong to future administration phases.

### Key UX Principle

Platform administration should not pollute the MVP search experience.

## PRIMARY USER JOURNEY 1 - SEARCH AND SELECT PICKUP POINT

### Persona

Operations User

### Technical Role

Viewer

### Trigger

The user wants to find a pickup point near an address.

### Preconditions

The user is authenticated.

At least one carrier account is available for the organisation.

### Journey

Login
↓
Search page
↓
Enter address
↓
Optional carrier selection
↓
Launch search
↓
View result cards
↓
View map
↓
Compare pickup points
↓
Open pickup point detail drawer
↓
Select pickup point

### Search Form Rules

Address:

- required

Carrier:

- optional

Default carrier value:

- All available carriers

### Final Action

The final MVP action is:

Select Pickup Point

### Selection Meaning

Selection means:

The user has selected one pickup point in the current user interface context.

Selection does not mean:

- reservation
- shipment creation
- parcel creation
- label creation
- carrier workflow execution
- business confirmation
- persistence

### Selection Lifecycle

Current SearchResult
↓
User selects pickup point
↓
Selection remains active
↓
User launches a new search
↓
New SearchResult is generated
↓
Selection is reset

### UX Implications

The UI must avoid wording that implies a business operation.

Recommended button label:

- Select Pickup Point

Avoid:

- Confirm
- Use This Pickup Point
- Book Pickup Point
- Reserve Pickup Point
- Create Shipment
- Generate Label

## PRIMARY USER JOURNEY 2 - SEARCH WITH ALL AVAILABLE CARRIERS

### Persona

Operations User

### Technical Role

Viewer

### Trigger

The user wants to search across all available organisation carriers.

### Preconditions

The user is authenticated.

At least one carrier account is available for the organisation.

### Journey

Login
↓
Search page
↓
Enter address
↓
Carrier field defaults to "All available carriers"
↓
Launch search
↓
System searches across available carriers
↓
Cards display pickup points from multiple carriers
↓
Map displays pickup points
↓
User compares carriers, distance and attributes
↓
User selects one pickup point

### UX Implications

The default carrier selection must reinforce the product value:

- multi-carrier search
- carrier comparison
- operational flexibility

Carrier filtering should be available but should not be mandatory.

## PRIMARY USER JOURNEY 3 - SEARCH WITH ONE CARRIER FILTER

### Persona

Operations User

### Technical Role

Viewer

### Trigger

The user wants to search pickup points for a specific carrier.

### Preconditions

The user is authenticated.

The selected carrier is available to the organisation.

### Journey

Login
↓
Search page
↓
Enter address
↓
Select one carrier
↓
Launch search
↓
View carrier-specific results
↓
Compare pickup points
↓
Open detail drawer
↓
Select pickup point

### UX Implications

Carrier selection is a filter.

Carrier selection must not imply that the platform only supports single-carrier search.

The default remains:

- All available carriers

## PRIMARY USER JOURNEY 4 - EMPTY STATE WITH NO CONNECTED CARRIER

### Persona

Transport Configuration Manager

### Technical Role

Owner

### Trigger

The user enters the Search page but no carrier account is connected.

### Preconditions

The user is authenticated.

The organisation has no connected carrier account.

### Journey

Login
↓
Search page
↓
Empty map displayed
↓
Explanatory message displayed
↓
Action button displayed
↓
User clicks "Connect a Carrier"
↓
User is redirected to Carrier Accounts

### Expected Message

No transport carrier is currently connected.  
Connect at least one carrier account before searching for pickup points.

### Expected Action

Connect a Carrier

### UX Implications

The empty state must not look like:

- an error
- a blank page
- a system failure
- a broken map

The empty state must explain:

- why no pickup points are visible
- what the user can do next

## PRIMARY USER JOURNEY 5 - PICKUP POINT DETAIL REVIEW

### Persona

Operations User

### Technical Role

Viewer

### Trigger

The user wants more information about one pickup point.

### Preconditions

Search results are available.

The user selects a result card or map marker.

### Journey

Search results displayed
↓
User selects one result or marker
↓
Side drawer opens
↓
User reviews pickup point details
↓
User copies address or relay ID if needed
↓
User selects pickup point

### Detail Drawer Information

The detail drawer should display:

- pickup point name
- relay ID
- full address
- distance
- phone number
- opening hours
- status
- carrier name
- carrier logo
- pickup point type
- carrier-specific attributes

### UX Implications

The detail view should not open a new page.

The drawer keeps the user in the search context.

## SECONDARY USER JOURNEY 1 - OWNER USES SEARCH

### Persona

Transport Configuration Manager

### Technical Role

Owner

### Trigger

The Owner wants to validate that connected carriers produce searchable pickup points.

### Preconditions

The user is authenticated.

The user has Owner role.

At least one carrier account is connected.

### Journey

Login
↓
Search page
↓
Enter address
↓
Search all available carriers
↓
View results
↓
Compare carrier results
↓
Select pickup point if needed

### UX Implications

The Owner should not have a different search experience from the Viewer.

The same operational search journey should be available to both.

## SECONDARY USER JOURNEY 2 - SESSION EXPIRED

### Persona

Operations User

### Technical Role

Viewer

### Trigger

The user session expires while using the search experience.

### Preconditions

The user was authenticated.

The session is no longer valid.

### Journey

User attempts action
↓
Session issue detected
↓
Business-friendly message displayed
↓
User is redirected to login
↓
User authenticates again
↓
User returns to the product

### UX Implications

Detailed session recovery behavior is not frozen in Phase 18.2.

This topic must be handled in:

- Phase 18.8 Security UX Strategy
- Phase 18.10 Data Fetching & State Strategy
- Phase 18.12 Error Handling Strategy

## SECONDARY USER JOURNEY 3 - NO PICKUP POINT FOUND

### Persona

Operations User

### Technical Role

Viewer

### Trigger

The user searches an address but no pickup point is found.

### Preconditions

The user is authenticated.

At least one carrier is available.

A search is executed.

### Journey

Search page
↓
Enter address
↓
Launch search
↓
No pickup point found
↓
Business message displayed
↓
User adjusts search criteria

### Recommended Message Direction

No pickup points found.

### UX Implications

The message should be business-oriented.

Avoid exposing technical errors such as:

- HTTP 404
- Internal Server Error
- backend stack trace
- provider payload error

## UNRESOLVED DECISION - ADDRESS SEARCH NATURE

### Decision ID

UX-D001

### Topic

Nature of address search.

### Current Known Flow

Address
↓
Search
↓
Pickup points

### Unresolved Question

What exactly is "Address" in the Frontend MVP?

Possible options:

- free text address
- address with autocomplete
- address with geocoding
- geographic coordinates
- combination of the above

### Current Phase 18.2 Position

This decision is not frozen during Phase 18.2.

Phase 18.2 must identify the topic only.

### Reason

The address search decision will influence:

- user journeys
- information architecture
- search UX
- search results UX
- frontend architecture
- data fetching strategy
- possible external service strategy
- error states
- validation rules

### Future Phases Concerned

This decision must be handled during:

- Phase 18.3 Information Architecture
- Phase 18.4 UX Strategy
- Phase 18.9 Frontend Architecture Design
- Phase 18.10 Data Fetching And State Strategy

### Constraint

No implementation decision is made in Phase 18.2.

## PERMISSIONS VISIBILITY MATRIX

| Capability                 | Viewer |  Owner | SaaS Administrator | MVP Priority    |
| -------------------------- | -----: | -----: | -----------------: | --------------- |
| Login                      |    Yes |    Yes |                Yes | High            |
| Access Search page         |    Yes |    Yes |           Possible | High            |
| Search pickup points       |    Yes |    Yes |           Possible | High            |
| View result cards          |    Yes |    Yes |           Possible | High            |
| View map                   |    Yes |    Yes |           Possible | High            |
| View pickup point details  |    Yes |    Yes |           Possible | High            |
| Select pickup point        |    Yes |    Yes |           Possible | High            |
| Connect carrier account    |     No |    Yes |             Future | Medium          |
| Manage carrier credentials |     No |    Yes |             Future | Medium          |
| Manage users               |     No | Future |             Future | Out of Phase 18 |
| Platform administration    |     No |     No |             Future | Out of Phase 18 |
| Dashboard                  |     No |     No |                 No | Out of MVP      |
| Export Platform            |     No |     No |                 No | Out of MVP      |

## UX IMPLICATIONS

### Search First

The user journey starts with search.

The Search page is the homepage after login.

### Map Enhanced

The map helps users:

- understand pickup point locations
- compare options visually
- understand distance
- support selection

The map does not replace search.

### Cards First For Comparison

Search results should be displayed as cards.

Cards should help users compare pickup points quickly.

### Drawer For Details

Pickup point details should open in a side drawer.

The user should remain in the search context.

### Selection Is UI State

Selection remains active within the current SearchResult.

Selection is reset only when a new SearchResult is generated.

### No Business Execution

The MVP must not imply that selecting a pickup point creates a business transaction.

The product must not suggest:

- reservation
- shipment creation
- carrier booking
- label generation
- order update
- carrier confirmation

### Empty States Matter

The empty state for no connected carrier is a primary UX flow.

It must explain the issue and guide the user to Carrier Accounts.

## MVP SCOPE VALIDATION

The Phase 18.2 journeys confirm that the Frontend MVP scope remains:

Included:

- authentication access
- search page
- address-based search
- optional carrier filtering
- all available carriers default
- result cards
- map visualization
- pickup point detail drawer
- pickup point selection
- no carrier connected empty state
- no pickup point found state

Excluded:

- dashboard
- analytics
- search history
- favorites
- public website
- blog
- CMS
- shipment creation
- label generation
- tracking
- route planning
- pickup point reservation
- carrier workflow execution
- export platform
- persistent notifications

## OUT OF SCOPE JOURNEYS

The following journeys are explicitly out of scope for Phase 18.2 and the Frontend MVP:

- Create shipment
- Generate shipping label
- Reserve pickup point
- Confirm carrier handover
- Update an OMS order
- Update a WMS shipment
- Track a parcel
- Export search results
- Build dashboard
- View analytics
- Manage platform billing
- Manage SaaS quotas
- Manage platform-wide carrier publication
- Configure complete administration portal
- Create public API consumers

## SUCCESS CRITERIA

Phase 18.2 is successful when:

- technical roles are identified
- business personas are identified
- role-to-persona mapping is documented
- primary user journeys are documented
- secondary user journeys are documented
- selection meaning is clarified
- search independence from orders is clarified
- carrier filter optionality is clarified
- empty state journey is documented
- unresolved address search decision is documented for later phases
- out-of-scope journeys are documented
- Phase 18.3 can start without redefining personas

## PHASE 18.2 EXIT CRITERIA

Phase 18.2 is complete when:

- Viewer role is mapped to Operations User
- Owner role is mapped to Transport Configuration Manager
- SaaS Administrator role is mapped to Platform Administrator
- Operations User journey is documented
- Transport Configuration Manager journey is documented
- Platform Administrator MVP relevance is documented
- search flow remains independent from orders
- address is marked as required
- carrier is marked as optional
- default carrier value is documented as "All available carriers"
- pickup point selection is documented as the final MVP action
- pickup point selection is documented as non-persistent
- no business workflow is attached to selection
- Q7 address search nature is documented as unresolved
- future phases impacted by Q7 are identified

## NEXT PHASE

Phase 18.3  
Information Architecture

Expected focus:

- define page inventory
- define navigation hierarchy
- define route structure
- define Search page composition
- define Carrier Accounts access relationship
- define map and results layout relationship
- define drawer placement
- preserve personas and journeys defined in Phase 18.2

Phase 18.3 must not start until Phase 18.2 is validated, documented, committed and pushed.

## RELATED DOCUMENTS

- docs/frontend-mvp-vision.md
- docs/product-vision.md
- docs/architecture.md
- docs/project-memory.md
- docs/project-status.md
- docs/roadmap.md
- docs/map-experience-design.md
- docs/map-experience-validation.md
- docs/map-experience-closure.md
- docs/adr/ADR-0010 - Frontend Prioritization Before Export Platform.md

## CHANGE HISTORY

2026-08-03  
Initial User Personas And User Journeys document created.  
Defined:

- technical roles
- business personas
- role-to-persona mapping
- Operations User persona
- Transport Configuration Manager persona
- Platform Administrator persona
- search and selection journey
- all available carriers default behavior
- optional carrier filtering
- no connected carrier empty state
- pickup point detail drawer journey
- selection as final non-persistent MVP action
- address search nature as unresolved future decision
- Phase 18.3 as next phase
