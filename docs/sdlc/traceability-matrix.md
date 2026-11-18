# Traceability Matrix

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start legend -->
Built from recorded links, not written by a model: requirement key → plan item (`source_stable_key`) → development ticket (`stable_key`) → the ticket's test steps → the last live deployment that started after the work finished. **AC tests** counts the story's acceptance criteria that have a test case, and those whose test cases all passed in the latest finished E2E run.
<!-- sdlc:auto:end legend -->

<!-- sdlc:auto:start matrix -->
| Requirement | Epic | Title | Plan items | Sprint | Design | Code | Commits | Ticket | Tests | AC tests | Deployed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| US-001 | EPIC-001 | Sign in with credentials | US-001 | 1 | POST /auth/login, api, frontend, users | — | — | not started | not run | 0/3 tested · 0/3 passing | — |
| US-002 | EPIC-001 | Passwords stored securely | US-002 | 1 | POST /auth/set-password, api, db, users | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-003 | EPIC-001 | Session expiry and sign-out | US-003 | 1 | POST /auth/logout, api, cache, users | — | — | not started | not run | 0/3 tested · 0/3 passing | — |
| US-004 | EPIC-002 | Create user accounts without self-registration | US-004 | 1 | POST /auth/set-password, POST /users, api, db, user_roles, users | — | — | not started | not run | 0/3 tested · 0/3 passing | — |
| US-005 | EPIC-002 | Assign multiple roles with combined permissions | US-005 | 1 | PATCH /users/{id}/roles, api, db, roles, user_roles | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-006 | EPIC-002 | Enforce role-scoped data access | US-006, US-006-T1, US-006-T2, US-006-T3, US-006-T4 | 2 | GET /timesheets, POST /leave-requests/{id}/decision, POST /timesheets/{id}/decision, api, cache, employees, projects, user_roles, users | — | — | not started | not run | 0/4 tested · 0/4 passing | — |
| US-007 | EPIC-002 | Deactivate a user | US-007 | 2 | POST /users/{id}/deactivate, api, db, users | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-008 | EPIC-003 | View and update own profile | US-008 | 3 | GET /me/profile, PATCH /me/profile, api, departments, employees, frontend | — | — | not started | not run | 0/3 tested · 0/3 passing | — |
| US-009 | EPIC-003 | Manage employee records | US-009 | 2 | POST /employees, api, db, departments, employees, users | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-010 | EPIC-003 | Manage department records | US-010 | 1 | POST /departments, api, db, departments | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-011 | EPIC-004 | Create and manage projects | US-011 | 2 | POST /projects, api, db, projects | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-012 | EPIC-004 | Assign employees to projects with allocated hours | US-012 | 3 | POST /projects/{id}/assignments, api, db, employees, project_assignments, projects | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-013 | EPIC-005 | Log daily and weekly hours against projects | US-013 | 3 | POST /timesheets, api, db, frontend, project_assignments, timesheet_entries, timesheets | — | — | not started | not run | 0/3 tested · 0/3 passing | — |
| US-014 | EPIC-005 | Submit a timesheet | US-014 | 4 | POST /timesheets/{id}/submit, api, db, timesheets | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-015 | EPIC-005 | Track timesheet status | US-015 | 4 | GET /timesheets, api, frontend, timesheets | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-016 | EPIC-006 | Configure leave types and carry-over as data | US-016 | 3 | POST /leave-types, api, db, leave_types | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-017 | EPIC-006 | Maintain per-employee leave balances | US-017 | 4 | PUT /employees/{id}/leave-balances, api, db, leave_balances | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-018 | EPIC-007 | Apply for leave against balance | US-018 | 4 | POST /leave-requests, api, db, leave_balances, leave_requests | — | — | not started | not run | 0/3 tested · 0/3 passing | — |
| US-019 | EPIC-007 | View leave balances | US-019 | 4 | GET /me/leave-balances, api, frontend, leave_balances | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-020 | EPIC-007 | View leave history and status | US-020 | 5 | GET /me/leave-requests, api, frontend, leave_requests | — | — | not started | not run | 0/1 tested · 0/1 passing | — |
| US-021 | EPIC-008 | Maintain the holiday calendar | US-021 | 3 | POST /holidays, api, db, holidays | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-022 | EPIC-008 | View holidays | US-022 | 4 | GET /holidays, api, frontend, holidays | — | — | not started | not run | 0/1 tested · 0/1 passing | — |
| US-023 | EPIC-009 | Review and decide team timesheets | US-023 | 5 | POST /timesheets/{id}/decision, api, db, notifications, timesheets | — | — | not started | not run | 0/3 tested · 0/3 passing | — |
| US-024 | EPIC-009 | Review and decide team leave requests | US-024 | 5 | POST /leave-requests/{id}/decision, api, db, leave_balances, leave_requests, notifications | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-025 | EPIC-009 | HR Admin override approval | US-025 | 5 | POST /leave-requests/{id}/decision, POST /timesheets/{id}/decision, api, audit_logs, db | — | — | not started | not run | 0/1 tested · 0/1 passing | — |
| US-026 | EPIC-010 | Notify on request submission | US-026 | 6 | email, notifications, queue, worker | — | — | not started | not run | 0/1 tested · 0/1 passing | — |
| US-027 | EPIC-010 | Notify on approval decision | US-027 | 6 | email, notifications, queue, worker | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-028 | EPIC-011 | View personal dashboard | US-028 | 6 | GET /me/dashboard, api, frontend, leave_balances, leave_requests, timesheets | — | — | not started | not run | 0/3 tested · 0/3 passing | — |
| US-029 | EPIC-012 | Record key actions in the audit log | US-029 | 5 | api, audit_logs, db | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-030 | EPIC-012 | View audit logs | US-030 | 6 | GET /audit-logs, api, audit_logs, frontend | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
| US-031 | EPIC-013 | Provide basic product documentation | US-031 | 6 | — | — | — | not started | not run | 0/2 tested · 0/2 passing | — |
<!-- sdlc:auto:end matrix -->
