# Contributing to tracewise

Thanks for your interest in contributing! This project aims to be lightweight and approachable. Please follow the guidelines below to keep reviews fast and releases stable.

## Ways to help
- Report bugs with a minimal reproduction and sample slow log (redact sensitive data).
- Propose features or improvements with a clear use case.
- Pick up issues labeled `good first issue`.

## Development setup
1) Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2) Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Code style
- Keep changes small and focused.
- Prefer clear, readable code over cleverness.
- Add or update tests when behavior changes.
- Format and lint with Ruff before opening a PR.

## Testing
- Run the test suite before opening a PR.
- If no tests exist yet, include a short note in your PR describing manual verification.

## Developer commands
- Install in editable mode: `pip install -e ".[dev]"`
- Run tests: `pytest`
- Lint: `ruff check .`
- Format: `ruff format .`

## Pull requests
- Keep PRs small and focused.
- Provide a concise summary and rationale.
- Include tests for new behavior or explain why not.
- Link related issues (e.g., `Closes #123`) when applicable.
- Include examples or output snippets for CLI or report changes.

## Reporting security issues
If you believe you’ve found a security issue, please avoid public disclosure. Open a private report by contacting the maintainer.
