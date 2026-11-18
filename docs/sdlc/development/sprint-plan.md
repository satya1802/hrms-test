# Sprint Plan

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start sprints -->
## Sprint 1: Sprint 1

Stand up secure sign-in, password hashing, account creation, department records and multi-role assignment

Capacity: 20 points · Committed: 20

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-001 | Story | Sign in with credentials | 5 | backend-agent | — |
| US-002 | Story | Passwords stored securely | 2 | security-agent | — |
| US-003 | Story | Session expiry and sign-out | 3 | backend-agent | US-001 |
| US-004 | Story | Create user accounts without self-registration | 5 | backend-agent | — |
| US-005 | Story | Assign multiple roles with combined permissions | 3 | backend-agent | US-004 |
| US-010 | Story | Manage department records | 2 | backend-agent | — |

## Sprint 2: Sprint 2

Enforce role-scoped access control, deactivate users, manage employee records and set up projects

Capacity: 20 points · Committed: 19

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-006 | Story | Enforce role-scoped data access | 8 | security-agent | US-005 |
| ↳ US-006-T1 | Task | Implement role-permission policy engine | — | security-agent | — |
| ↳ US-006-T2 | Task | Enforce employee self-scope on profile, timesheet and leave endpoints | — | backend-agent | — |
| ↳ US-006-T3 | Task | Enforce reporting-manager scope on approval endpoints | — | backend-agent | — |
| ↳ US-006-T4 | Task | Enforce project-manager scope on project endpoints | — | backend-agent | — |
| US-007 | Story | Deactivate a user | 3 | backend-agent | US-004, US-003 |
| US-009 | Story | Manage employee records | 5 | backend-agent | US-004, US-010 |
| US-011 | Story | Create and manage projects | 3 | backend-agent | — |

## Sprint 3: Sprint 3

Enable profile self-service, project staffing, timesheet hour entry, leave-type configuration and holiday maintenance

Capacity: 20 points · Committed: 19

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-008 | Story | View and update own profile | 5 | backend-agent | US-009 |
| US-012 | Story | Assign employees to projects with allocated hours | 3 | backend-agent | US-011 |
| US-013 | Story | Log daily and weekly hours against projects | 5 | backend-agent | US-012 |
| US-016 | Story | Configure leave types and carry-over as data | 3 | backend-agent | — |
| US-021 | Story | Maintain the holiday calendar | 3 | backend-agent | — |

## Sprint 4: Sprint 4

Complete timesheet submission and status tracking, leave balances and leave application, and holiday viewing

Capacity: 20 points · Committed: 19

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-014 | Story | Submit a timesheet | 3 | backend-agent | US-013 |
| US-015 | Story | Track timesheet status | 3 | frontend-agent | US-014 |
| US-017 | Story | Maintain per-employee leave balances | 3 | backend-agent | US-016 |
| US-018 | Story | Apply for leave against balance | 5 | backend-agent | US-016, US-017 |
| US-019 | Story | View leave balances | 3 | frontend-agent | US-017, US-018 |
| US-022 | Story | View holidays | 2 | frontend-agent | US-021 |

## Sprint 5: Sprint 5

Deliver manager and HR approval workflows with audit logging

Capacity: 20 points · Committed: 20

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-020 | Story | View leave history and status | 2 | frontend-agent | US-018 |
| US-023 | Story | Review and decide team timesheets | 5 | backend-agent | US-014, US-006 |
| US-024 | Story | Review and decide team leave requests | 5 | backend-agent | US-018, US-006 |
| US-025 | Story | HR Admin override approval | 3 | backend-agent | US-023, US-024 |
| US-029 | Story | Record key actions in the audit log | 5 | backend-agent | — |

## Sprint 6: Sprint 6

Add notifications, the personal dashboard, audit-log viewing and product documentation

Capacity: 20 points · Committed: 17

| Key | Type | Title | Points | Role | Depends on |
|---|---|---|---|---|---|
| US-026 | Story | Notify on request submission | 3 | integration-agent | US-014, US-018 |
| US-027 | Story | Notify on approval decision | 3 | integration-agent | US-023, US-024 |
| US-028 | Story | View personal dashboard | 5 | backend-agent | US-013, US-015, US-018, US-019 |
| US-030 | Story | View audit logs | 3 | backend-agent | US-029 |
| US-031 | Story | Provide basic product documentation | 3 | devops-agent | — |

## Unscheduled

_Nothing unscheduled._
<!-- sdlc:auto:end sprints -->
