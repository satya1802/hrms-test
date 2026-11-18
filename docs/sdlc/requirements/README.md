# Product Requirements

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start narrative -->
## Summary

### REQ-TECH-001 · approved · source: requirements:technology-stack

Technology stack approved by the product owner for the portal: FastAPI backend, PostgreSQL database, React frontend, hosted on AWS. Must be designed against exactly these, no substitutions.

- Backend: FastAPI 0.115 -- chosen to express RBAC rules, single-level approvals, configurable leave accrual/carry-over, and per-admin-action audit entries as a well-documented API for the React screens; scale (200-1000 employees, internal) is well within its reach.
- Cloud: AWS -- hosts the app, PostgreSQL (via RDS) and stored documents/exports (via S3) for a single-organisation internal portal; managed DB reduces backup/patching burden on sensitive employee data.
- Database: PostgreSQL 16 -- enforces the highly relational data model (employees/departments/managers/projects/leave balances/audit trail); the system is the single source of truth with no payroll to reconcile against.
- Frontend: React 19 -- builds the role-driven interactive screens (approval queues, utilisation charts, balance trackers) in one responsive layout for laptop and phone.

### REQ-SVC-001 · approved · source: requirements:services

Runtime services approved for the build: email delivery, background queue, file storage and cache, plus the API keys/env vars each needs.

- Email: SendGrid (SaaS, env SENDGRID_API_KEY) -- delivers approval/rejection/request notification emails without running a mail server.
- Queue: Redis as a queue (container redis:7-alpine) -- runs notification emails and org-wide CSV/PDF report generation in the background so approval clicks and report requests don't block the user.
- File storage: Amazon S3 (SaaS, env AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, S3_BUCKET) -- durable storage for uploaded profile documents and generated report files outside the database.
- Cache: Redis (container redis:7-alpine) -- caches role/permission checks and in-app notification lookups so the portal stays responsive at morning login peak.
- Required API keys/env vars: AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY, REDIS_URL, S3_BUCKET, SENDGRID_API_KEY (all real values must be stored as placeholders in docs, e.g. <sendgrid-api-key>).

### REQ-SCOPE-001 · approved · source: requirements:scope

Delivery scope is lightweight (requirements v1, approved). Defines what is in scope for this build and what is explicitly excluded.

In scope: secure employee login; own profile view/update; daily and weekly timesheet entry against projects; timesheet submission and status tracking; leave application against balances; leave balance and history view; holiday calendar view; personal dashboard of own timesheets/leave; project and department records; leave type and per-employee balance records as configurable data (not statutory rules); basic product documentation.
Out of scope -- not to be designed or built: payroll/HR system export or sync; biometric/badge attendance-device integration.

### REQ-FEAT-SIGNIN · approved · source: requirements:feature:Sign-in & accounts

Covers secure sign-in and session lifecycle for registered users.

- Sign in with credentials: a registered user signs in with work email and password and is taken to their personal dashboard; a wrong password shows a generic error; a deactivated account is told it is inactive.
- End session on sign-out or inactivity: a signed-in user can sign out, ending the session so further requests need a new sign-in; a session is also rejected once idle beyond the configured expiry period or once the account has been deactivated.

**Related:** REQ-NFR-001, REQ-NFR-002, REQ-NFR-003

### REQ-FEAT-USERROLES · approved · source: requirements:feature:Users & roles

Covers how accounts are created, how roles combine, and how departed staff are deactivated rather than deleted.

- Create user accounts: an HR Admin or System Admin creates an account for a new joiner with a unique work email and initial details; an initial password must be set at first login; no public self-registration exists; a duplicate email is rejected.
- Assign multiple roles: a System Admin assigns one or more of the five roles to a user, and permissions combine across all assigned roles; removing one role takes away only the permissions unique to it.
- Deactivate a user: an HR Admin or System Admin deactivates a user who has left so they can no longer sign in; the record is marked inactive and kept for historical reference rather than deleted.

**Related:** REQ-NFR-004, REQ-NFR-006

### REQ-FEAT-PROFILES · approved · source: requirements:feature:Profiles & departments

Covers employees managing their own profile and HR Admin maintaining employee and department records.

- View and update own profile: an employee views their own profile, including department and reporting manager, and updates permitted fields such as contact details; restricted fields like department and reporting manager are read-only.
- Manage employee records: an HR Admin creates and maintains employee records including department and reporting manager, which drives approvals and team views; assigning a non-existent or inactive manager is rejected with a clear message.
- Manage department records: an HR Admin adds and renames departments; a department still holding employees cannot be deleted until they are reassigned.

**Related:** REQ-NFR-004

### REQ-FEAT-PROJECTS · approved · source: requirements:feature:Projects & timesheets

Covers project creation/assignment by Project Managers and timesheet entry, submission and status tracking by employees.

- Create and manage projects: a Project Manager creates and maintains projects with a name and status; setting a project to inactive/closed stops it being selectable for new timesheet entries.
- Assign employees to projects: a Project Manager assigns employees to their own project with allocated hours, letting those employees pick the project on their timesheet; managing a project they do not own is denied.
- Log daily and weekly hours: an employee records hours per day/week against assigned projects only; negative hours or more than 24 hours in a day are rejected with a clear message.
- Submit a timesheet: an employee submits a draft timesheet for a period, setting status to Submitted and routing it to their reporting manager; it cannot be edited again until approved or rejected.
- Track timesheet status: an employee sees each submitted timesheet's status (pending/approved/rejected) including the reviewer's comment where rejected; a rejected timesheet can be edited and resubmitted.

**Related:** REQ-NFR-004

### REQ-FEAT-LEAVE · approved · source: requirements:feature:Leave & holidays

Covers configurable leave policy, per-employee balances, leave application/history, and the organisation holiday calendar.

- Configure leave types and carry-over: an HR Admin defines leave types with entitlement and carry-over rules as data so policy changes need no code change; at annual rollover, unused balance carries over only up to the configured limit.
- Maintain per-employee leave balances: an HR Admin sets/adjusts each employee's balance per leave type; adjustments are recorded in the audit log.
- Apply for leave: an employee applies for leave of a chosen type and date range, creating a Pending request routed to their reporting manager; requests exceeding available balance or overlapping an existing request are rejected with a clear message.
- View leave balances: an employee sees remaining balance per leave type; an approved leave's deduction is reflected afterwards.
- View leave history and status: an employee views past and pending leave requests with dates, type, status and any approver comment.
- Maintain the holiday calendar: an HR Admin adds, edits and removes public holidays by date and name on a single organisation calendar for the operating country.
- View the holiday calendar: an employee views the holiday calendar's dates and names to plan work and leave.

**Related:** REQ-NFR-012

### REQ-FEAT-APPROVALS · approved · source: requirements:feature:Approvals & notifications

Covers manager and HR approval of timesheets/leave, and email plus in-app notifications of submissions and decisions.

- Review team timesheets: a Reporting Manager approves/rejects direct reports' submitted timesheets, with a comment on rejection, and the employee is notified; acting on a non-direct-report's timesheet is denied.
- Review team leave requests: a Reporting Manager approves/rejects direct reports' pending leave requests with a comment; approval deducts the balance, rejection deducts nothing, employee notified either way.
- HR override approval: an HR Admin can approve/reject a pending timesheet or leave request when the reporting manager is unavailable; recorded in the audit log as an HR override.
- Notify managers of submissions: when a direct report submits a timesheet or leave request, the reporting manager gets an in-app notification and an email about the pending item.
- Notify employees of decisions: when a request is approved or rejected, the employee gets an in-app notification and an email showing the outcome and any comment.

**Related:** REQ-NFR-005, REQ-NFR-009, REQ-NFR-010

### REQ-FEAT-DASHBOARD · approved · source: requirements:feature:Dashboard & audit

Covers each user's personal dashboard and the System Admin's audit log.

- View personal dashboard: a signed-in user opens a dashboard summarising their recent timesheet status and current leave balances, with pending/rejected items highlighted; it shows only their own data.
- Record actions in audit log: approvals, rejections, record modifications and admin actions write an audit entry capturing actor, action, affected record and timestamp.
- View and filter audit log: a System Admin opens the audit log and filters by user or date range; anyone else is denied access.

**Related:** REQ-NFR-004, REQ-NFR-005

### REQ-FEAT-DOCS · approved · source: requirements:feature:Documentation

Covers the basic product documentation to be delivered with the build.

- Provide product documentation: basic documentation covers login, user provisioning, leave and holiday configuration, timesheet and leave flows, and approvals, so administrators can set up the portal and help users. Every credential shown in setup docs must be a bracketed placeholder with no real value.

### REQ-NFR-001 · approved · source: requirements:NFR-001

[security] Passwords stored only as salted hashes.

User passwords are stored only as salted hashes; the plain-text password is never written to the database or any log, so no readable password value appears anywhere even if the database is exposed.

**Related:** REQ-FEAT-SIGNIN

### REQ-NFR-002 · approved · source: requirements:NFR-002

[security] Sessions expire and end on sign-out or deactivation.

A session ends on sign-out, after the configured idle period, or when an admin deactivates the account; any further protected request requires a fresh sign-in and an abandoned/deactivated session cannot be reused.

**Related:** REQ-FEAT-SIGNIN

### REQ-NFR-003 · approved · source: requirements:NFR-003

[security] Sign-in error does not reveal whether an email exists.

An incorrect sign-in attempt shows a generic error that does not reveal whether the submitted email belongs to an existing account.

**Related:** REQ-FEAT-SIGNIN

### REQ-NFR-004 · approved · source: requirements:NFR-004

[privacy] Each user sees and acts on only their permitted data.

RBAC restricts every user to the data their roles permit: employees reach only their own profile/timesheets/leave/dashboard; reporting managers act only on direct reports; project managers act only on their own projects; HR Admin manages HR data but not security or role settings. Out-of-scope access is denied.

**Related:** REQ-FEAT-PROFILES, REQ-FEAT-PROJECTS, REQ-FEAT-LEAVE, REQ-FEAT-DASHBOARD

### REQ-NFR-005 · approved · source: requirements:NFR-005

[compliance] Audit entries cannot be altered once written.

Approvals, rejections, record changes and admin actions are recorded in an audit log capturing actor, action, affected record and timestamp; once written, an entry cannot be edited or deleted.

**Related:** REQ-FEAT-APPROVALS, REQ-FEAT-DASHBOARD

### REQ-NFR-006 · approved · source: requirements:NFR-006

[compliance] Departed users retained rather than deleted.

A deactivated user record is clearly marked inactive and kept for historical records rather than deleted, so the organisation retains an accurate history.

**Related:** REQ-FEAT-USERROLES

### REQ-NFR-007 · approved · source: requirements:NFR-007

[scalability] Supports the whole organisation's workforce.

The portal supports a single internal organisation of roughly 200-1000 employees logging in and using timesheets, leave and approvals, without being built for multi-tenant or global scale. Target: 200-1000 employees.

### REQ-NFR-008 · approved · source: requirements:NFR-008

[performance] Responsive during the morning login peak.

The portal stays responsive on role/permission checks and in-app notification lookups even when much of the organisation signs in at the start of the day.

### REQ-NFR-009 · approved · source: requirements:NFR-009

[performance] Actions complete without waiting for emails.

A submission or an approval/rejection decision completes and returns to the user immediately, while notification emails are sent in the background, so the user never waits on email delivery.

**Related:** REQ-FEAT-APPROVALS

### REQ-NFR-010 · approved · source: requirements:NFR-010

[availability] In-app notifications survive email failure.

If the email provider credential is not configured or email delivery fails, the in-app notification is still delivered and the email failure is logged, so users are not left uninformed.

**Related:** REQ-FEAT-APPROVALS

### REQ-NFR-011 · approved · source: requirements:NFR-011

[compatibility] Responsive on laptop and phone.

The portal uses one responsive layout that works on a manager's laptop and an employee's phone through a standard web browser.

### REQ-NFR-012 · approved · source: requirements:NFR-012

[maintainability] Leave and holiday policy configurable as data.

Leave types, entitlements, carry-over rules, per-employee balances and the holiday calendar are configured as data by the HR Admin rather than hardcoded to any country's statutory rules, so policy changes need no code changes.

**Related:** REQ-FEAT-LEAVE

### REQ-NFR-013 · approved · source: requirements:NFR-013

[compliance] (accepted risk) No specific data-protection regime targeted.

The portal applies role-restricted access and audit logging as reasonable data-protection practices, but no specific regional regime (such as GDPR) has been named for the operating country, so compliance with any named regulatory regime is not a target of this build. This is an accepted risk per the requirements input, not a confirmed compliance posture -- a human should confirm whether a specific regime applies.
<!-- sdlc:auto:end narrative -->

<!-- sdlc:auto:start summary -->
**Requirements version:** v1  
**Delivery scope:** lightweight  
**Approved:** 2026-11-18

**Capabilities in scope:** Secure employee login, Own employee profile view and update, Daily and weekly timesheet entry against projects, Timesheet submission and status tracking, Leave application against leave balances, Leave balance and history view, Holiday calendar view, Personal dashboard of own timesheets and leave, Project and department records, Leave type and per-employee balance records, Basic product documentation, Leave types and carry-over as configurable data, not statutory rules, Leave balances tracked per employee per leave type

**Approved technology stack:**

| Layer | Choice | Rationale |
|---|---|---|
| backend | FastAPI | The product's heart is rules: who may see whose data, single-level approvals, leave accrual and carry-over as configurable policy, and an audit entry for every admin action. FastAPI is a clean fit for writing these rules as a well-documented API that the React screens call, and its automatic API docs help whoever maintains the system after launch. Scale (200–1000 employees, internal use) is modest and well within its reach. |
| cloud | AWS | A single-organisation internal portal for up to ~1000 staff needs reliable, private hosting for the app, the PostgreSQL database, and stored documents/exports — not global scale. AWS covers all of it (managed PostgreSQL via RDS, file storage via S3, standard networking to keep it internal) with no hard deadline forcing shortcuts, and its managed database service reduces the day-to-day burden of backups and patching on sensitive employee data. |
| database | PostgreSQL | All of this product's data is highly relational — employees belong to departments, report to managers, log hours against projects, draw down leave balances per type, and every action leaves an audit trail. PostgreSQL enforces these relationships and keeps balances and approvals consistent, which matters because this system is the single source of truth with no payroll to reconcile against. It handles this organisation's size comfortably with room to spare. |
| frontend | React | This is an internal, responsive portal where five roles each see a different slice of the same data — an employee's own timesheet versus a manager's team view versus HR's org-wide dashboards with CSV/PDF export. React handles these role-driven, interactive screens (approval queues, utilisation charts, balance trackers) well and lets you build one responsive layout that works on a manager's laptop and an employee's phone. |
<!-- sdlc:auto:end summary -->

<!-- sdlc:auto:start epics -->
## EPIC-001: Secure Login & Session Security

Users authenticate directly against the HRMS, which is the source of truth for its own accounts (no SSO or external directory). Assumption (technical stack): the product is a responsive web application backed by a PostgreSQL relational database, using session/JWT-based authentication with credentials stored only as salted hashes. Sign-in and session security are expressed as checkable outcomes (sessions expire, sign-out and deactivation end sessions, passwords are never stored in plain text); the specific token or storage mechanism is left to implementation and no browser-cookie behaviour is prescribed, because the web app and API are served from different web addresses.

### US-001: Sign in with credentials

**Priority:** critical

> As a registered user, I want to sign in with my work email and password, so that I can access the features permitted for my roles.

| ID | Given | When | Then |
|---|---|---|---|
| AC-001 | I am a user with an active account | I submit my correct email and password | I am signed in and taken to my personal dashboard |
| AC-002 | I am on the sign-in page | I submit an incorrect password | I am not signed in and I see a generic error that does not reveal whether the email exists |
| AC-003 | my account has been deactivated by an admin | I submit my correct email and password | I am not signed in and I am told my account is inactive |

### US-002: Passwords stored securely

**Priority:** critical

> As a security-conscious organisation, I want user passwords to be stored only as hashes, so that credentials cannot be read even if the database is exposed.

| ID | Given | When | Then |
|---|---|---|---|
| AC-004 | a user sets or changes their password | the password is persisted | only a salted hash is stored and the plain-text password is never written to the database or logs |
| AC-005 | a stored user record | an administrator or operator inspects it | no readable password value is present in any field or log |

### US-003: Session expiry and sign-out

**Priority:** high

> As a signed-in user, I want my session to end when I sign out or after a period of inactivity, so that an unattended or abandoned session cannot be reused.

| ID | Given | When | Then |
|---|---|---|---|
| AC-006 | I am signed in | I choose to sign out | my session is ended and any further request requires signing in again |
| AC-007 | I am signed in and leave the session idle beyond the configured expiry period | I next attempt a protected action | the session is rejected and I am prompted to sign in again |
| AC-008 | an admin deactivates my account while I am signed in | I next make a protected request | my session is no longer valid and I am signed out |

## EPIC-002: User Provisioning & Role-Based Access Control

Accounts are created by HR Admin / System Admin; there is no public self-registration. The System Admin assigns one or more of the five roles (Employee, Reporting Manager, HR Admin, Project Manager, System Admin) per user, and permissions combine across all assigned roles. RBAC enforces that employees see only their own data, reporting managers act only on their direct reports, and project managers act only on their own projects; HR Admin manages HR data but not security settings. Assumption (data privacy): access is restricted to permitted roles with reasonable data-protection practices; no specific regional regime (e.g. GDPR) has been named for the operating country.

### US-004: Create user accounts without self-registration

**Priority:** critical

> As a HR Admin or System Admin, I want to create a user account for a new joiner, so that staff can access the portal without any public sign-up.

| ID | Given | When | Then |
|---|---|---|---|
| AC-009 | I am an HR Admin or System Admin | I create a user with a unique work email and initial details | the account is created and an initial password is required to be set at first login, shown as a placeholder such as <set-at-first-login> |
| AC-010 | a person without an account | they visit the portal | no public self-registration option is available |
| AC-011 | I try to create a user | I enter an email that already belongs to another account | the account is not created and I am told the email is already in use |

### US-005: Assign multiple roles with combined permissions

**Priority:** critical

> As a System Admin, I want to assign one or more roles to a user, so that a person who is, for example, both an employee and a reporting manager gets the combined permissions.

| ID | Given | When | Then |
|---|---|---|---|
| AC-012 | I am a System Admin editing a user | I assign the Employee and Reporting Manager roles to that user | the user can access all Employee features plus all Reporting Manager features |
| AC-013 | a user holds multiple roles | I remove one role | the user immediately loses only the permissions unique to the removed role and retains those from remaining roles |

### US-006: Enforce role-scoped data access

**Priority:** critical

> As a organisation, I want each user to see and act on only the data their roles permit, so that personal and project data is not exposed to unauthorised users.

| ID | Given | When | Then |
|---|---|---|---|
| AC-014 | I hold only the Employee role | I attempt to open another employee's profile or timesheet | access is denied |
| AC-015 | I am a Reporting Manager | I attempt to approve a request for an employee who is not my direct report | access is denied |
| AC-016 | I am a Project Manager | I attempt to review timesheets for a project I do not manage | access is denied |
| AC-017 | I am an HR Admin | I attempt to change system security or role/permission settings | access is denied because those belong to the System Admin |

### US-007: Deactivate a user

**Priority:** high

> As a HR Admin or System Admin, I want to deactivate a user who has left, so that they can no longer sign in and their active sessions end.

| ID | Given | When | Then |
|---|---|---|---|
| AC-018 | an active user | I deactivate their account | they can no longer sign in and any existing session becomes invalid on its next request |
| AC-019 | a deactivated user record | I view it | it is clearly marked inactive and retained for historical records rather than deleted |

## EPIC-003: Employee Profile & Department Records

Employees can view and update their own profile within permitted fields; HR Admin manages employee records, department records and reporting-manager relationships. Departments and reporting lines are the basis for manager scoping used elsewhere in the portal.

### US-008: View and update own profile

**Priority:** high

> As a employee, I want to view my profile and update my permitted details, so that my personal information stays current.

| ID | Given | When | Then |
|---|---|---|---|
| AC-020 | I am signed in as an employee | I open my profile | I see my details including my department and reporting manager |
| AC-021 | I am editing my profile | I change a field I am permitted to edit (such as contact details) and save | the change is stored and shown on my profile |
| AC-022 | I am editing my profile | I attempt to change a restricted field such as my department or reporting manager | that field is read-only and the change is not accepted |

### US-009: Manage employee records

**Priority:** high

> As a HR Admin, I want to create and maintain employee records including department and reporting manager, so that the organisation structure is accurate.

| ID | Given | When | Then |
|---|---|---|---|
| AC-023 | I am an HR Admin | I create or edit an employee record and set their department and reporting manager | the record is saved and the reporting-manager relationship takes effect for approvals and team views |
| AC-024 | I am an HR Admin | I assign a reporting manager who does not exist or is inactive | the assignment is rejected with a clear message |

### US-010: Manage department records

**Priority:** medium

> As a HR Admin, I want to maintain the list of departments, so that employees can be organised and reported on by department.

| ID | Given | When | Then |
|---|---|---|---|
| AC-025 | I am an HR Admin | I add or rename a department | it becomes available for assigning to employees |
| AC-026 | a department has employees assigned | I attempt to delete it | deletion is prevented and I am asked to reassign those employees first |

## EPIC-004: Project Records & Assignments

Project Managers create and manage projects and assign employees to them, including allocated hours; timesheets are logged against these projects. Project Managers act only on their own projects.

### US-011: Create and manage projects

**Priority:** high

> As a Project Manager, I want to create and maintain projects, so that employees can log time against them.

| ID | Given | When | Then |
|---|---|---|---|
| AC-027 | I am a Project Manager | I create a project with a name and status | the project is saved and available for assignment |
| AC-028 | I am a Project Manager | I set a project to inactive/closed | it can no longer be selected for new timesheet entries |

### US-012: Assign employees to projects with allocated hours

**Priority:** high

> As a Project Manager, I want to assign employees to my project and record allocated hours, so that logged time can later be compared against the allocation.

| ID | Given | When | Then |
|---|---|---|---|
| AC-029 | I am a Project Manager of a project | I assign an employee and set their allocated hours | the employee can select that project on their timesheet |
| AC-030 | I am a Project Manager | I attempt to manage a project I do not own | access is denied |

## EPIC-005: Timesheet Entry, Submission & Status Tracking

Employees log working hours daily or weekly against projects they are assigned to, submit timesheets, and track their approval status. Status progresses through draft, submitted, approved or rejected.

### US-013: Log daily and weekly hours against projects

**Priority:** critical

> As a employee, I want to record hours per day and per week against my assigned projects, so that my worked time is captured accurately.

| ID | Given | When | Then |
|---|---|---|---|
| AC-031 | I am assigned to one or more projects | I enter hours for a date against a project | the entry is saved against that project and date |
| AC-032 | I am entering timesheet hours | I select a project I am not assigned to | the project is not available for selection |
| AC-033 | I enter an invalid value such as negative hours or more than 24 hours in a day | I try to save | the entry is rejected with a clear validation message |

### US-014: Submit a timesheet

**Priority:** critical

> As a employee, I want to submit my timesheet for a period, so that it goes to my reporting manager for approval.

| ID | Given | When | Then |
|---|---|---|---|
| AC-034 | I have a draft timesheet for a period | I submit it | its status becomes Submitted and it is routed to my reporting manager and can no longer be edited by me |
| AC-035 | a timesheet has already been submitted | I try to edit it | editing is blocked until it is approved or rejected |

### US-015: Track timesheet status

**Priority:** high

> As a employee, I want to see the current status of my submitted timesheets, so that I know whether they are pending, approved or rejected.

| ID | Given | When | Then |
|---|---|---|---|
| AC-036 | I have submitted timesheets | I view my timesheet list | each shows its current status and, where rejected, the reviewer's comment |
| AC-037 | my timesheet was rejected | I open it | I can edit and resubmit it |

## EPIC-006: Leave Policy & Balance Configuration

Assumption (leave policy): leave types, entitlements, accrual and annual carry-over are configured as data by the HR Admin rather than hardcoded to any country's statutory rules. Balances are tracked per employee per leave type. The workforce is in a single country, so one set of leave rules applies.

### US-016: Configure leave types and carry-over as data

**Priority:** high

> As a HR Admin, I want to define leave types and their entitlement and carry-over rules, so that leave rules reflect our policy without code changes.

| ID | Given | When | Then |
|---|---|---|---|
| AC-038 | I am an HR Admin | I create a leave type with an entitlement and a carry-over rule | it is saved and available for employees to apply against |
| AC-039 | a leave type is configured with a carry-over limit | an annual period rolls over | unused balance is carried over only up to the configured limit |

### US-017: Maintain per-employee leave balances

**Priority:** high

> As a HR Admin, I want to set and adjust each employee's balance per leave type, so that balances reflect their actual entitlement.

| ID | Given | When | Then |
|---|---|---|---|
| AC-040 | I am an HR Admin | I set an employee's balance for a leave type | that balance is stored for that employee and leave type |
| AC-041 | I am an HR Admin | I adjust a balance | the change is saved and recorded in the audit log |

## EPIC-007: Leave Application, Balances & History

Employees apply for leave against their available balances, view their balances per leave type, and see their leave history and request status. Applications are routed to the reporting manager for approval.

### US-018: Apply for leave against balance

**Priority:** critical

> As a employee, I want to apply for leave of a chosen type and date range, so that my time off is recorded and approved.

| ID | Given | When | Then |
|---|---|---|---|
| AC-042 | I have sufficient balance for a leave type | I submit a leave application for a date range within that balance | the application is created with status Pending and routed to my reporting manager |
| AC-043 | I apply for more days than my available balance for that leave type | I submit | the application is rejected with a clear message about insufficient balance |
| AC-044 | I apply for a date range that overlaps an existing leave request | I submit | the application is rejected with a message about the overlap |

### US-019: View leave balances

**Priority:** high

> As a employee, I want to see my remaining balance for each leave type, so that I know how much leave I can still take.

| ID | Given | When | Then |
|---|---|---|---|
| AC-045 | I am an employee | I open my leave balances | I see my remaining balance for each leave type available to me |
| AC-046 | an approved leave reduces my balance | I view my balances afterwards | the remaining balance reflects the deduction |

### US-020: View leave history and status

**Priority:** medium

> As a employee, I want to see my past and pending leave requests with their status, so that I can track what has been approved, rejected or is pending.

| ID | Given | When | Then |
|---|---|---|---|
| AC-047 | I have submitted leave requests | I open my leave history | I see each request with its dates, type, status and any approver comment |

## EPIC-008: Holiday Calendar

HR Admin maintains a single organisation holiday calendar for the operating country; employees can view it. Holidays are configured as data, not hardcoded to statutory rules.

### US-021: Maintain the holiday calendar

**Priority:** medium

> As a HR Admin, I want to add and edit public holidays for the year, so that employees see the correct non-working days.

| ID | Given | When | Then |
|---|---|---|---|
| AC-048 | I am an HR Admin | I add a holiday with a date and name | it appears on the organisation holiday calendar |
| AC-049 | I am an HR Admin | I remove or edit a holiday | the calendar updates accordingly |

### US-022: View holidays

**Priority:** medium

> As a employee, I want to view the holiday calendar, so that I can plan my work and leave around non-working days.

| ID | Given | When | Then |
|---|---|---|---|
| AC-050 | the HR Admin has configured holidays | I open the holiday calendar | I see the list of holidays with their dates |

## EPIC-009: Approval Workflows

Assumption (approval workflow): timesheet and leave approvals are single-level. The employee's reporting manager approves or rejects with a comment; the HR Admin can act as an override/fallback approver. There is no multi-stage escalation chain in this build. Approvals and rejections trigger notifications and are written to the audit log.

### US-023: Review and decide team timesheets

**Priority:** critical

> As a Reporting Manager, I want to approve or reject my direct reports' submitted timesheets with a comment, so that worked hours are validated.

| ID | Given | When | Then |
|---|---|---|---|
| AC-051 | a direct report has submitted a timesheet | I approve it | its status becomes Approved and the employee is notified |
| AC-052 | a direct report's timesheet | I reject it with a comment | its status becomes Rejected, the comment is stored, and the employee is notified |
| AC-053 | a timesheet belongs to someone who is not my direct report | I try to act on it | access is denied |

### US-024: Review and decide team leave requests

**Priority:** critical

> As a Reporting Manager, I want to approve or reject my direct reports' leave requests with a comment, so that time off is authorised and balances stay correct.

| ID | Given | When | Then |
|---|---|---|---|
| AC-054 | a direct report has a pending leave request | I approve it | its status becomes Approved, the corresponding balance is deducted, and the employee is notified |
| AC-055 | a pending leave request | I reject it with a comment | its status becomes Rejected, no balance is deducted, and the employee is notified |

### US-025: HR Admin override approval

**Priority:** medium

> As a HR Admin, I want to approve or reject a request when the reporting manager is unavailable, so that requests are not blocked indefinitely.

| ID | Given | When | Then |
|---|---|---|---|
| AC-056 | a pending timesheet or leave request | I act on it as an HR Admin override | the decision is applied and recorded in the audit log as an HR override |

## EPIC-010: Notifications

Assumption (notifications): request, approval and rejection events are delivered both by email and as in-app notifications. Email requires an email-provider credential, stored as a placeholder such as <email-provider-api-key> and never a real value.

### US-026: Notify on request submission

**Priority:** high

> As a Reporting Manager, I want to be notified when a direct report submits a timesheet or leave request, so that I can act on it promptly.

| ID | Given | When | Then |
|---|---|---|---|
| AC-057 | a direct report submits a timesheet or leave request | the submission is saved | I receive an in-app notification and an email about the pending item |

### US-027: Notify on approval decision

**Priority:** high

> As a employee, I want to be notified when my request is approved or rejected, so that I know the outcome without checking manually.

| ID | Given | When | Then |
|---|---|---|---|
| AC-058 | my timesheet or leave request is approved or rejected | the decision is saved | I receive an in-app notification and an email showing the outcome and any comment |
| AC-059 | the email provider credential is not configured | a notification is triggered | the in-app notification is still delivered and the email failure is logged |

## EPIC-011: Personal Dashboard

Each signed-in user gets a personal dashboard summarising their own timesheets and leave, scoped strictly to their own data. Assumption (reporting): broader reporting dashboards and CSV/PDF export for managers, project managers and HR Admin (team availability, project utilisation, org-wide HR reports) are deferred beyond this Lightweight MVP and are not included in this version.

### US-028: View personal dashboard

**Priority:** medium

> As a employee, I want a dashboard summarising my timesheets and leave, so that I can see my status at a glance when I sign in.

| ID | Given | When | Then |
|---|---|---|---|
| AC-060 | I am signed in | I open my dashboard | I see a summary of my recent timesheet status and my current leave balances |
| AC-061 | I have pending or rejected items | I view my dashboard | those items are highlighted so I can follow up |
| AC-062 | I am viewing my dashboard | the data loads | it shows only my own data and no other employee's data |

## EPIC-012: Audit Logging

All approvals, rejections, modifications and administrative actions are recorded in an audit log for accountability and reasonable data-protection practices. Audit logs are viewable by the System Admin.

### US-029: Record key actions in the audit log

**Priority:** high

> As a organisation, I want approvals, rejections, record changes and admin actions written to an audit log, so that we have an accountable history of who did what.

| ID | Given | When | Then |
|---|---|---|---|
| AC-063 | a user approves, rejects, modifies a record, or performs an admin action | the action completes | an audit entry is written capturing the actor, action, affected record and timestamp |
| AC-064 | an audit entry has been written | anyone attempts to edit or delete it | the entry cannot be altered |

### US-030: View audit logs

**Priority:** medium

> As a System Admin, I want to view and filter the audit log, so that I can investigate changes and access.

| ID | Given | When | Then |
|---|---|---|---|
| AC-065 | I am a System Admin | I open the audit log and filter by user or date range | I see the matching entries |
| AC-066 | I am not a System Admin | I attempt to open the audit log | access is denied |

## EPIC-013: Product Documentation

Basic product documentation is provided so administrators can set up the portal and users understand the core flows. Setup documentation references secrets only as placeholders such as <email-provider-api-key> and <database-password>, never real values. Out of scope for this version: payroll/HR system export or sync, and biometric/badge attendance-device integration.

### US-031: Provide basic product documentation

**Priority:** medium

> As a administrator, I want basic documentation covering setup and core user flows, so that I can configure the portal and help users get started.

| ID | Given | When | Then |
|---|---|---|---|
| AC-067 | the product is delivered | I open the documentation | it covers login, user provisioning, leave/holiday configuration, timesheet and leave flows, and approvals |
| AC-068 | the setup documentation references credentials | I read it | every secret is shown as a bracketed placeholder such as <email-provider-api-key> with no real value |
<!-- sdlc:auto:end epics -->
