################################################################################
# Makefile for mikewebb.tech hugo site and blog content repo
#
# Workflow Targets:
#
# 1. make sync
#    - Pulls the latest changes from the Hugo site repo (current branch)
#      and the blog repo (main branch), then updates submodules.
#
# 2. make blogpush [MSG="commit message"]
#    - Pushes any changes in the blog repo (~/Projects/mikewebbtech-blog/main)
#    - Updates the submodule pointer in the Hugo repo and pushes it.
#    - MSG can be overridden to customize the commit message.
#
# 3. make sitepush [MSG="commit message"]
#    - Commits and pushes any changes in the Hugo site repo.
#    - MSG can be overridden to customize the commit message.
#
# 4. make draft TITLE="Post Title" [DATE=YYYY-MM-DD]
#    - Creates a new Markdown draft in the blog repo.
#    - Places the file in content/articles/YYYY/YYYY-MM-DD-title.md
#    - Sets YAML front matter: date, draft=false, title, summary, tags, categories, series
#    - DATE optional; defaults to today. Front matter date matches the DATE.
#    - Does not overwrite existing drafts with same date+title.
#
# Example usage:
#   make sync
#   make blogpush MSG="Add new article"
#   make sitepush MSG="Fix theme CSS"
#   make draft TITLE="Hugo Submodules Workflow"
#   make draft TITLE="Essential Eight in Practice" DATE=2025-08-15
################################################################################

# Paths to local repos
BLOG_DIR := ../mikewebbtech-blog
SITE_DIR := .

# Detect current branch in Hugo site repo
BRANCH := $(shell git -C $(SITE_DIR) rev-parse --abbrev-ref HEAD)

# Commit message (can be overridden: make blogpush MSG="...")
MSG ?= "Update blog content"

.PHONY: blogpush sitepush sync draft

## blogpush: Push blog repo changes, then update Hugo site pointer
blogpush:
	@echo ">>> Pushing blog changes from $(BLOG_DIR) on branch main..."
	cd $(BLOG_DIR) && git add . && git commit -m "$(MSG)" || echo "No changes to commit in blog repo"
	cd $(BLOG_DIR) && git push origin main
	@echo ">>> Updating Hugo site pointer on branch $(BRANCH)..."
	cd $(SITE_DIR) && git add content/articles
	cd $(SITE_DIR) && git commit -m "Update articles pointer" || echo "No changes to commit in Hugo repo"
	cd $(SITE_DIR) && git push origin $(BRANCH)

## sitepush: Commit & push Hugo site repo changes
sitepush:
	@echo ">>> Pushing Hugo site changes on branch $(BRANCH)..."
	cd $(SITE_DIR) && git add .
	cd $(SITE_DIR) && git commit -m "$(MSG)" || echo "No changes to commit in Hugo repo"
	cd $(SITE_DIR) && git push origin $(BRANCH)

## sync: Pull latest changes in both repos and update submodules
sync:
	@echo ">>> Pulling latest Hugo site repo changes (branch $(BRANCH))..."
	cd $(SITE_DIR) && git pull origin $(BRANCH)
	@echo ">>> Pulling latest blog repo changes (branch main)..."
	cd $(BLOG_DIR) && git pull origin main
	@echo ">>> Updating submodule pointer in Hugo site..."
	cd $(SITE_DIR) && git submodule update --init --recursive

## draft: Create a new blog draft
draft:
	@if [ -z "$(TITLE)" ]; then \
		echo "❌ Error: Please provide a TITLE. Usage: make draft TITLE=\"My New Post\" [DATE=YYYY-MM-DD]"; \
		exit 1; \
	fi; \
	DATE=$${DATE:-$$(date +"%Y-%m-%d")}; \
	SLUG=$$(echo "$(TITLE)" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-'); \
	YEAR=$$(echo $$DATE | cut -d'-' -f1); \
	FILE="$(BLOG_DIR)/content/articles/$$YEAR/$$DATE-$$SLUG.md"; \
	if [ -f "$$FILE" ]; then \
		echo "❌ Error: Draft already exists: $$FILE"; \
		exit 1; \
	fi; \
	mkdir -p "$$(dirname $$FILE)"; \
	echo "---" > $$FILE; \
	echo "date: $${DATE}T00:00:00+08:00" >> $$FILE; \
	echo "draft: false" >> $$FILE; \
	echo "title: \"$(TITLE)\"" >> $$FILE; \
	echo "summary:" >> $$FILE; \
	echo "tags:" >> $$FILE; \
	echo "categories:" >> $$FILE; \
	echo "series:" >> $$FILE; \
	echo "---" >> $$FILE; \
	echo "" >> $$FILE; \
	echo "📝 Draft created: $$FILE"

