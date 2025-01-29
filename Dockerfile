# Utiliser Python comme image de base
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Exposer le port 5000 pour Flask
EXPOSE 5000
