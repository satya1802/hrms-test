# Planning

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start narrative -->
### EPIC-001 · approved · source: planning:EPIC-001

Users authenticate directly against the HRMS (no SSO/external directory); sign-in and session security are expressed as checkable outcomes (expiry, sign-out/deactivation ending sessions, passwords never stored in plain text).

Assumption (technical stack): responsive web app backed by PostgreSQL, using session/JWT-based auth with credentials stored only as salted hashes; the specific token/storage mechanism is left to implementation, no browser-cookie behaviour is prescribed because web app and API are served from different addresses.

**Related:** US-001, US-002, US-003

### EPIC-002 · approved · source: planning:EPIC-002

Accounts are created only by HR Admin/System Admin (no public self-registration); the System Admin assigns one or more of the five roles per user with permissions combining across roles, and RBAC scopes each role's data access.

Assumption (data privacy): access is restricted to permitted roles with reasonable data-protection practices; no specific regional regime (e.g. GDPR) has been named for the operating country.

**Related:** US-004, US-005, US-006, US-007

### EPIC-003 · approved · source: planning:EPIC-003

Employees view/update their own profile within permitted fields; HR Admin manages employee records, department records and reporting-manager relationships that drive manager scoping elsewhere in the portal.

**Related:** US-008, US-009, US-010

### EPIC-004 · approved · source: planning:EPIC-004

Project Managers create and manage their own projects and assign employees with allocated hours; timesheets are logged against these projects.

**Related:** US-011, US-012

### EPIC-005 · approved · source: planning:EPIC-005

Employees log daily/weekly hours against assigned projects, submit timesheets, and track status through draft, submitted, approved or rejected.

**Related:** US-013, US-014, US-015

### EPIC-006 · approved · source: planning:EPIC-006

Leave types, entitlements, accrual and annual carry-over are configured as data by HR Admin rather than hardcoded statutory rules; balances are tracked per employee per leave type for a single-country workforce.

Assumption (leave policy): one set of leave rules applies since the workforce is in a single country.

**Related:** US-016, US-017

### EPIC-007 · approved · source: planning:EPIC-007

Employees apply for leave against their available balances, view balances per leave type, and see their leave history and request status; applications route to the reporting manager for approval.

**Related:** US-018, US-019, US-020

### EPIC-008 · approved · source: planning:EPIC-008

HR Admin maintains a single organisation holiday calendar for the operating country as configured data (not statutory rules); employees can view it.

**Related:** US-021, US-022

### EPIC-009 · approved · source: planning:EPIC-009

Timesheet and leave approvals are single-level: the employee's reporting manager approves/rejects with a comment, and HR Admin can act as an override/fallback approver. No multi-stage escalation in this build.

Assumption (approval workflow): approvals and rejections trigger notifications and are written to the audit log.

**Related:** US-023, US-024, US-025

### EPIC-010 · approved · source: planning:EPIC-010

Request, approval and rejection events are delivered both by email and as in-app notifications.

Assumption (notifications): email requires an email-provider credential, stored as a placeholder such as <email-provider-api-key> and never a real value.

**Related:** US-026, US-027

### EPIC-011 · approved · source: planning:EPIC-011

Each signed-in user gets a personal dashboard summarising their own timesheets and leave, scoped strictly to their own data.

Assumption (reporting): broader reporting dashboards and CSV/PDF export for managers, project managers and HR Admin (team availability, project utilisation, org-wide HR reports) are deferred beyond this Lightweight MVP and not included in this version.

**Related:** US-028

### EPIC-012 · approved · source: planning:EPIC-012

All approvals, rejections, modifications and administrative actions are recorded in an immutable audit log; the System Admin can view and filter it.

**Related:** US-029, US-030

### EPIC-013 · approved · source: planning:EPIC-013

Basic product documentation is provided so administrators can set up the portal and users understand the core flows.

Setup documentation references secrets only as placeholders such as <email-provider-api-key> and <database-password>, never real values. Out of scope for this version: payroll/HR system export or sync, and biometric/badge attendance-device integration.

**Related:** US-031
<!-- sdlc:auto:end narrative -->
