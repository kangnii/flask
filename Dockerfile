# Image de base
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Port exposé
EXPOSE 5000

# Commande de lancement
CMD ["python", "app.py"]
