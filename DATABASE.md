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

sections 
| Field                 | Type        | Required | Purpose                        |
| --------------------- | ----------- | -------: | ------------------------------ |
| `id`                  | BIGINT      |        ✅ | Unique section ID              |
| `organization_id`     | BIGINT      |        ✅ | Owning organization            |
| `department_id`       | BIGINT      |        ❌ | Department                     |
| `academic_session_id` | BIGINT      |        ✅ | Academic session               |
| `study_year`          | ENUM/choice |        ✅ | First/Second/Third/Fourth year |
| `name`                | VARCHAR(50) |        ✅ | Section name, e.g. A           |
| `created_at`          | DATETIME    |        ✅ | Creation time                  |
| `updated_at`          | DATETIME    |        ✅ | Last update                    |
| `is_active`           | BOOLEAN     |        ✅ | Defaults to TRUE               |

students
| Field             | Required | Details                       |
| ----------------- | -------: | ----------------------------- |
| `id`              |        ✅ | Unique student ID             |
| `organization_id` |        ✅ | Organization                  |
| `student_id`      |        ✅ | Institution's student/roll ID |
| `full_name`       |        ✅ | Full name                     |
| `email`           |        ❌ | Student email                 |
| `phone`           |        ❌ | Phone                         |
| `date_of_birth`   |        ❌ | DOB                           |
| `gender`          |        ❌ | Controlled choice             |
| `profile_photo`   |        ❌ | Photo                         |
| `created_at`      |        ✅ | Automatic                     |
| `updated_at`      |        ✅ | Automatic                     |
| `is_active`       |        ✅ | Default `TRUE`                |


students enrollment
| Field                 | Required | Details                   |
| --------------------- | -------: | ------------------------- |
| `id`                  |        ✅ | Enrollment ID             |
| `student_id`          |        ✅ | Student                   |
| `academic_session_id` |        ✅ | Academic session          |
| `department_id`       |        ❌ | Optional department       |
| `study_year`          |        ✅ | First/Second/Third/Fourth |
| `section_id`          |        ✅ | Student's section         |
| `created_at`          |        ✅ | Automatic                 |
| `updated_at`          |        ✅ | Automatic                 |
| `is_active`           |        ✅ | Current enrollment status |

subject

| Field             | Type         | Required | Purpose                         |
| ----------------- | ------------ | -------: | ------------------------------- |
| `id`              | BIGINT       |        ✅ | Unique subject ID               |
| `organization_id` | BIGINT       |        ✅ | Organization                    |
| `department_id`   | BIGINT       |        ❌ | Department offering the subject |
| `name`            | VARCHAR(150) |        ✅ | Subject name                    |
| `code`            | VARCHAR(50)  |        ✅ | Subject code                    |
| `description`     | TEXT         |        ❌ | Optional description            |
| `created_at`      | DATETIME     |        ✅ | Creation time                   |
| `updated_at`      | DATETIME     |        ✅ | Last update                     |
| `is_active`       | BOOLEAN      |        ✅ | Defaults to `TRUE`              |

course assignments
course_assignments
├── id
├── organization_id
├── subject_id
├── teacher_id
├── section_id
├── academic_session_id
├── assignment_type
│     ├── THEORY
│     ├── LAB
│     ├── PRACTICAL
│     └── OTHER
├── created_at
├── updated_at
└── is_active

class_sessions — FINAL
class_sessions
├── id
├── organization_id
├── course_assignment_id
├── session_date
├── start_time
├── end_time
├── room                  OPTIONAL
├── created_at
├── updated_at
└── is_cancelled         DEFAULT FALSE

attendance — FINAL
attendance
├── id
├── organization_id
├── student_id
├── class_session_id
├── status
│     ├── PRESENT
│     ├── ABSENT
│     ├── LATE
│     └── EXCUSED
├── marked_at
├── marked_by
├── remarks             OPTIONAL
├── created_at
└── updated_at