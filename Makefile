up:
	docker compose --env-file envs/development.env up --build -d

down:
	docker compose --env-file envs/development.env down

install-requirements:
	pip install -r requirements.txt

install:
	pip install $(PROJECT)
	$(MAKE) freeze

freeze:
	pip freeze > requirements.txt

docker-exec:
	docker exec -it boilerplate_flask-server-1 $(COMMAND)

test:
	$(MAKE) docker-exec COMMAND=pytest

coverage:
	$(MAKE) docker-exec COMMAND="coverage run -m pytest"
	$(MAKE) docker-exec COMMAND="coverage report"
