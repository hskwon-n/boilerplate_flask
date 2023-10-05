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
