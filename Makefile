.PHONY: help
help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help


.PHONY: lint-check
lint-check: ## Run ruff linter on project
	ruff check .

.PHONY: format-check
format-check: ## Run ruff format checker on project
	ruff format --check .

.PHONY: py-commit-check
py-commit-check: lint-check format-check ## Run lint and formatting checks

.PHONY: lint-fix
lint-fix: ## Run ruff linter with fixes
	ruff check . --fix

.PHONY: format-fix
format-fix: ## Run ruff formatter
	ruff format .
	ruff check --select I --fix .

.PHONY: fix-all
fix-all: format-fix lint-fix  ## Fix formatting and lint errors

