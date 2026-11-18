# HRMS_test — SDLC Documentation

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start overview -->
Develop a modern, responsive HRMS portal with secure login and role-based access for Employees, Managers, HR, and Admins. Employee Management: Manage employee profiles, departments, reporting managers, and project assignments. Timesheet Management: Allow employees to log daily/weekly working hours, select projects, submit timesheets, and track approval status. Leave Management: Enable employees to apply for leave, check leave balances, view leave history, and track requests. Approval Workflows: Allow managers to approve/reject timesheets and leave requests with comments and notifications. ## HRMS Portal – User Roles and Permissions | Role | Permissions | | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | | Employee | View/update own profile, submit daily/weekly timesheets, apply for leave, check leave balances, view holidays, and track approval status. | | Reporting Manager | All employee permissions, view team members, approve/reject team timesheets and leave requests, monitor team availability, and access team reports. | | HR Admin | Manage employee records, departments, leave policies, leave balances, holiday calendars, attendance records, and organization-wide HR reports. | | Project Manager | Create/manage projects, assign employees to projects, review project-specific timesheets, and monitor project utilization and allocated hours. | | System Admin | Manage users, roles, permissions, organization settings, system configurations, and audit logs with full administrative access. | ### Role-Based Access Control (RBAC) Requirements 1. Users must log in securely and access only features permitted for their roles. 2. Employees can view and modify only their own timesheets, leave requests, and permitted profile details. 3. Reporting Managers can approve or reject requests only for employees assigned to them. 4. Project Managers can access timesheets

**Documentation version:** v1
<!-- sdlc:auto:end overview -->

## Contents

<!-- sdlc:auto:start contents -->
| Document | State |
|---|---|
| [Requirements](requirements/README.md) | v1 approved |
| [Architecture](architecture/README.md) | 0 entries |
| [Planning](planning/README.md) | 13 entries |
| [Development](development/README.md) | 0 entries |
| [Testing](testing/README.md) | 0 entries |
| [Deployment](deployment/README.md) | 0 entries |
| [Maintenance](maintenance/README.md) | 0 entries |
| [Data model](architecture/data-model.md) | not generated yet |
| [API (OpenAPI)](architecture/api/openapi.yaml) | not generated yet |
| [Decisions (ADRs)](architecture/adr/README.md) | 0 decisions |
| [Sprint plan](development/sprint-plan.md) | not generated yet |
| [Developer guide](development/developer-guide.md) | not generated yet |
| [API reference](development/api-reference.md) | 0 routes |
| [Test report](testing/test-report.md) | not run yet |
| [Tests](testing/test-cases.md) | 0 tests |
| [Deployment guide](deployment/deployment-guide.md) | not deployed yet |
| [Runbook](deployment/runbook.md) | not deployed yet |
| [Release notes](deployment/release-notes.md) | 0 releases |
| [Traceability matrix](traceability-matrix.md) | 31 requirements |
| [Changelog](CHANGELOG.md) | 1 version |
<!-- sdlc:auto:end contents -->
