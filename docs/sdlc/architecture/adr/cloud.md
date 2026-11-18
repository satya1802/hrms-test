<!-- sdlc:auto:start adr -->
# ADR-0004: Use AWS for Cloud

Status: Accepted  
Date: 2026-11-18

## Context and Problem Statement

Which Cloud technology does the project use? Decided in architecture v1.

## Considered Options

- AWS
- Azure
- GCP

## Decision Outcome

Chosen option: AWS, because The approved stack. Hosts the API and worker containers, managed PostgreSQL via RDS (backups and patching handled for sensitive employee data), Redis in a private subnet, and S3 for profile documents and exports, all within private networking that keeps the portal internal for ~200-1000 staff.

## Consequences

RDS and private networking add operational setup over a single box, but remove day-to-day backup and patch burden on sensitive data.
<!-- sdlc:auto:end adr -->