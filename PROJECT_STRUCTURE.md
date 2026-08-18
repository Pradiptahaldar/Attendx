AttendX/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── PROJECT_STRUCTURE.md
├── .gitignore
│
├── instance/
│   └── config.py
│
├── routes/
│   ├── __init__.py
│   ├── home.py
│   ├── auth.py
│   ├── register.py
│   ├── dashboard.py
│   ├── students.py
│   ├── attendance.py
│   ├── reports.py
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   ├── organization.py
│   ├── admin.py
│   ├── teacher.py
│   ├── student.py
│   ├── attendance.py
│   └── subject.py
│
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   ├── attendance_service.py
│   ├── report_service.py
│   ├── student_service.py
│   ├── teacher_service.py
│   └── face_service.py
│
├── database/
│   ├── db.py
│   └── schema.sql
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   ├── validators.py
│   ├── security.py
│   └── constants.py
│
├── templates/
│   ├── base.html
│   │
│   ├── home/
│   │   └── index.html
│   │
│   ├── auth/
│   │   ├── login.html
│   │   ├── setup.html
│   │   ├── register.html
│   │   └── forgot_password.html
│   │
│   ├── dashboard/
│   │   └── dashboard.html
│   │
│   ├── students/
│   │   ├── students.html
│   │   └── student_profile.html
│   │
│   ├── attendance/
│   │   └── attendance.html
│   │
│   ├── reports/
│   │   └── reports.html
│   │
│   └── settings/
│       └── settings.html
│
├── static/
│   │
│   ├── css/
│   │   ├── global.css
│   │   ├── components.css
│   │   │
│   │   └── pages/
│   │       ├── home.css
│   │       ├── login.css
│   │       ├── setup.css
│   │       ├── dashboard.css
│   │       ├── students.css
│   │       ├── attendance.css
│   │       ├── reports.css
│   │       └── settings.css
│   │
│   ├── js/
│   │   ├── global.js
│   │   ├── components.js
│   │   │
│   │   └── pages/
│   │       ├── login.js
│   │       ├── setup.js
│   │       ├── dashboard.js
│   │       ├── students.js
│   │       ├── attendance.js
│   │       ├── reports.js
│   │       └── settings.js
│   │
│   ├── images/
│   │   ├── illustrations/
│   │   ├── logos/
│   │   ├── avatars/
│   │   └── backgrounds/
│   │
│   ├── icons/
│   │
│   ├── fonts/
│   │
│   └── uploads/
│
├── exports/
│   ├── pdf/
│   ├── excel/
│   └── csv/
│
├── uploads/
│   ├── students/
│   ├── teachers/
│   └── organizations/
│
├── tests/
│   ├── test_auth.py
│   ├── test_students.py
│   └── test_attendance.py
│
└── docs/
    ├── UI_DESIGN.md
    ├── DATABASE.md
    ├── API.md
    └── CHANGELOG.md

                 ┌──────────────┐
                 │    AttendX   │
                 │  Landing Page│
                 └──────┬───────┘
                        │
                 First time?
                   /          \
                 YES           NO
                  │             │
                  ▼             ▼
              Get Started      Login
                  │             │
                  ▼             ▼
           Organization       Dashboard
              Setup
                  │
                  ▼
             Admin Setup
                  │
                  ▼
           Setup Complete
                  │
                  ▼
                Login
                  │
                  ▼
             Dashboard