# Agent Guidelines

## PR Rules
- One PR per branch. One branch per task.
- Never close a PR to open a replacement. Fix in place.
- Never push directly to main.
- Squash merge only.
- Branches auto-delete after merge.
- Branch naming: `user/CameronImmesoete/<description>`

## CI Requirements
- All CI checks must pass before merge.
- No `[skip ci]` commits unless pure documentation.
- If CI is red on main, fix it before other work.

## Security
- Never commit secrets, API keys, tokens, or credentials.
- Never add dependencies without justification.
- Never force push to main.
- Run tests before pushing.

## Code Quality
- Tests required for all new functions.
- Lint must pass (ruff for Python, eslint for TypeScript).
- Type checks must pass (mypy for Python, tsc for TypeScript).
- Prefer simple, readable code over clever abstractions.

## Shared Workflows
- Python repos can use the reusable CI workflow: `uses: CameronImmesoete/.github/.github/workflows/python-ci.yml@main` # @main is used here because this IS the source repo; downstream callers should pin to a release tag or commit SHA
  - Note: The doubled `.github` is intentional. The first is the repo name (`CameronImmesoete/.github`), the second is the workflows directory within it (`.github/workflows/`).
- **Pinning policy:** `@main` is temporary during initial setup. Once the repo has a stable first release, all downstream callers must pin to a tagged release or specific commit SHA (e.g., `@v1.0.0` or `@abc1234`). Never use `@main` in production workflows. Update callers when the shared workflow changes by bumping the pinned reference.
