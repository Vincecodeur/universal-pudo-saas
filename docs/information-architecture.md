# Information Architecture

# Universal PUDO SaaS

# Phase 18.3 Information Architecture

Version: 1.0.0
Status: Approved
Last Updated: 2026-08-04

---

## PURPOSE

This document defines the Information Architecture of the Frontend MVP.

Goals:

- define page inventory
- define navigation structure
- define route structure
- define page responsibilities
- define Search / Results / Map relationships
- define Pickup Point Detail architecture
- define information hierarchy
- freeze architecture decisions before UX Strategy

This document does not define:

- visual design
- component styling
- design system
- accessibility implementation
- frontend implementation
- responsive implementation
- state management implementation

These subjects belong to later Phase 18 sub-phases.

---

# INFORMATION ARCHITECTURE PRINCIPLES

## IA-001

Search is the primary purpose of the product.

The primary reason users access the platform is to locate pickup points.

Therefore Search is the primary application entry point.

---

## IA-002

Search remains independent from:

- OMS workflows
- WMS workflows
- shipment workflows
- label workflows
- carrier execution workflows

Search only returns pickup point information.

---

## IA-003

Map is a visual support layer.

Results remain the primary operational interface.

Map reflects Results.

Results do not reflect Map.

Information hierarchy:

Results
↓
Map

---

## IA-004

Pickup Point selection is non-persistent.

The MVP does not:

- reserve pickup points
- create shipments
- create labels
- create orders
- create workflows

Selection is a user interface action only.

---

## IA-005

Carrier Accounts are organization assets.

An organization may own:

- multiple carriers
- multiple accounts per carrier

Carrier Account is the primary entity.

Carrier is not the primary entity.

Example:

Colissimo FR
Colissimo Export

DPD UK
DPD Retail
DPD B2B

---

# APPLICATION NAVIGATION

## NAVIGATION MODEL

The application uses a persistent left sidebar.

Layout:

Sidebar

- Application Content Area

  ***

## SIDEBAR NAVIGATION

Standard User:

- Search
- Carrier Accounts
- Profile

Platform Administrator:

- Search
- Carrier Accounts
- Profile
- Administration

---

## NAVIGATION RULES

The sidebar remains visible throughout the application.

Users should never lose navigation context.

The MVP does not use a top-navigation-first approach.

---

# ROUTE MAP

## AUTHENTICATION

/login

Purpose:

User authentication.

---

## SEARCH

/search

Purpose:

Primary MVP page.

Responsibilities:

- search form
- pickup point results
- interactive map
- pickup point details

---

## CARRIER ACCOUNTS

/carrier-accounts

Purpose:

Carrier account management.

Responsibilities:

- view accounts
- add account
- edit account
- activate/deactivate account
- validate account status

---

## PROFILE

/profile

Purpose:

Personal user settings.

Responsibilities:

- user information
- account preferences
- future security settings

---

## ADMINISTRATION

/administration

Administrator only.

Purpose:

Platform administration.

Responsibilities:

- carrier publication
- organization administration
- platform settings

Future Phase 19 expansion expected.

---

# APPLICATION ENTRY POINT

## LOGIN FLOW

User
↓
Login
↓
/search

The homepage after login is:

/search

There is no Dashboard page in the MVP.

Reason:

Search is the primary MVP use case.

---

# PAGE INVENTORY

## PAGE 1

Search

Status:

Core MVP Page

---

## PAGE 2

Carrier Accounts

Status:

Core MVP Page

---

## PAGE 3

Profile

Status:

Core MVP Page

---

## PAGE 4

Administration

Status:

Future Administrator Page

---

# SEARCH PAGE ARCHITECTURE

## HIGH LEVEL STRUCTURE

Header

↓

Search Filters

↓

Results + Map

↓

Pickup Point Detail Drawer

---

## PAGE LAYOUT

+-------------------------------------------------------+
| Search Filters |
+-------------------------------------------------------+

+----------------------+--------------------------------+
| Results | Map |
| | |
| Pickup Point List | Leaflet |
| | |
+----------------------+--------------------------------+

+-------------------------------------------------------+
| Pickup Point Drawer (right side) |
+-------------------------------------------------------+

---

# SEARCH FILTER AREA

## RESPONSIBILITIES

Collect search parameters.

Input fields:

- Address
- Carrier Filter

Actions:

- Search

---

## REQUIRED FIELDS

Address

Required.

---

## OPTIONAL FIELDS

Carrier

Optional.

Default value:

All Available Carriers

---

# RESULTS PANEL

## ROLE

Primary operational area.

Results are the primary interaction surface.

The list is the authoritative view.

---

## RESPONSIBILITIES

Display:

- pickup point name
- carrier name
- address
- distance
- operating information

Actions:

- view details
- select pickup point
- synchronize map position

---

# MAP PANEL

## ROLE

Visual exploration support.

The map is not the primary operational view.

The map reflects Results.

---

## RESPONSIBILITIES

Display:

- markers
- clustering
- carrier branding
- selected pickup point

Consume:

MapProjectionResult

without modifying business contracts.

---

## FULL SCREEN MODE

Architecture support required.

Future implementation allowed.

The MVP architecture must allow:

Expand Map

without redesigning navigation.

---

# PICKUP POINT DETAIL DRAWER

## ARCHITECTURE

Right-side drawer.

No modal.

No dedicated page.

---

## OPENING EVENTS

Results click

OR

Map marker click

↓

Open Drawer

---

## CONTENT

Pickup Point:

- name
- address
- carrier
- geolocation information
- opening hours
- services

Actions:

- Select Pickup Point
- Close Drawer

---

## CLOSING EVENTS

User closes drawer.

OR

New Search execution.

---

# SEARCH / RESULTS / MAP RELATIONSHIP

## DATA FLOW

Search
↓
SearchResult
↓
Results Panel
↓
Map Projection
↓
Map

---

## AUTHORITY MODEL

SearchResult

↓

Results

↓

Map

Results remain authoritative.

Map remains representative.

---

# CARRIER ACCOUNTS ARCHITECTURE

## PAGE MODEL

Single page.

No sub-navigation.

No separate credential section.

No history pages.

---

## RESPONSIBILITIES

Display:

- account name
- carrier
- status
- activation status

Manage:

- create
- update
- activate
- deactivate

Carrier Account is the primary displayed entity.

---

# PROFILE ARCHITECTURE

## MVP RESPONSIBILITIES

Display:

- user information

Future:

- preferences
- security settings
- notifications

---

# ADMINISTRATION ARCHITECTURE

## MVP STATUS

Placeholder.

Reserved for:

Phase 19 Administration Portal

---

# EMPTY STATES

## NO CARRIER ACCOUNT

Message:

No carrier account connected.

Connect a carrier account to start searching pickup points.

Action:

Go To Carrier Accounts

---

## NO RESULTS

Message:

No pickup points found.

Action:

Modify search criteria.

---

# ERROR STATES

## SEARCH FAILURE

Display:

Search failed.

Please retry.

---

## MAP FAILURE

Display:

Map unavailable.

Results remain available.

---

## CARRIER ACCOUNT FAILURE

Display:

Carrier account unavailable.

Please verify credentials.

---

# FROZEN ARCHITECTURE DECISIONS

## DIA-001

Homepage after login is Search.

---

## DIA-002

Search, Results and Map share the same page.

---

## DIA-003

Left sidebar is the primary navigation model.

---

## DIA-004

Pickup Point Details use a right-side drawer.

---

## DIA-005

Carrier Accounts use a single-page architecture.

---

## DIA-006

Organizations may own multiple accounts for the same carrier.

---

## DIA-007

Results and Map appear immediately after search execution.

---

## DIA-008

Map is mandatory in the MVP.

---

## DIA-009

Map full-screen mode must be supported by architecture.

---

## DIA-010

Search criteria are not persisted.

---

## DIA-011

Responsive architecture must be anticipated.

---

## DIA-012

Pickup Point selection is non-persistent.

---

## DIA-013

Results are authoritative.

Map reflects Results.

---

# OPEN DECISIONS

## UX-D001

Address Search Strategy

Still unresolved.

Possible future options:

- free text
- autocomplete
- geocoding-assisted search

This decision belongs to:

- Phase 18.4 UX Strategy
- Phase 18.9 Frontend Architecture Design
- Phase 18.10 Data Fetching & State Strategy

---

# EXIT CRITERIA

Phase 18.3 Information Architecture is complete when:

- page inventory is frozen
- navigation hierarchy is frozen
- route structure is frozen
- Search page architecture is frozen
- Carrier Account page architecture is frozen
- Search / Results / Map relationship is frozen
- Pickup Point Detail architecture is frozen
- architecture decisions are documented
- documentation is synchronized

Next Phase:

18.4 UX Strategy
