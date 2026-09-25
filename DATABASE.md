desgining the admin database

| Field | Type | Required | Details |
| ----- | ----- | ----- | ----- |
| `id`  | BIGINT | ✅ | Unique Admin ID |
| `user_id`  | BIGINT | ✅ | Link to Django authentication user |
| `organization_id`  | BIGINT | ✅ | Organization the admin manages |
| `full_name`  | VARCHAR(150) | ✅ | Administrator's full name |
| `email`  | VARCHAR(254) | ✅ | **Valid, unique email address** |
| `password`  | Django-managed hash | ✅ | Password created during registration |
| `phone`  | VARCHAR(20) | ❌ | Optional contact number |
| `profile_photo`  | VARCHAR(255) | ❌ | Optional profile photo |
| `created_at`  | DATETIME | ✅ | Account creation time |
| `updated_at`  | DATETIME | ✅ | Last update time |
| `is_active`  | BOOLEAN | ✅ | Defaults to `TRUE`  |
desging the teachers table databasse design

| Field | Type | Required | Details |
| ----- | ----- | ----- | ----- |
| `id`  | BIGINT | ✅ | Unique teacher ID |
| `organization_id`  | BIGINT | ✅ | Organization the teacher belongs to |
| `full_name`  | VARCHAR(150) | ✅ | Teacher's full name |
| `email`  | VARCHAR(254) | ✅ | Valid teacher email |
| `phone`  | VARCHAR(20) | ❌ | Optional |
| `employee_id`  | VARCHAR(50) | ✅ | Institution's teacher ID |
| `department_id`  | BIGINT | ❌ | Optional department |
| `profile_photo`  | VARCHAR(255) | ❌ | Optional |
| `created_at`  | DATETIME | ✅ | Automatic |
| `updated_at`  | DATETIME | ✅ | Automatic |
| `is_active`  | BOOLEAN | ✅ | Defaults to `TRUE`  |
departments database design

| Field | Required | Details |
| ----- | ----- | ----- |
| `id`  | ✅ | Unique department ID |
| `organization_id`  | ✅ | Owning organization |
| `name`  | ✅ | Department name |
| `code`  | ✅ | Department code |
| `description`  | ❌ | Optional |
| `created_at`  | ✅ | Automatic |
| `updated_at`  | ✅ | Automatic |
| `is_active`  | ✅ | <p>Default `TRUE` </p><p></p> |
academic sessions database

| Field | Type | Required | Purpose |
| ----- | ----- | ----- | ----- |
| `id`  | BIGINT | ✅ | Unique session ID |
| `organization_id`  | BIGINT | ✅ | Organization owning the session |
| `name`  | VARCHAR(20) | ✅ | Display name, e.g. `2026-2027`  |
| `start_date`  | DATE | ✅ | Session start |
| `end_date`  | DATE | ✅ | Session end |
| `is_current`  | BOOLEAN | ✅ | Whether this is the current session |
| `created_at`  | DATETIME | ✅ | Creation time |
| `updated_at`  | DATETIME | ✅ | Last update |


there are firstly 6 core identities should be for our version 1

Organization
 │
 ├── Admin
 │
 ├── Department
 │ └── Academic Year
 │ └── Section
 │ └── Students
 │
 ├── Teachers
 │
 └── Subjects
 │
 └── Attendance

| Column | Type | Purpose |
| ----- | ----- | ----- |
| `id`  | BIGINT | Unique organization ID |
| `name`  | VARCHAR(150) | Organization name |
| `type`  | VARCHAR(50) | School / College / Coaching / Company / Other |
| `email`  | VARCHAR(150) | Official organization email |
| `phone`  | VARCHAR(20) | Contact number |
| `address`  | TEXT | Organization address |
| `logo`  | VARCHAR(255) | Logo file path |
| `created_at`  | DATETIME | Creation timestamp |
| `updated_at`  | DATETIME | Last update timestamp |
| `is_active`  | BOOLEAN | Whether organization is active |
organizations
│
├── id REQUIRED
├── name REQUIRED
├── type REQUIRED
│ ├── SCHOOL
│ ├── COLLEGE
│ ├── COACHING
│ ├── COMPANY
│ └── OTHER
│
├── email REQUIRED + UNIQUE
├── phone OPTIONAL
├── address REQUIRED
├── logo OPTIONAL
├── created_at AUTOMATIC
├── updated_at AUTOMATIC
└── is_active REQUIRED → TRUE by default

