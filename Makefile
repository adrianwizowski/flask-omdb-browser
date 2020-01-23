run:
	flask run

test:
	python -m pytest

docker:
	docker-compose up --build

lint:
	pylint flask_app/