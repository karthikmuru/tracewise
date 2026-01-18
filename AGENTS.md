# Repository Guidelines

## Project Structure & Module Organization
- This repository is currently minimal; add new modules under a top-level `src/` directory and keep tests in a parallel `tests/` directory.
- Use `docs/` for project documentation, `scripts/` for automation, and `assets/` for static files (images, fixtures, etc.).
- Example layout:
  - `src/` — application code
  - `tests/` — unit/integration tests
  - `scripts/` — developer tooling
  - `docs/` — architecture notes and ADRs

## Build, Test, and Development Commands
- No build or run commands are defined yet. Add a `README.md` with the exact commands once tooling is selected.
- Suggested defaults once tooling exists:
  - `npm run dev` or `make dev` for local development
  - `npm test` or `make test` for test execution
  - `npm run lint` or `make lint` for static analysis

## Coding Style & Naming Conventions
- Default to 2-space indentation for frontend code and 4-space for backend code, unless the chosen framework dictates otherwise.
- Prefer descriptive, lowercase-kebab filenames for scripts (`build-assets.sh`) and lowercase snake_case for test files (`user_login_test`).
- Add formatting and linting tools early (e.g., Prettier/ESLint or Black/Ruff) and enforce via CI.

## Testing Guidelines
- Use a single test framework per language and document it in `README.md`.
- Name tests after the behavior they verify (e.g., `auth_login_success`).
- Target meaningful coverage; document any thresholds in CI once established.

## Commit & Pull Request Guidelines
- No commit conventions are established yet. Use short, imperative subject lines (e.g., "Add user auth middleware").
- Pull requests should include:
  - A concise description of the change and rationale.
  - Linked issues or tickets when applicable.
  - Screenshots or logs for user-facing changes.

## Configuration & Security Notes
- Keep secrets out of source control; use `.env` files and document required keys in `README.md`.
- Store environment-specific configuration under `config/` if needed.
