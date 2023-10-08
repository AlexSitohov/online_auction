export POSTGRES_DB_LOGIN='postgres'
export POSTGRES_DB_PASSWORD='postgres_pass'
export POSTGRES_DB_HOST='auction_service_db'
export POSTGRES_DB_PORT=5442
export POSTGRES_DB_NAME='auction_db'

export PYTHONPATH=$PWD:$PWD/src:$PWD/src/
export SQLALCHEMY_ECHO='true'
export SQLALCHEMY_POOL_SIZE=10
export APP_HOST=0.0.0.0
export APP_PORT=8000
export LOGGING_LEVEL=10

echo "Переменные окружения установлены"

