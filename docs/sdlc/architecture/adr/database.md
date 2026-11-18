<!-- sdlc:auto:start adr -->
# ADR-0003: Use PostgreSQL 16 for Database

Status: Accepted  
Date: 2026-11-18

## Context and Problem Statement

Which Database technology does the project use? Decided in architecture v1.

## Considered Options

- PostgreSQL 16
- MySQL
- SQL Server

## Decision Outcome

Chosen option: PostgreSQL 16, because The approved stack. Holds the highly relational HRMS data as the single source of truth and keeps per-employee leave balances and approval status consistent within transactions; jsonb covers flexible audit detail and the append-only audit log is enforced at the database level.

## Consequences

Carry-over rollover and balance deduction must be written as careful transactions, but relational integrity is exactly what this data needs.
<!-- sdlc:auto:end adr -->