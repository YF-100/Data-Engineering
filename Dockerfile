FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu du dossier Flask dans le conteneur
COPY ./flask /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Flask
EXPOSE 5000

# Commande pour lancer Flask
CMD ["python", "app.py"]

