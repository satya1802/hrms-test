# Planning

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start narrative -->
### EPIC-001 · approved · source: planning:EPIC-001

Users authenticate directly against the HRMS (no SSO/external directory) with session/JWT-based auth and salted password hashes.

Goal: stand up secure sign-in and session security so that sessions expire, sign-out and deactivation end sessions immediately, and passwords are never stored in plain text. Token/storage mechanism left to implementation; no browser-cookie behavior prescribed since the web app and API are served from different addresses.

**Related:** US-001, US-002, US-003

### EPIC-002 · approved · source: planning:EPIC-002

Accounts are provisioned only by HR Admin/System Admin (no public self-registration), with multi-role assignment and strict role-scoped data access.

Goal: let System Admin assign one or more of five roles per user with combined permissions, enforce that employees/managers/project managers act only within their own scope, and allow deactivation of leavers. Assumption noted: data-protection practices are reasonable-effort; no specific regional regime (e.g. GDPR) was named.

**Related:** US-004, US-005, US-006, US-007

### EPIC-003 · approved · source: planning:EPIC-003

Employees can view/update their own profile within permitted fields; HR Admin manages employee and department records and reporting-manager relationships.

Goal: maintain accurate organization structure (departments, reporting lines) as the basis for manager scoping used across timesheets, leave, and approvals.

**Related:** US-008, US-009, US-010

### EPIC-004 · approved · source: planning:EPIC-004

Project Managers create and manage their own projects and assign employees with allocated hours for timesheet logging.

Goal: give Project Managers full control of their own projects (including staffing and allocated hours) while restricting them from projects they do not own.

**Related:** US-011, US-012

### EPIC-005 · approved · source: planning:EPIC-005

Employees log daily/weekly hours against assigned projects, submit timesheets for approval, and track status.

Goal: capture worked time accurately and route submitted timesheets to the reporting manager, with status progressing through draft, submitted, approved or rejected.

**Related:** US-013, US-014, US-015

### EPIC-006 · approved · source: planning:EPIC-006

HR Admin configures leave types, entitlements and carry-over rules as data, and maintains per-employee leave balances.

Goal: let leave rules reflect organizational policy without code changes, since the workforce is in a single country with one set of leave rules; balances are tracked per employee per leave type.

**Related:** US-016, US-017

### EPIC-007 · approved · source: planning:EPIC-007

Employees apply for leave against their balances, view remaining balances per type, and review their leave history and status.

Goal: let employees self-serve leave applications routed to their reporting manager for approval, with visibility into balances and past/pending requests.

**Related:** US-018, US-019, US-020

### EPIC-008 · approved · source: planning:EPIC-008

HR Admin maintains a single organization holiday calendar; employees can view it.

Goal: configure public holidays as data (not hardcoded to statutory rules) for the single operating country, so employees see correct non-working days.

**Related:** US-021, US-022

### EPIC-009 · approved · source: planning:EPIC-009

Single-level approval workflow: reporting managers approve/reject their direct reports' timesheets and leave with comments; HR Admin can override.

Goal: validate worked hours and authorize time off through one approval level (no multi-stage escalation), with HR Admin acting as fallback approver when the manager is unavailable. Approvals/rejections trigger notifications and audit entries.

**Related:** US-023, US-024, US-025

### EPIC-010 · approved · source: planning:EPIC-010

Submission and approval-decision events are delivered via in-app notification and email.

Goal: notify reporting managers of pending submissions and notify employees of approval/rejection outcomes. Email requires an email-provider credential stored only as a placeholder (e.g. <email-provider-api-key>); if not configured, in-app notification still delivers and the email failure is logged.

**Related:** US-026, US-027

### EPIC-011 · approved · source: planning:EPIC-011

Each signed-in user gets a personal dashboard summarizing only their own timesheets and leave.

Goal: give users an at-a-glance view of their recent timesheet status and leave balances on sign-in. Broader manager/HR reporting dashboards and CSV/PDF export are explicitly deferred beyond this MVP.

**Related:** US-028

### EPIC-012 · approved · source: planning:EPIC-012

All approvals, rejections, modifications and admin actions are recorded in an immutable audit log, viewable by System Admin.

Goal: provide accountable history of who did what for data-protection and investigation purposes; audit entries cannot be edited or deleted once written.

**Related:** US-029, US-030

### EPIC-013 · approved · source: planning:EPIC-013

Basic product documentation covers setup and core user flows for administrators.

Goal: document login, user provisioning, leave/holiday configuration, timesheet and leave flows, and approvals, with every secret shown only as a bracketed placeholder (e.g. <email-provider-api-key>, <database-password>). Payroll/HR export/sync and biometric/badge attendance integration are explicitly out of scope for this version.

**Related:** US-031

### SPRINT-1 · approved · source: plan:Sprint 1

Sprint 1 stands up secure sign-in, password hashing, account creation, department records and multi-role assignment.

Capacity 20 points. Inferred item mapping from goal wording: US-001 Sign in with credentials (5, backend-agent), US-002 Passwords stored securely (2, security-agent), US-003 Session expiry and sign-out (3, backend-agent), US-004 Create user accounts without self-registration (5, backend-agent), US-005 Assign multiple roles with combined permissions (3, backend-agent), US-010 Manage department records (2, backend-agent). Sum of points = 20, matching stated capacity exactly.

**Related:** EPIC-001, US-001, US-002, US-003, US-004, US-005, US-010

### SPRINT-2 · approved · source: plan:Sprint 2

Sprint 2 enforces role-scoped access control, deactivates users, manages employee records, and sets up projects.

Capacity 20 points. Inferred item mapping: US-006 Enforce role-scoped data access (8, security-agent), decomposed into tasks US-006-T1 Implement role-permission policy engine (security-agent), US-006-T2 Enforce employee self-scope on profile/timesheet/leave endpoints (backend-agent), US-006-T3 Enforce reporting-manager scope on approval endpoints (backend-agent), US-006-T4 Enforce project-manager scope on project endpoints (backend-agent); US-007 Deactivate a user (3, backend-agent); US-009 Manage employee records (5, backend-agent); US-011 Create and manage projects (3, backend-agent). Points sum = 19 of 20 capacity (tasks carry no separate points).

**Related:** US-006, US-006-T1, US-006-T2, US-006-T3, US-006-T4, US-007, US-009, US-011

### SPRINT-3 · approved · source: plan:Sprint 3

Sprint 3 enables profile self-service, project staffing, timesheet hour entry, leave-type configuration and holiday maintenance.

Capacity 20 points. Inferred item mapping: US-008 View and update own profile (5, backend-agent), US-012 Assign employees to projects with allocated hours (3, backend-agent), US-013 Log daily and weekly hours against projects (5, backend-agent), US-016 Configure leave types and carry-over as data (3, backend-agent), US-021 Maintain the holiday calendar (3, backend-agent). Points sum = 19 of 20 capacity.

**Related:** US-008, US-012, US-013, US-016, US-021

### SPRINT-4 · approved · source: plan:Sprint 4

Sprint 4 completes timesheet submission and status tracking, leave balances and leave application, and holiday viewing.

Capacity 20 points. Inferred item mapping: US-014 Submit a timesheet (3, backend-agent), US-015 Track timesheet status (3, frontend-agent), US-017 Maintain per-employee leave balances (3, backend-agent), US-018 Apply for leave against balance (5, backend-agent), US-019 View leave balances (3, frontend-agent), US-020 View leave history and status (2, frontend-agent), US-022 View holidays (2, frontend-agent). Points sum = 21, slightly above the stated 20-point capacity.

**Related:** US-014, US-015, US-017, US-018, US-019, US-020, US-022

### SPRINT-5 · approved · source: plan:Sprint 5

Sprint 5 delivers manager and HR approval workflows with audit logging.

Capacity 20 points. Inferred item mapping: US-023 Review and decide team timesheets (5, backend-agent), US-024 Review and decide team leave requests (5, backend-agent), US-025 HR Admin override approval (3, backend-agent), US-029 Record key actions in the audit log (5, backend-agent). Points sum = 18 of 20 capacity.

**Related:** US-023, US-024, US-025, US-029

### SPRINT-6 · approved · source: plan:Sprint 6

Sprint 6 adds notifications, the personal dashboard, audit-log viewing and product documentation.

Capacity 20 points. Inferred item mapping: US-026 Notify on request submission (3, integration-agent), US-027 Notify on approval decision (3, integration-agent), US-028 View personal dashboard (5, backend-agent), US-030 View audit logs (3, backend-agent), US-031 Provide basic product documentation (3, devops-agent). Points sum = 17 of 20 capacity.

**Related:** US-026, US-027, US-028, US-030, US-031
<!-- sdlc:auto:end narrative -->
