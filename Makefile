export DOCKER_DEFAULT_PLATFORM=linux/amd64

up:
	docker compose -f docker-compose-local.yaml up -d

down:
	docker compose -f docker-compose-local.yaml down --remove-orphans

up_ci:
	docker compose -f docker-compose-ci.yaml up -d

up_ci_rebuild:
	docker compose -f docker-compose-ci.yaml up --build -d

down_ci:
	docker compose -f docker-compose-ci.yaml down --remove-orphans

run-db:
	docker run --name tesseract_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=tesseract -d postgres:16
