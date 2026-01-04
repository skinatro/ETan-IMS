# E-Tan Inventory Management System (IMS)

E-Tan IMS is a specialized platform developed for SFIT ECS and ExTC branch students to rent and borrow electronic components for their mini-projects.

## Project Documentation

Before starting development or contributing, please review the core documentation in the `./docs` directory to understand the system architecture and project scope:

* **[SRS (Software Requirements Specification)](./docs/SRS.md)**: Detailed functional requirements, user roles, and system constraints.
* **ERD (Entity Relationship Diagram)**: The database schema outlining how Users, Products, and Orders interact.

## Tech Stack

* **Frontend**: ReactJs & Tailwind CSS
* **Backend**: Django (Python 3+)
* **Database**: PostgreSQL / MySQL
* **Authentication**: JWT (JSON Web Tokens)

## Contribution Guidelines

To maintain code quality and a clear project history, please adhere to the following guidelines:

### 1. Branching Strategy
* **`main`**: Reserved for stable, production-ready code. No direct pushes allowed.
* **`dev`**: The primary branch for all code contributions and feature development.
* **`docs`**: Use this branch specifically for updating documentation (SRS, README, etc.).

### 2. Conventional Commits
We strictly follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. Every commit message must be prefixed with a type:
* `feat:`: A new feature for the user.
* `fix:`: A bug fix.
* `docs:`: Documentation only changes.
* `refactor:`: A code change that neither fixes a bug nor adds a feature.
* `chore:`: Updating grunt tasks etc; no production code change.

*Example: `feat: implement JWT login for student portal`*

### 3. Review & Merge Process
1.  Fork the repository and create your feature branch.
2.  Submit a Pull Request (PR) to the `dev` or `docs` branch as appropriate.
3.  All submissions will be **reviewed by Om Kate**.
4.  Once the review is successful, the code will be merged into the `main` branch.

---
*Developed for E-Tan SFIT.*