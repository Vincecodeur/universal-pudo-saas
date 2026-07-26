# Future Consumers

Version: 1.0

Status: Draft

Last Updated: 2026-07-26

---

# Purpose

This document identifies future consumers of Universal PUDO Engine.

Each consumer owns its own integration contract with the Engine.

The Engine remains the owner of carrier integrations.

Consumers remain responsible for how they consume Engine capabilities.

---

# Consumer Ownership Rule

Universal PUDO Engine owns:

- carrier implementations
- carrier discovery
- provider execution
- pickup point normalization
- search orchestration

Consumers own:

- user experience
- configuration
- authentication
- credential management
- integration contract documentation

---

# Current Consumer

## Universal PUDO SaaS

Repository:

```text
universal-pudo-saas
```

Relationship:

```text
Engine Consumer
```

Contract documentation:

```text
docs/ecosystem/
```

---

# Future Consumers

## Python SDK

Repository:

```text
universal-pudo-sdk-python
```

Purpose:

```text
Provide a Python developer experience
on top of Universal PUDO Engine.
```

Own contract documentation:

```text
docs/ecosystem/
```

---

## TypeScript SDK

Repository:

```text
universal-pudo-sdk-typescript
```

Purpose:

```text
Provide TypeScript interfaces
for frontend and backend consumers.
```

Own contract documentation:

```text
docs/ecosystem/
```

---

## WooCommerce Plugin

Repository:

```text
universal-pudo-cms-woocommerce
```

Purpose:

```text
Integrate pickup point selection
inside WooCommerce.
```

Own contract documentation:

```text
docs/ecosystem/
```

---

## Prestashop Plugin

Repository:

```text
universal-pudo-cms-prestashop
```

Purpose:

```text
Integrate pickup point selection
inside Prestashop.
```

Own contract documentation:

```text
docs/ecosystem/
```

---

# Architectural Rule

Consumers never define Engine behavior.

Consumers consume Engine capabilities.

The Engine remains the single source of truth for:

- carriers
- providers
- capabilities
- search behavior
- normalization

---

# Decision Summary

Every consumer owns its own contract documentation.

No global consumer contract repository is required.

Each repository is responsible for documenting how it consumes Universal PUDO Engine.
