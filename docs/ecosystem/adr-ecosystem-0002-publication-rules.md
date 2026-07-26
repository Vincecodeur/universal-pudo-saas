# ADR-ECOSYSTEM-0002 - Carrier Publication Rules

Status: Accepted

Date: 2026-07-26

---

# Context

Consumers must expose only carriers that are actually usable.

The user experience must reflect operational reality.

An unfinished, disabled or unavailable carrier must not appear as available for activation.

---

# Decision

Consumers must only expose carriers that are considered available by the Engine.

Consumers must never manually maintain their own carrier catalog.

The Engine remains the source of truth.

---

# Consumer Rule

Consumers may:

- display available carriers
- allow activation of available carriers
- display carrier capabilities

Consumers must not:

- create extra carriers
- duplicate carrier definitions
- maintain a separate carrier catalog

---

# User Experience Rule

Users must only see carriers they can use.

Unavailable carriers must remain hidden.

Experimental carriers must not be displayed.

---

# Benefits

- consistent user experience
- single source of truth
- reduced maintenance
- reduced support effort

---

# Result

Carrier visibility is driven by Engine availability.

Consumers merely present Engine-supported carriers.
