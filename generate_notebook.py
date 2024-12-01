import json

# Contenu du notebook
notebook_content = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Gestion de version avec Git et GitHub : Guide détaillé"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Introduction\n",
                "### Qu’est-ce que c’est ?\n",
                "- **Git** : Un système de gestion de versions distribué qui permet de suivre les modifications d'un fichier ou d’un ensemble de fichiers dans le temps. Il est principalement utilisé pour le développement logiciel, mais peut s'appliquer à n'importe quel type de fichiers.\n",
                "- **GitHub** : Une plateforme cloud qui héberge des dépôts Git et permet de collaborer sur le code, partager des projets, et les sauvegarder en ligne."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Pourquoi c’est important ?\n",
                "1. **Traçabilité** : Savoir quand, pourquoi, et par qui un fichier a été modifié.\n",
                "2. **Collaboration** : Faciliter le travail simultané sur un projet avec des fonctionnalités comme les branches et les Pull Requests.\n",
                "3. **Sécurité** : Sauvegarder votre code dans le cloud, éviter les pertes dues à des erreurs locales."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Pourquoi avons-nous besoin d’un système de contrôle de version ?\n",
                "### Problème : Le cycle de vie d’un fichier\n",
                "Les fichiers évoluent constamment :\n",
                "- Nous voulons suivre **les différentes versions** d’un fichier.\n",
                "- Identifier **qui** a effectué les changements, **quoi** a été modifié et **pourquoi**.\n",
                "- Faire cela manuellement est inefficace et source d’erreurs.\n",
                "\n",
                "### Solution : Git\n",
                "- Git automatise le suivi des versions.\n",
                "- Il enregistre chaque changement apporté à vos fichiers dans une **ligne de temps consultable**, tout en permettant de revenir facilement à des états précédents."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Utiliser Git pour suivre les modifications localement"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Commandes essentielles de Git\n",
                "\n",
                "| Commande                      | Description                                         | Exemple                                                 |\n",
                "|-------------------------------|-----------------------------------------------------|---------------------------------------------------------|\n",
                "| `git init`                   | Initialiser un dépôt Git dans un dossier.           | `git init`                                              |\n",
                "| `git clone <url>`            | Cloner un dépôt existant, par ex. sur GitHub.        | `git clone git@github.com:username/projet.git`          |\n",
                "| `git status`                 | Vérifier l’état des fichiers dans le dépôt local.   | `git status`                                            |\n",
                "| `git add <fichier>`          | Ajouter des fichiers au suivi de Git.               | `git add fichier.txt`                                   |\n",
                "| `git commit -m \"<message>\"`  | Sauvegarder les modifications avec un message clair.| `git commit -m \"Ajout d’un README\"`                    |\n",
                "| `git reset <fichier>`        | Retirer un fichier du suivi avant le commit.        | `git reset fichier.txt`                                 |\n",
                "| `git log`                    | Afficher l’historique des commits.                  | `git log`                                              |\n",
                "| `git diff <fichier>`         | Voir les modifications non suivies dans un fichier.| `git diff fichier.txt`                                 |\n",
                "| `git reset --hard <hash>`    | Revenir à une version spécifique.                   | `git reset --hard abc123`                              |\n",
                "| `git pull`                   | Récupérer les changements d’un dépôt distant.       | `git pull origin main`                                 |\n",
                "| `git push`                   | Envoyer les modifications locales vers un dépôt distant.| `git push origin main`                             |"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Démarrer un projet avec Git"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Créer un nouveau projet\n",
                "mkdir -p ~/code/mon_projet && cd $_\n",
                "git init"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Ajouter et valider des fichiers"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "echo \"Mon projet\" > README.md\n",
                "git add README.md\n",
                "git commit -m \"Initialisation du projet avec README\""
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Modifier un fichier"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "echo \"Nouvelle ligne\" >> README.md\n",
                "git diff README.md  # Voir les modifications\n",
                "git add README.md   # Ajouter au suivi\n",
                "git commit -m \"Ajout d'une nouvelle ligne au README\""
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.5"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

# Nom du fichier à générer
notebook_filename = "git_github_cours.ipynb"

# Sauvegarde du fichier
with open(notebook_filename, 'w', encoding='utf-8') as notebook_file:
    json.dump(notebook_content, notebook_file, indent=4)

print(f"Fichier '{notebook_filename}' généré avec succès !")
