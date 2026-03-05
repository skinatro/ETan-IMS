# E-Tan Inventory Management System

E-Tan IMS is a specialized platform developed for E-TAN to allow SFIT ECS and ExTC branch students to rent and borrow electronic components for their mini-projects.

## Project Documentation

Before starting development or contributing, please review the core documentation in the `./docs` directory to understand the system architecture and project scope:

* **[SRS (Software Requirements Specification)](./docs/SRS.md)**: Detailed functional requirements, user roles, and system constraints.
* **[ERD (Entity Relationship Diagram)](./docs/ERD.dbml)**: The database schema outlining how Users, Components, and Orders interact.

## Tech Stack

**Framework:** Django (Python)  
**Database:** SQLite (For Dev)

## Features

### Admin
- **Dashboard**: View borrowed item count and recent orders
- **Inventory**: List, add, and edit components with categories, images, and datasheets
- **Orders**: Accept or reject student rental orders

### Customer (Student)
- **Dashboard**: View personal order history
- **Inventory**: Browse available components with filtering
- **Orders**: Place rental orders and track status

## Quick Start

To get the project running locally:

1.  **Clone & Install:** `git clone ... && uv sync`
2.  **Setup Environment:** Copy `IMS/IMS/.env.example` to `IMS/IMS/.env`
3.  **Migrate:** `python IMS/manage.py migrate`
4.  **Create Superuser:** `python IMS/manage.py createsuperuser`
5.  **Run:** `python IMS/manage.py runserver`

For detailed instructions, see the **[Contributing Guide](./CONTRIBUTING.md)**.

## URL Routes

| Path | Description |
|---|---|
| `/` | Dashboard (admin or customer) |
| `/inventory/` | Browse components |
| `/inventory/<id>/` | Component details |
| `/inventory/add/` | Add component (admin) |
| `/orders/` | Order listing |
| `/orders/<id>/` | Order details |
| `/register/` | Student registration |
| `/login/` | Login |
| `/admin/` | Django admin panel |

## Contribution Guidelines

Please refer to the **[CONTRIBUTING.md](./CONTRIBUTING.md)** file for detailed information on:
* Local installation and setup
* Branching strategy
* Commit message conventions
* The review and merge process

---
*Developed for E-Tan SFIT.*
