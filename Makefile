install:
	poetry install

page-loader:
	poetry run page-loader

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest --cov=page_loader --cov-report xml tests/

test-watch:
	poetry run ptw

lint:
	poetry run flake8 page_loader

.PHONY: page-loader test
