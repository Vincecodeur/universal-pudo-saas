# Ecosystem Documentation

Version: 1.0

Status: Accepted

Last Updated: 2026-07-26

Location:

docs/ecosystem/README.md

---

# Purpose

This folder contains ecosystem-level documentation for the Universal PUDO SaaS repository.

Its purpose is to document how Universal PUDO SaaS consumes Universal PUDO Engine and how the repository boundaries must be maintained across the Universal PUDO ecosystem.

This folder exists to prevent confusion between:

- Engine responsibilities
- SaaS responsibilities
- consumer contract responsibilities
- future plugin responsibilities
- future SDK responsibilities

---

# Repository Scope

This folder belongs to:

```text
universal-pudo-saas
```

The SaaS repository is the first official consumer of Universal PUDO Engine.

The documents in this folder describe how the SaaS consumes the Engine and how future consumer contracts should be organized.

---

# Important Rule

The documents in this folder are not Engine ADRs.

The documents in this folder are not Engine implementation documents.

The documents in this folder are consumer-side ecosystem documents.

They describe how Universal PUDO SaaS and future consumers should interact with Universal PUDO Engine.

---

# Current Repositories

## Universal PUDO Engine

Repository:

```text
universal-pudo-engine
```

Role:

```text
Reusable Core
```

Owns:

- carrier integrations
- provider implementations
- carrier clients
- carrier parsers
- carrier mappers
- pickup point normalization
- provider discovery
- provider execution
- hybrid search
- synchronization
- provider health
- public Core interfaces

Does not own:

- SaaS users
- SaaS organisations
- SaaS memberships
- SaaS authentication
- SaaS carrier accounts
- SaaS credentials
- SaaS administration
- SaaS dashboards
- SaaS frontend

---

## Universal PUDO SaaS

Repository:

```text
universal-pudo-saas
```

Role:

```text
SaaS consumer of Universal PUDO Engine
```

Owns:

- authentication
- users
- organisations
- memberships
- permissions
- carrier accounts
- carrier credentials
- administration
- future dashboards
- future billing
- future frontend
- SaaS consumption of Engine capabilities

Does not own:

- carrier integrations
- provider implementations
- carrier clients
- carrier parsers
- carrier mappers
- carrier normalization
- Engine search orchestration

---

# Folder Contents

This folder contains the following documents.

---

## repository-ownership.md

Purpose:

Defines ownership boundaries between repositories.

Use this document when there is uncertainty about where a change belongs.

Examples:

- Engine change
- SaaS change
- contract change
- future plugin change
- future SDK change

This document is the main guardrail against mixing repository responsibilities.

---

## engine-saas-contract.md

Purpose:

Defines the integration contract between:

```text
universal-pudo-engine
```

and:

```text
universal-pudo-saas
```

This document describes:

- what the Engine owns
- what the SaaS owns
- how the SaaS consumes Engine capabilities
- how carriers should be discovered
- how carrier accounts relate to Engine carriers
- how the SaaS avoids duplicating carrier logic

---

## adr-ecosystem-0001-public-contract.md

Purpose:

Documents the ecosystem-level public contract strategy.

This ADR explains why consumer repositories must define their own contracts with Universal PUDO Engine.

This is not an Engine ADR.

This is an ecosystem ADR owned by the consumer side.

---

## adr-ecosystem-0002-publication-rules.md

Purpose:

Documents carrier publication rules from the consumer perspective.

Main rule:

```text
Users must only see carriers that they can actually use.
```

Consumers must not expose unfinished, inactive, unavailable, or unsupported carriers.

---

## future-consumers.md

Purpose:

Lists future repositories that may consume Universal PUDO Engine.

Examples:

- Python SDK
- TypeScript SDK
- WooCommerce plugin
- Prestashop plugin
- future CMS plugins
- future checkout integrations

Each future consumer will own its own contract documentation inside its own repository.

---

# Contract Ownership Model

Each consumer owns its own Engine contract.

Examples:

```text
Engine ↔ SaaS contract
```

lives in:

```text
universal-pudo-saas/docs/ecosystem/
```

```text
Engine ↔ WooCommerce contract
```

will live in:

```text
universal-pudo-cms-woocommerce/docs/ecosystem/
```

```text
Engine ↔ Python SDK contract
```

will live in:

```text
universal-pudo-sdk-python/docs/ecosystem/
```

There is no central contract repository at this stage.

---

# Why Contracts Live With Consumers

The Engine defines what it can do.

The consumer defines how it consumes Engine capabilities.

Therefore, each consumer repository must document its own expectations, constraints, workflows, and integration rules.

This prevents:

- Engine documentation from becoming polluted with consumer-specific workflows
- SaaS documentation from describing plugin-specific behavior
- plugin repositories from depending on SaaS assumptions
- SDK repositories from inheriting SaaS-specific constraints

---

# Decision Categories

All future decisions must be classified into one of the following categories.

---

## ENGINE

A decision belongs to the Engine when it concerns:

- provider behavior
- carrier implementation
- provider discovery
- pickup point search
- normalization
- synchronization
- provider health
- Engine public interfaces
- Engine data model

Repository:

```text
universal-pudo-engine
```

---

## SAAS

A decision belongs to the SaaS when it concerns:

- users
- organisations
- memberships
- authentication
- carrier accounts
- carrier credentials
- permissions
- dashboards
- administration
- frontend
- SaaS user experience

Repository:

```text
universal-pudo-saas
```

---

## CONTRACT

A decision belongs to the contract when it concerns:

- how the SaaS consumes Engine capabilities
- how the SaaS discovers available carriers
- how the SaaS interprets Engine carrier lifecycle
- how the SaaS activates a carrier
- how the SaaS remains compatible with Engine versions

Repository:

```text
universal-pudo-saas/docs/ecosystem/
```

for the SaaS consumer contract.

Future consumers will own their own contract folders.

---

# Repository Navigation Rule

Before modifying code or documentation, the active scope must be explicit.

Examples:

```text
[REPOSITORY ACTIF]
universal-pudo-engine
```

or:

```text
[REPOSITORY ACTIF]
universal-pudo-saas
```

or:

```text
[SUJET]
ENGINE ↔ SAAS CONTRACT
```

No implementation work should begin before the active repository or contract scope is clearly identified.

---

# Modification Examples

## Add a new carrier integration

Repository:

```text
universal-pudo-engine
```

Reason:

Carrier integrations belong to the Engine.

---

## Add a carrier activation screen

Repository:

```text
universal-pudo-saas
```

Reason:

The activation screen is part of the SaaS user experience.

---

## Define how the SaaS discovers carriers

Repository:

```text
universal-pudo-saas/docs/ecosystem/
```

Reason:

This is an Engine ↔ SaaS contract decision.

---

## Add WooCommerce checkout pickup point selection

Repository:

```text
universal-pudo-cms-woocommerce
```

Reason:

WooCommerce checkout behavior belongs to the WooCommerce plugin.

---

## Define Engine ↔ WooCommerce contract

Repository:

```text
universal-pudo-cms-woocommerce/docs/ecosystem/
```

Reason:

The WooCommerce plugin owns its own consumption contract.

---

# Golden Rules

## Rule 1

The Engine owns carrier functionality.

---

## Rule 2

The SaaS owns SaaS user experience and SaaS configuration.

---

## Rule 3

Each consumer owns its own Engine contract documentation.

---

## Rule 4

No consumer reimplements carrier integrations.

---

## Rule 5

No repository should document behavior that belongs to another repository unless it is explicitly part of an integration contract.

---

# Current Status

Current consumer:

```text
universal-pudo-saas
```

Current Engine:

```text
universal-pudo-engine
```

Current contract folder:

```text
universal-pudo-saas/docs/ecosystem/
```

Current purpose of this folder:

```text
Document the Engine ↔ SaaS contract
and define future consumer ownership rules.
```

---

# Future Evolution

When new consumer repositories are created, each repository should include its own:

```text
docs/ecosystem/
```

folder.

Examples:

```text
universal-pudo-cms-woocommerce/docs/ecosystem/
```

```text
universal-pudo-cms-prestashop/docs/ecosystem/
```

```text
universal-pudo-sdk-python/docs/ecosystem/
```

```text
universal-pudo-sdk-typescript/docs/ecosystem/
```

Each future folder should contain the contract between that consumer and Universal PUDO Engine.

---

# Decision Summary

The Universal PUDO ecosystem is composed of independent repositories.

Universal PUDO Engine owns carrier functionality.

Universal PUDO SaaS owns SaaS functionality.

Each consumer owns its own Engine contract documentation.

This folder exists to prevent repository confusion and to provide a stable documentation area for the Engine ↔ SaaS contract.
