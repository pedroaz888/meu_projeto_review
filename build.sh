#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala as bibliotecas do requirements.txt
pip install -r requirements.txt

# Reúne os arquivos de CSS/JS (essencial para o WhiteNoise)
python manage.py collectstatic --no-input

# Cria as tabelas no banco de dados do Render
python manage.py migrate