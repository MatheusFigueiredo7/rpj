#!/bin/bash

echo "Aplicando as migrações no banco de dados..."
python manage.py migrate

echo "Iniciando o servidor Python..."
exec "$@"
