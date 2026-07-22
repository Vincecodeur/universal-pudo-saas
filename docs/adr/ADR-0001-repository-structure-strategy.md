# ADR-0001 - Repository Structure Strategy

Status: Accepted

Date: 2026-07-22

Authors:

- Vincent Gueret
- Microsoft Copilot

---

# Context

Universal PUDO SaaS is being developed as a platform built on top of:

Universal PUDO Engine

The project contains:

- frontend
- backend
- documentation
- future ADRs
- future tests

A repository structure decision is required before any application code is created.

The objective is to define a repository strategy that supports:

- long-term maintainability
- architectural clarity
- developer productivity
- SaaS growth
- future self-host compatibility

while avoiding unnecessary complexity.

---

# Problem Statement

Should Universal PUDO SaaS be implemented as:

Option A

Single Repository (Monorepo)

or

Option B

Multiple Repositories

Examples:

- universal-pudo-saas-frontend
- universal-pudo-saas-backend

---

# Decision

Accepted Option:

Option A

Monorepo

Repository:

universal-pudo-saas

---

# Target Structure

Target structure after technical foundations:

```text
UNIVERSAL-PUDO-SAAS/
│
├── docs/
│
├── backend/
│
├── frontend/
│
├── tests/
│
├── README.md
├── CHANGELOG.md
└── .gitignore
```

The structure will be created progressively.

Directories should not be created before they are required.

---

# Decision Drivers

The following factors influenced the decision.

---

## Simplicity

Current project team:

Single primary contributor.

The overhead of multiple repositories would exceed the benefits.

---

## Architectural Alignment

The SaaS is delivered as a single product.

Users consume:

Universal PUDO SaaS

not:

Frontend separately

Backend separately

A monorepo reflects product reality.

---

## Documentation Consistency

Project documentation remains easier to maintain when:

- roadmap
- architecture
- implementation

are located in a single repository.

---

## Development Velocity

A monorepo simplifies:

- issue tracking
- commits
- releases
- architecture reviews

during the early project stages.

---

## Deployment Independence

Although development occurs in a monorepo:

Frontend and backend remain logically separated.

Future deployment strategies remain possible.

Examples:

- separate containers
- separate services
- separate infrastructure

---

# Rejected Alternatives

---

## Option B

Multiple Repositories

Example:

```text
universal-pudo-saas-frontend
universal-pudo-saas-backend
```

Status:

Rejected

---

### Reasons

Increases:

- repository management
- release management
- documentation complexity
- onboarding complexity

without providing significant value at the current project size.

---

# Consequences

---

## Positive Consequences

```text
Single source of truth
Simpler project management
Unified documentation
Simpler releases
Simpler onboarding
```

---

## Negative Consequences

```text
Larger repository over time
Need for clear module boundaries
Need for architecture discipline
```

These drawbacks are acceptable.

---

# Architectural Constraints

This ADR does not authorize:

- frontend code inside backend modules
- backend code inside frontend modules
- removal of module boundaries

The repository is shared.

Responsibilities remain separated.

---

# Future Re-evaluation

This decision may be reviewed if:

- the team size increases significantly
- independent release cycles become necessary
- operational requirements change

Current expectation:

The monorepo strategy remains valid for the foreseeable future.

---

# Related Documents

- docs/project-memory.md
- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md
- docs/project-status.md

---

# Status History

2026-07-22

Accepted.
