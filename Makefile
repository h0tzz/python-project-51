install:
	poetry install

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest -s
	poetry run pytest --cov=page_loader

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-force-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
