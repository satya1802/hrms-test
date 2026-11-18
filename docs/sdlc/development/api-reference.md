# API Reference

> Maintained by QuorQ AI SDLC. Text between `sdlc:auto` markers is regenerated; anything outside them is yours and is kept.

<!-- sdlc:auto:start endpoints -->
| Method | Path | Handler | Source | Summary |
|---|---|---|---|---|
| GET | /health | health | `backend/app/main.py:58` | Liveness probe, and the only route here that is not a stub. |
<!-- sdlc:auto:end endpoints -->

<!-- sdlc:auto:start drift -->
**Designed but missing:**

- GET /audit-logs
- GET /holidays
- GET /me/dashboard
- GET /me/leave-balances
- GET /me/leave-requests
- GET /me/notifications
- GET /me/profile
- GET /timesheets
- PATCH /me/profile
- PATCH /users/{id}/roles
- POST /auth/login
- POST /auth/logout
- POST /auth/set-password
- POST /departments
- POST /employees
- POST /holidays
- POST /leave-requests
- POST /leave-requests/{id}/decision
- POST /leave-types
- POST /projects
- POST /projects/{id}/assignments
- POST /timesheets
- POST /timesheets/{id}/decision
- POST /timesheets/{id}/submit
- POST /users
- POST /users/{id}/deactivate
- PUT /employees/{id}/leave-balances
<!-- sdlc:auto:end drift -->

<!-- sdlc:auto:start source -->
Generated from commit `049f7f8`
<!-- sdlc:auto:end source -->
