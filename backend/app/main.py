"""Application entrypoint.

Generated from the approved architecture: one router per component that owns
endpoints, one route per endpoint the API spec declares. Every generated route
is a stub that returns a typed placeholder, so the service starts, serves its
OpenAPI document and passes its tests before a single handler is implemented.
"""

import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models  # noqa: F401 -- imported so the tables register before create_all
from app.database import Base, engine
from app.services import configured_services


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """The scaffold ships no migrations, so the tables are created from the models
    when the application starts. Replace this with Alembic before anything holds data
    worth keeping.

    This runs on startup and not at import, so importing the application never opens a
    connection. A test can therefore point `get_db` at a database of its own, and a
    deployment whose `DATABASE_URL` names a server that is not up fails where you can
    read the error, not while pytest collects the files.
    """
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="HRMS_test",
    description="Develop a modern, responsive HRMS portal with secure login and role-based access for Employees, Managers, HR, and Admins. Employee Management: Manage employee profiles, departments, reporting managers, and project assignments. Timesheet Management: Allow employees to log daily/weekly working hours, select projects, submit timesheets, and track approval status. Leave Management: Enable employees to apply for leave, check leave balances, view leave history, and track requests. Approval Workflows: Allow managers to approve/reject timesheets and leave requests with comments and notifications. ## HRMS Portal \u2013 User Roles and Permissions | Role | Permissions | | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | | Employee | View/update own profile, submit daily/weekly timesheets, apply for leave, check leave balances, view holidays, and track approval status. | | Reporting Manager | All employee permissions, view team members, approve/reject team timesheets and leave requests, monitor team availability, and access team reports. | | HR Admin | Manage employee records, departments, leave policies, leave balances, holiday calendars, attendance records, and organization-wide HR reports. | | Project Manager | Create/manage projects, assign employees to projects, review project-specific timesheets, and monitor project utilization and allocated hours. | | System Admin | Manage users, roles, permissions, organization settings, system configurations, and audit logs with full administrative access. | ### Role-Based Access Control (RBAC) Requirements 1. Users must log in securely and access only features permitted for their roles. 2. Employees can view and modify only their own timesheets, leave requests, and permitted profile details. 3. Reporting Managers can approve or reject requests only for employees assigned to them. 4. Project Managers can access timesheets",
    version="0.1.0",
    lifespan=lifespan,
)

# The SPA runs on a different origin than the API, so the browser refuses its calls
# unless that origin is allowed here. In development that is the Vite dev server; when
# deployed, the platform injects the frontend's real URL as ALLOWED_ORIGINS (comma
# separated). Point ALLOWED_ORIGINS at the real thing and nothing else has to change.
_dev_origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
_allowed_origins = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins or _dev_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health() -> dict[str, object]:
    """Liveness probe, and the only route here that is not a stub."""
    return {"status": "ok", "services": configured_services()}
