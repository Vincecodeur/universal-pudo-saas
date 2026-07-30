# ADR-0009 - Carrier Publication Rules

Status: Proposed

Date: 2026-07-26

Decision Type: Architecture

Related ADRs:

- ADR-0007 Carrier Catalog Ownership
- ADR-0008 Public Engine Contract

---

# Context

Universal PUDO Engine is the single source of truth for carrier definitions.

ADR-0008 established that all consumers access carrier information through the Public Engine Contract.

Consumers include:

- Universal PUDO SaaS
- Engine APIs
- Shopify Plugins
- WooCommerce Plugins
- CLI Applications
- Future Products

The Engine must guarantee that consumers only see carriers that are actually usable.

A carrier that is partially implemented, under development, or misconfigured must not appear in the public catalog.

---

# Problem

With the carrier auto-discovery strategy, a carrier definition may exist before the provider implementation is complete.

Example:

```text
providers/

dpd_south_africa/

├── definition.py
└── provider.py
```

Possible situations:

```text
definition.py exists

provider.py missing
```

or

```text
definition.py exists

provider.py exists

provider implementation incomplete
```

or

```text
provider registration invalid
```

If the public catalog exposes these carriers, consumers may display capabilities that are not actually usable.

Example:

```text
Universal PUDO SaaS

shows:

DPD South Africa

but:

search_pickup_points()

does not work.
```

This creates false expectations and violates product reliability principles.

---

# Decision

A carrier becomes publicly discoverable only when its provider is fully registered and validated.

Carrier definitions alone are not sufficient for publication.

The Public Engine Contract must expose only validated carriers.

---

# Publication Rule

A carrier is considered publishable when all publication requirements are satisfied.

Required conditions:

```text
✅ definition.py exists

✅ provider.py exists

✅ provider implements required contracts

✅ provider registration is valid

✅ provider passes startup validation

✅ provider is marked as active
```

Only then may the carrier appear in:

```text
get_available_carriers()
```

and

```text
get_carrier_definition()
```

---

# Non-Publishable Carriers

The following carriers must not appear in the public catalog:

## Missing Provider

```text
definition.py present

provider.py missing
```

Result:

```text
Not Published
```

---

## Incomplete Implementation

```text
provider.py exists

required methods missing
```

Result:

```text
Not Published
```

---

## Registration Failure

```text
provider registration failed
```

Result:

```text
Not Published
```

---

## Startup Validation Failure

```text
provider validation failed
```

Result:

```text
Not Published
```

---

## Disabled Provider

```text
provider marked inactive
```

Result:

```text
Not Published
```

---

# Discovery Workflow

Carrier discovery follows this process:

```text
Provider Discovery
        ↓
Provider Validation
        ↓
Provider Registration
        ↓
Publication Eligibility Check
        ↓
Public Catalog Exposure
```

A carrier becomes visible only after passing every step.

---

# Example

Development State:

```text
providers/

dpd_sa/

├── definition.py
└── provider.py
```

Status:

```text
Implementation incomplete
```

Result:

```text
❌ Not discoverable

❌ Not visible in SaaS

❌ Not visible in APIs

❌ Not visible in Plugins
```

---

After completion:

```text
definition.py valid

provider.py valid

registration valid

validation successful
```

Result:

```text
✅ Discoverable

✅ Visible in SaaS

✅ Visible in APIs

✅ Visible in Plugins
```

---

# Public Catalog Principle

The Public Contract represents reality.

The public catalog must never expose:

```text
planned carriers

experimental carriers

unfinished carriers

invalid carriers
```

The public catalog must expose only:

```text
usable carriers
```

---

# Benefits

## Reliability

Consumers only see features that actually work.

---

## User Experience

Users never discover unusable carriers.

---

## Product Consistency

All consumers share the same eligibility rules.

---

## Reduced Support Costs

No false-positive carrier availability.

---

## Safer Development

Developers can work on a provider without exposing unfinished functionality.

---

# Consequences

Carrier publication becomes a controlled process.

Adding a carrier now requires:

```text
1. Create definition

2. Implement provider

3. Validate provider

4. Register provider

5. Automatic publication
```

Publication is automatic.

Publication is never manual.

Publication is never based solely on carrier definitions.

---

# Architectural Rule

The Public Engine Contract must expose only carriers that are fully operational.

A carrier definition does not make a carrier discoverable.

A validated provider makes a carrier discoverable.

---

# Decision Summary

Universal PUDO Engine uses automatic carrier discovery.

Carrier publication is based on validated provider availability rather than carrier definitions alone.

All consumers must see only carriers that are fully implemented, validated, and usable.

This guarantees that the public catalog always reflects operational reality.
