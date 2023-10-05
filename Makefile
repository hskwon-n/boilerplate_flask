up:
	docker compose --env-file envs/development.env up --build -d

down:
	docker compose --env-file envs/development.env down
