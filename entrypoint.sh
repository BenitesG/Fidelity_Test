#!/bin/sh

echo "Esperando pelo PostgreSQL..."

until python -c "import socket; import os; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((os.environ.get('POSTGRES_HOST'), int(os.environ.get('POSTGRES_PORT')))); s.close()"; do
  >&2 echo "Postgres está indisponível - esperando..."
  sleep 1
done

>&2 echo "PostgreSQL iniciado"
exec "$@"