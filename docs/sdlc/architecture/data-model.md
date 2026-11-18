# Data Model

<!-- sdlc:auto:start entities -->
### users

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| email | varchar | False | — | False |
| password_hash | varchar | False | — | False |
| is_active | boolean | False | — | False |
| must_set_password | boolean | False | — | False |
| created_at | timestamptz | False | — | False |
| deactivated_at | timestamptz | False | — | True |

### roles

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | smallint | True | — | False |
| name | varchar | False | — | False |

### user_roles

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| user_id | uuid | True | users.id | False |
| role_id | smallint | True | roles.id | False |

### departments

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| name | varchar | False | — | False |

### employees

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| user_id | uuid | False | users.id | False |
| full_name | varchar | False | — | False |
| contact_phone | varchar | False | — | True |
| department_id | uuid | False | departments.id | True |
| reporting_manager_id | uuid | False | employees.id | True |
| profile_document_key | varchar | False | — | True |

### projects

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| name | varchar | False | — | False |
| status | varchar | False | — | False |
| project_manager_id | uuid | False | employees.id | False |

### project_assignments

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| project_id | uuid | False | projects.id | False |
| employee_id | uuid | False | employees.id | False |
| allocated_hours | numeric | False | — | True |

### timesheets

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| employee_id | uuid | False | employees.id | False |
| period_start | date | False | — | False |
| period_end | date | False | — | False |
| status | varchar | False | — | False |
| reviewer_comment | text | False | — | True |
| submitted_at | timestamptz | False | — | True |
| decided_at | timestamptz | False | — | True |

### timesheet_entries

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| timesheet_id | uuid | False | timesheets.id | False |
| project_id | uuid | False | projects.id | False |
| work_date | date | False | — | False |
| hours | numeric | False | — | False |

### leave_types

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| name | varchar | False | — | False |
| annual_entitlement | numeric | False | — | False |
| carry_over_limit | numeric | False | — | False |

### leave_balances

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| employee_id | uuid | False | employees.id | False |
| leave_type_id | uuid | False | leave_types.id | False |
| balance_days | numeric | False | — | False |
| period_year | integer | False | — | False |

### leave_requests

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| employee_id | uuid | False | employees.id | False |
| leave_type_id | uuid | False | leave_types.id | False |
| start_date | date | False | — | False |
| end_date | date | False | — | False |
| days | numeric | False | — | False |
| status | varchar | False | — | False |
| approver_comment | text | False | — | True |
| decided_at | timestamptz | False | — | True |

### holidays

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| holiday_date | date | False | — | False |
| name | varchar | False | — | False |

### notifications

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| recipient_user_id | uuid | False | users.id | False |
| message | text | False | — | False |
| is_read | boolean | False | — | False |
| email_status | varchar | False | — | False |
| created_at | timestamptz | False | — | False |

### audit_logs

| Field | Type | PK | FK | Nullable |
|---|---|---|---|---|
| id | uuid | True | — | False |
| actor_user_id | uuid | False | users.id | False |
| action | varchar | False | — | False |
| entity_type | varchar | False | — | False |
| entity_id | varchar | False | — | False |
| detail | jsonb | False | — | True |
| created_at | timestamptz | False | — | False |
<!-- sdlc:auto:end entities -->

<!-- sdlc:auto:start relationships -->
| Source | Target | Type |
|---|---|---|
| users | user_roles | one-to-many |
| roles | user_roles | one-to-many |
| users | employees | one-to-one |
| departments | employees | one-to-many |
| employees | employees | one-to-many |
| employees | projects | one-to-many |
| projects | project_assignments | one-to-many |
| employees | project_assignments | one-to-many |
| employees | timesheets | one-to-many |
| timesheets | timesheet_entries | one-to-many |
| projects | timesheet_entries | one-to-many |
| leave_types | leave_balances | one-to-many |
| employees | leave_balances | one-to-many |
| employees | leave_requests | one-to-many |
| leave_types | leave_requests | one-to-many |
| users | notifications | one-to-many |
| users | audit_logs | one-to-many |
<!-- sdlc:auto:end relationships -->

<!-- sdlc:auto:start er-diagram -->
```mermaid
erDiagram
  users {
    uuid id PK
    varchar email
    varchar password_hash
    boolean is_active
    boolean must_set_password
    timestamptz created_at
    timestamptz deactivated_at
  }
  roles {
    smallint id PK
    varchar name
  }
  user_roles {
    uuid user_id PK,FK
    smallint role_id PK,FK
  }
  departments {
    uuid id PK
    varchar name
  }
  employees {
    uuid id PK
    uuid user_id FK
    varchar full_name
    varchar contact_phone
    uuid department_id FK
    uuid reporting_manager_id FK
    varchar profile_document_key
  }
  projects {
    uuid id PK
    varchar name
    varchar status
    uuid project_manager_id FK
  }
  project_assignments {
    uuid id PK
    uuid project_id FK
    uuid employee_id FK
    numeric allocated_hours
  }
  timesheets {
    uuid id PK
    uuid employee_id FK
    date period_start
    date period_end
    varchar status
    text reviewer_comment
    timestamptz submitted_at
    timestamptz decided_at
  }
  timesheet_entries {
    uuid id PK
    uuid timesheet_id FK
    uuid project_id FK
    date work_date
    numeric hours
  }
  leave_types {
    uuid id PK
    varchar name
    numeric annual_entitlement
    numeric carry_over_limit
  }
  leave_balances {
    uuid id PK
    uuid employee_id FK
    uuid leave_type_id FK
    numeric balance_days
    integer period_year
  }
  leave_requests {
    uuid id PK
    uuid employee_id FK
    uuid leave_type_id FK
    date start_date
    date end_date
    numeric days
    varchar status
    text approver_comment
    timestamptz decided_at
  }
  holidays {
    uuid id PK
    date holiday_date
    varchar name
  }
  notifications {
    uuid id PK
    uuid recipient_user_id FK
    text message
    boolean is_read
    varchar email_status
    timestamptz created_at
  }
  audit_logs {
    uuid id PK
    uuid actor_user_id FK
    varchar action
    varchar entity_type
    varchar entity_id
    jsonb detail
    timestamptz created_at
  }
  users ||--o{ user_roles : "one-to-many"
  roles ||--o{ user_roles : "one-to-many"
  users ||--|| employees : "one-to-one"
  departments ||--o{ employees : "one-to-many"
  employees ||--o{ employees : "one-to-many"
  employees ||--o{ projects : "one-to-many"
  projects ||--o{ project_assignments : "one-to-many"
  employees ||--o{ project_assignments : "one-to-many"
  employees ||--o{ timesheets : "one-to-many"
  timesheets ||--o{ timesheet_entries : "one-to-many"
  projects ||--o{ timesheet_entries : "one-to-many"
  leave_types ||--o{ leave_balances : "one-to-many"
  employees ||--o{ leave_balances : "one-to-many"
  employees ||--o{ leave_requests : "one-to-many"
  leave_types ||--o{ leave_requests : "one-to-many"
  users ||--o{ notifications : "one-to-many"
  users ||--o{ audit_logs : "one-to-many"
```
<!-- sdlc:auto:end er-diagram -->
