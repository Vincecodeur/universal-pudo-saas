# Universal PUDO SaaS - Frontend MVP Vision

Version: 1.0.0

Status: Phase 18.1 Frontend Product Vision

Last Updated: 2026-08-03

---

## PURPOSE

This document defines the product vision for the Universal PUDO SaaS Frontend MVP.

The objective is to define the first real user-facing experience before any frontend implementation starts.

This document establishes:

- product purpose
- target users
- user value
- MVP scope
- out-of-scope items
- user workflow
- frontend principles
- success criteria

No frontend code is introduced in this phase.

No backend modification is introduced in this phase.

No database change is introduced in this phase.

---

## PRODUCT VISION

Universal PUDO SaaS is primarily a PUDO Search Platform.

The platform exists to allow users to:

- search pickup points
- visualize pickup points
- compare pickup points
- inspect pickup point details
- select the most relevant pickup point

The frontend must provide a modern, simple and efficient experience.

The frontend should help users find the right information quickly.

The frontend should feel:

- simple
- visual
- intuitive
- modern
- fast

The platform is not intended to become a generic logistics platform, shipping platform or administration portal.

Its primary objective remains PUDO search and selection.

---

## MVP OBJECTIVE

The Frontend MVP exists to allow an authenticated user to:

- search pickup points
- visualize pickup point results
- compare pickup point results
- inspect pickup point details
- select a pickup point

Official MVP definition:

"Allow an authenticated user to search, visualize and select a pickup point."

---

## TARGET USERS

### Viewer

Primary user of the platform.

Responsibilities:

- search pickup points
- visualize results
- compare pickup points
- select a pickup point

The Viewer does not configure transporters.

The Viewer does not manage users.

The Viewer does not administer the platform.

---

### Owner

Organisation administrator.

Responsibilities:

- connect carrier accounts
- configure carrier credentials
- access pickup point search features
- manage organisation transport configuration

The Owner uses the same search experience as the Viewer.

---

### SaaS Administrator

Platform-level administrator.

Responsibilities:

- platform administration
- support
- organisation management

The Administration Portal is not part of the Frontend MVP.

---

## PRODUCT IDENTITY

The product should follow:

Modern SaaS

- Map Enhanced

The frontend is:

Search Driven

- Map Enhanced

The user journey starts with search.

The map enhances the results.

The map does not replace the search workflow.

---

## DEVICE STRATEGY

Primary target:

Desktop First

Secondary target:

Tablet Supported

Optional target:

Mobile

Reason:

Desktop and tablet provide the highest value for professional operational workflows.

Tablet support may become useful in warehouse and logistics environments.

Mobile support is not a priority for the MVP.

---

## AUTHENTICATION STRATEGY

Frontend MVP should support:

- Login
- Password
- Remember Me
- MFA

The architecture should remain compatible with:

- OAuth
- SSO

OAuth is not required to launch the MVP.

OAuth and SSO may be introduced later without redesigning the frontend architecture.

---

## HOMEPAGE STRATEGY

After login:

Homepage is the Search Experience.

Not a Dashboard.

Not an Administration Page.

Not an Analytics Page.

Search becomes the primary entry point of the product.

---

## EMPTY STATE STRATEGY

A pickup point search requires at least one active carrier account.

If the organisation has no connected carrier account:

Display:

- map component
- search page layout
- onboarding message
- action button

Message example:

"No transport carrier is currently connected.

Connect at least one carrier account before searching for pickup points."

Action:

"Connect a Carrier"

The action redirects the user to Carrier Account configuration.

The goal is to explain clearly why no pickup points are visible.

---

## MAIN USER JOURNEY

Login
↓
Homepage
↓
Search Address
↓
Search Results
↓
Map Visualization
↓
Pickup Point Details
↓
Pickup Point Selection

This journey is the primary workflow of the MVP.

All frontend decisions must prioritize this workflow.

---

## SEARCH STRATEGY

### Simple Search

Available immediately.

Fields:

- address
- transporter

Goal:

Fast search execution.

---

### Advanced Search

Accessible through additional filters.

Possible filters:

- radius
- pickup point type
- future carrier-specific filters

The goal is:

Simple for most users.

Powerful for advanced users.

---

## SEARCH PRINCIPLES

The user will usually start with:

A destination address.

Then:

The platform displays nearby pickup points.

The map visualizes the results.

The user compares available options.

The user selects the most relevant pickup point.

The map supports decision-making.

The map does not replace the search flow.

---

## RESULTS DISPLAY STRATEGY

Preferred display mode:

Cards

Cards should present the key information needed to compare pickup points quickly.

The user should not need to open every result to make a first selection.

---

## MAP STRATEGY

The map is visually dominant.

The map helps users:

- understand location
- compare options
- visualize distances
- identify clusters of pickup points

However:

The map is not the main business workflow.

Search and results remain primary.

The map remains a visual aid.

---

## PICKUP POINT DETAILS

Cards and map markers should expose essential information.

Priority information:

- pickup point name
- distance
- active / inactive status
- transporter logo
- transporter name
- address
- pickup point type
- important attributes
- opening hours
- phone number

---

## PICKUP POINT ATTRIBUTES

The platform must support important operational attributes.

Examples:

- large parcel support
- locker availability
- pickup point availability
- transporter-specific capabilities
- transporter-specific restrictions

Carrier-specific attributes should remain visible to users when they influence carrier selection.

---

## PICKUP POINT SELECTION CRITERIA

The most important decision factors are:

1. Active status

2. Distance

3. Parcel compatibility
   (large parcel support for example)

4. Pickup point type

5. Transporter

6. Opening hours

These criteria should guide future sorting and filtering strategies.

---

## PICKUP POINT DETAIL PANEL

After selecting a pickup point:

Display a detailed side panel.

Not a new page.

Displayed information:

- Pickup Point Name
- Relay ID
- Full Address
- Distance
- Phone Number
- Opening Hours
- Status
- Transporter Name
- Transporter Logo
- Pickup Point Type
- Carrier-Specific Attributes

All useful identifiers and addresses should be easy to copy.

---

## NAVIGATION STRATEGY

Preferred navigation:

Left Sidebar

Expected future sections:

- Search
- Map
- Carrier Accounts
- Administration
- Settings

The sidebar supports future platform growth without redesigning navigation.

---

## DASHBOARD STRATEGY

Dashboards are not part of the MVP.

Future dashboard capabilities may be added later.

The MVP must remain focused on:

search
visualization
selection

---

## NOTIFICATION STRATEGY

MVP:

Toast Messages Only

Examples:

- search completed
- error message
- no pickup points found
- session expired

Persistent notifications are out of scope.

Future notification center may support:

- carrier issues
- expired credentials
- maintenance notices
- integration alerts

---

## ERROR MANAGEMENT STRATEGY

Use business-oriented messages.

Preferred:

" No pickup points found "

Avoid:

" HTTP 404 "

Users should understand:

- what happened
- why it happened
- how to resolve it

without technical knowledge.

---

## ACCESSIBILITY STRATEGY

Target:

WCAG AA

This affects:

- colors
- contrasts
- keyboard navigation
- labels
- screen readers

Accessibility must be considered from the beginning.

---

## MULTI-LANGUAGE STRATEGY

The MVP does not require multiple languages.

However:

The architecture must be designed to support future localization.

Adding a new language should not require major frontend redesign.

---

## OUT OF SCOPE

The MVP excludes:

- Dashboard Builder
- Analytics Dashboard
- Export Platform
- Search History
- Favorite Pickup Points
- Public Website
- Blog
- CMS
- Route Planning
- Shipment Creation
- Label Generation
- Tracking Management
- Persistent Notifications
- Public APIs
- Advanced Reporting

---

## SUCCESS CRITERIA

The Frontend MVP vision is successful when:

- the target users are identified
- the product purpose is clear
- the primary workflow is defined
- the MVP scope is defined
- the out-of-scope items are defined
- the search-first philosophy is documented
- the map strategy is documented
- frontend responsibilities are defined
- future UX work can begin

---

## PHASE 18.1 EXIT CRITERIA

Phase 18.1 is complete when:

- vision is validated
- users are identified
- MVP scope is frozen
- responsibilities are documented
- product workflow is documented
- search strategy is documented
- map strategy is documented
- navigation strategy is documented

No code is required.

No database change is required.

No backend modification is required.

---

## NEXT PHASE

Phase 18.2

User Personas & User Journeys

Objectives:

- define Viewer journeys
- define Owner journeys
- define SaaS Administrator journeys
- define primary workflows
- define secondary workflows
- define permissions visibility
- prepare Information Architecture
- prepare UX Strategy

---

## DESIGN PRINCIPLE

In two years, the frontend should be described as:

"Simple, modern and enjoyable.

Users can find the information they need very quickly."
