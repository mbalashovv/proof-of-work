# Start both containers
docker_up:
	docker compose up --build -d

# Start server container
server_up:
	docker compose up --build server -d

# Start client container
client_up:
	docker compose up --build client -d

# Watch logs in following mode in both containers
logs:
	docker compose logs -f

# Watch logs in following mode in server container
server_logs:
	docker compose logs server -f

# Watch logs in following mode in client container
client_logs:
	docker compose logs client -f

# Shut down containers
down:
	docker compose down

# Run all tests in src/tests folder
tests:
	python -m unittest discover -s src/tests -p "test_*.py"
