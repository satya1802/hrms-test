<!-- sdlc:auto:start adr -->
# ADR-0002: Use FastAPI 0.115 for Backend

Status: Accepted  
Date: 2026-11-18

## Context and Problem Statement

Which Backend technology does the project use? Decided in architecture v1.

## Considered Options

- FastAPI 0.115
- Django REST Framework
- Flask

## Decision Outcome

Chosen option: FastAPI 0.115, because The approved stack. Expresses the product's rules — RBAC scoping, single-level approvals, leave balance and overlap checks, immutable audit writes — as a documented API the React screens call, with automatic OpenAPI docs aiding post-launch maintenance. Enqueues emails rather than sending them inline so requests return immediately.

## Consequences

Async background work needs a separate worker process and queue; shared here with Redis rather than an added broker.
<!-- sdlc:auto:end adr -->