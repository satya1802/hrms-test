<!-- sdlc:auto:start adr -->
# ADR-0001: Use React 19 for Frontend

Status: Accepted  
Date: 2026-11-18

## Context and Problem Statement

Which Frontend technology does the project use? Decided in architecture v1.

## Considered Options

- React 19
- Vue
- Angular

## Decision Outcome

Chosen option: React 19, because The approved stack. Built as a Vite single-page app on its own origin that stores the opaque session token and sends it as Authorization: Bearer; one responsive layout serves the employee's phone and the manager's laptop, and role-driven views (approval queues, balance trackers, personal dashboard) render different slices of the same data.

## Consequences

A separate SPA origin means no shared cookies with the API, so session state is carried by a Bearer token the app stores and attaches to every call.
<!-- sdlc:auto:end adr -->