#  ALIKHARESTO : Architecture Full-Stack & Modélisation de Données (Django)

**Auteur :** Alassane POUYE | Étudiant en L3 Mathématiques-Informatique  
**Technologies :** Python 3, Framework Django, SQLite/SQL, MDBootstrap (HTML5/CSS3)  

##  Contexte et Objectif

"Alikharesto" est une application web Full-Stack développée pour démontrer mes compétences en **ingénierie logicielle globale**. Prenant pour cas d'usage le système de gestion d'un restaurant gastronomique, l'objectif de ce projet est d'illustrer la maîtrise de l'architecture **Model-View-Template (MVT)**, la modélisation de bases de données relationnelles complexes, et l'intégration d'une interface utilisateur (UI) dynamique et responsive.



##  Architecture Modulaire (Separation of Concerns)

Le projet est divisé en plusieurs applications indépendantes (Apps) pour garantir un code maintenable et évolutif :

*  **`accounts` (Sécurité & Auth) :** Gestion sécurisée du parcours utilisateur (Inscription, Connexion, Déconnexion) utilisant le système natif de Django et la protection des sessions.
*  **`dishes` (Catalogue & Médias) :** Gestion du menu (Catégories et Plats). Utilisation de **Class-Based Views (CBV)** (`ListView`, `DetailView`, `CreateView`) pour une logique orientée objet propre. Gestion du téléversement dynamique d'images (`ImageField`).
* **`core` (Logique Métier & Réservations) :** Le cœur du système. Gestion des Commandes, des Paiements, et des Réservations de tables avec vérification des disponibilités.

##  Modélisation et Base de Données

La structure des données a été pensée pour garantir l'intégrité référentielle stricte :
1. **Relations complexes :** Utilisation avancée des `ForeignKey` (Catégories/Plats), `OneToOneField` (Commande/Paiement pour s'assurer qu'une commande n'est payée qu'une fois), et `ManyToManyField` (Historique).
2. **Automatisation via les Signaux (Django Signals) :** Implémentation du pattern *Observer* (`@receiver`). Lorsqu'une commande passe au statut "Payée" ou "Annulée", un signal modifie automatiquement la disponibilité de la table en base de données.
3. **Protection des Données :** Utilisation de `on_delete=models.PROTECT` et `SET_NULL` pour éviter la corruption de l'historique comptable en cas de suppression d'un plat ou d'une table.

##  Sécurité et Bonnes Pratiques

* **Protection des Routes :** Utilisation systématique de `@login_required` et de `LoginRequiredMixin` pour interdire l'accès aux vues métiers aux utilisateurs non authentifiés.
* **Sécurité des Formulaires :** Protection contre les failles CSRF (Cross-Site Request Forgery) via le tag `{% csrf_token %}`.
* **Interface d'Administration :** Panneau d'administration Django personnalisé (`@admin.register`, `list_display`, `search_fields`) pour permettre une gestion métier CRUD rapide.

##  Lancement du projet en local

Pour tester l'application sur votre machine :

1. Clonez le dépôt : `git clone https://github.com/POUYE25/Alikharesto-Django-FullStack.git`
2. Appliquez les migrations de la base de données : `python manage.py migrate`
3. Lancez le serveur de développement : `python manage.py runserver`
4. Accédez à l'application via `http://127.0.0.1:8000/`
