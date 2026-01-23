## Getting Started

To get started with the project locally, follow these steps:

### Prerequisites

* **Python 3.14+**: The project uses the latest features of Python.
* **uv**: A fast Python package installer and resolver. You can install it via:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/skinatro/ETan-IMS.git
   cd ETan-IMS
   ```

2. **Install dependencies:**
   The project uses `uv` for dependency management. Run the following command to create a virtual environment and install all dependencies:
   ```bash
   uv sync
   ```

3. **Configure Environment Variables:**
   Copy the example environment file and update it with your settings:
   ```bash
   cp IMS/IMS/.env.example IMS/IMS/.env
   ```
   Open `IMS/IMS/.env` and set a `DJANGO_SECRET_KEY` and ensure `DEBUG=1` for local development.

4. **Initialize Database:**
   Run the migrations to set up your local SQLite database:
   ```bash
   python IMS/manage.py migrate
   ```

5. **Create a Superuser (Optional):**
   To access the Django admin interface, create a superuser:
   ```bash
   python IMS/manage.py createsuperuser
   ```

### Running the Development Server

Start the Django development server:
```bash
python IMS/manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

### Running Tests

To run the project's test suite:
```bash
python IMS/manage.py test
```

---

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
* `chore:`: Updating tasks, dependencies, etc.; no production code change.

*Example: `feat: implement JWT login for student portal`*

### 3. Review & Merge Process
1.  Fork the repository and create your feature branch.
2.  Submit a Pull Request (PR) to the `dev` or `docs` branch as appropriate.
3.  All submissions will be reviewed.
4.  Once the review is successful, the code will be merged into the `main` branch.
