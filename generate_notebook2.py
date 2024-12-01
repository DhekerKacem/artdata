{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Guide visuel et détaillé : Git et GitHub"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **1. Pourquoi avons-nous besoin d’un système de gestion de versions ?**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Qu’est-ce qu’un système de gestion de versions ?**\n",
    "Un système de gestion de versions comme **Git** permet de suivre les modifications dans un fichier ou un projet tout au long de son cycle de vie. Il fournit des réponses claires aux questions suivantes :\n",
    "- **Quand** un fichier a-t-il été modifié ?\n",
    "- **Quelles** modifications ont été apportées ?\n",
    "- **Pourquoi** ces modifications ont-elles eu lieu ?\n",
    "- **Qui** a fait les changements ?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Problème sans gestion de versions**\n",
    "- Gérer manuellement les versions (par exemple en utilisant des noms de fichiers comme `rapport_v1`, `rapport_v2_final`, etc.) est inefficace et sujet aux erreurs.\n",
    "- Les projets d’équipe deviennent rapidement chaotiques :\n",
    "  - Perte de fichiers ou écrasement des modifications.\n",
    "  - Difficulté à suivre les changements ou à revenir en arrière."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Illustration du problème : cycle de vie d’un fichier**"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Image illustrative\n",
    "from IPython.display import Image\n",
    "Image(url=\"https://via.placeholder.com/800x400.png?text=Cycle+de+vie+chaotique+d'un+fichier+sans+gestion+de+version\")"
   ],
   "execution_count": None,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Sans Git** : les fichiers sont dupliqués, modifiés aléatoirement, et rien n’est traçable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Pourquoi c’est important pour un projet ?**\n",
    "Avec **Git** :\n",
    "1. **Traçabilité complète** : Chaque modification est enregistrée, avec son auteur et ses raisons.\n",
    "2. **Collaboration facilitée** : Plusieurs développeurs peuvent travailler sur le même fichier sans écraser leurs modifications.\n",
    "3. **Récupération rapide** : Possibilité de revenir à une version stable en cas d’erreur."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Illustration du suivi avec Git**"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Illustration graphique\n",
    "Image(url=\"https://via.placeholder.com/800x400.png?text=Suivi+clair+et+organisé+avec+Git\")"
   ],
   "execution_count": None,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **2. Suivre les modifications localement avec Git**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Qu’est-ce que Git ?**\n",
    "Git est un **outil de gestion de versions distribué**. Contrairement à d’autres systèmes centralisés, Git permet :\n",
    "- De travailler hors ligne, avec une copie locale du projet.\n",
    "- D’intégrer facilement les modifications dans un dépôt centralisé (ex. : sur GitHub)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Commandes essentielles :**\n",
    "| **Commande**              | **Description**                                          | **Exemple**                                       |\n",
    "|----------------------------|----------------------------------------------------------|---------------------------------------------------|\n",
    "| `git init`                | Initialiser un dépôt Git dans un répertoire              | `git init`                                        |\n",
    "| `git clone <url>`         | Télécharger une copie d’un dépôt existant                | `git clone git@github.com:user/repo.git`         |\n",
    "| `git add <fichier>`       | Ajouter un fichier ou plusieurs fichiers au suivi        | `git add fichier.txt` ou `git add .`             |\n",
    "| `git commit -m \"<msg>\"`   | Enregistrer les modifications avec un message descriptif | `git commit -m \"Ajout de la fonctionnalité X\"`   |\n",
    "| `git log`                 | Afficher l’historique des modifications                  | `git log`                                         |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Cycle de vie d’un fichier avec Git**"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Graphique généré\n",
    "Image(url=\"https://via.placeholder.com/800x400.png?text=Cycle+de+vie+Git\")"
   ],
   "execution_count": None,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **3. Travailler avec des branches**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Qu’est-ce qu’une branche ?**\n",
    "Une branche est une **version parallèle** du projet. Elle permet de travailler sur une fonctionnalité spécifique sans affecter la version principale."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Illustration du concept de branches"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Illustration graphique\n",
    "Image(url=\"https://via.placeholder.com/800x400.png?text=Illustration+des+branches\")"
   ],
   "execution_count": None,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Commandes pour gérer les branches**\n",
    "| **Commande**              | **Description**                                  | **Exemple**                          |\n",
    "|----------------------------|--------------------------------------------------|---------------------------------------|\n",
    "| `git branch`              | Affiche toutes les branches disponibles          | `git branch`                         |\n",
    "| `git checkout -b nom`     | Crée et passe à une nouvelle branche             | `git checkout -b feature/nouvelle_fonction` |\n",
    "| `git merge`               | Fusionne une branche dans la branche actuelle    | `git merge feature/nouvelle_fonction` |\n",
    "| `git branch -d nom`       | Supprime une branche après fusion                | `git branch -d feature/ancienne_fonction` |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Gérer les conflits de fusion**\n",
    "Un conflit apparaît lorsque deux branches modifient les mêmes lignes d’un fichier. Git indique exactement où les conflits se trouvent et demande une résolution manuelle."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Illustration graphique\n",
    "Image(url=\"https://via.placeholder.com/800x400.png?text=Conflits+dans+Git\")"
   ],
   "execution_count": None,
   "outputs": []
  }
 ]
}
