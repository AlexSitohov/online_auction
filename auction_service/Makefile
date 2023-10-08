build-dc:
	source ./env.sh && docker-compose up --build

build-native:
	source ./env.sh && uvicorn --log-level debug src.app.main:app --port 8000 --reload
