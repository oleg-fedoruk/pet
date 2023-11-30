run-db:
	docker run --name tesseract_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=tesseract -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres:15
