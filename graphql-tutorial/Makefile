# Django and Docker commands

PROJECT_NAME = project
DJANGO_PROJECT_NAME = project
PROJECT_SRV = ${PROJECT}_SRV

.PHONY = help
.DEFAULT:
	@echo "Usage: "
	@make help

help: ## Show this help.
	# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
build: ## Build and start project.
	@docker-compose up --build
start: ## Start project running in a non-dettached mode.
	@docker-compose up
startbg: ## Start project running in dettached mode - background.
	@docker-compose up -d
stop: ## Stop the running project.
	@docker-compose stop
requirements: ## Update requirements.txt file
	poetry export -v -o graphql-tutorial/backend/requirements.txt
fixtures:
	@docker-compose exec backend python manage.py loaddata ingredients
