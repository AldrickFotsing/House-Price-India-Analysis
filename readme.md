# Analyse détaillée des prix de l'immobilier en Inde urbaine : tendances et perspectives

## Présentation du projet

Ce projet a pour objectif d'analyser et de prédire les prix des maisons à partir d'un dataset immobilier.

L'objectif est de reproduire un **workflow complet de Data Science**, allant de l'analyse exploratoire des données jusqu'à la modélisation prédictive avec plusieurs algorithmes de Machine Learning.

Le travail principal de ce projet est présenté dans le **Jupyter Notebook**, qui contient toutes les étapes de l'analyse.

## Présentation du projet

* Comprendre l'ensemble de données et le nettoyer.
* Faire une analyse du marché immobilier et la modélisation prédictive
* Créez des modèles de régression pour prédire les ventes en fonction d'une ou plusieurs caractéristiques.
* Évaluez également les modèles et comparez leurs scores respectifs tels que R², RMSE, etc.

## Description du jeu de donnée:

* Cet ensemble de données contient des informations détaillées sur les prix de l'immobilier résidentiel en Inde. Il comprend des caractéristiques telles que le nombre de chambres et de salles de bains, la surface habitable et la superficie du terrain, le nombre d'étages, la proximité de l'eau, l'état et la catégorie de la maison, les années de construction et de rénovation, ainsi que les coordonnées géographiques. D'autres caractéristiques incluent le nombre d'écoles à proximité, la distance de l'aéroport et le prix du bien.

* Le dataset provient du site Kaggle.

## Description des variables :

- `id` : Identifiant unique pour chaque propriété.
- `Date` : Date à laquelle le bien a été mis en vente ou vendu.
- `number of bedrooms`: Nombre total de chambres dans la maison.
- `number of bathrooms`: Nombre total de salles de bains dans la maison.
- `living area`: La surface habitable totale en mètre carré.
- `lot area`: La superficie totale du terrain en mètre carré.
- `number of floors`: Nombre total d'étages dans la maison.
- `waterfront present`: Indique si la maison a une vue sur l'eau (1 pour oui, 0 pour non).
- `number of views`: Nombre de fois où le bien a été consulté.
- `condition of the house`: État général de la maison sur une échelle (ex. : 1 à 5).
- `grade of the house`: Niveau de la maison.
- `Area of the house(excluding basement)`: Surface de la maison (sous-sol exclu).
- `Area of the basement`: Niveau du sous-sol.
- `Built Year`: Année de construction.
- `Renovation Year`: Année de rénovation.
- `Postal Code`: Code Postal.
- `Lattitude`: Latitude.
- `Longitude`: Longitude.
- `living_area_renov`: Superficie habitable de la maison après rénovation..
- `lot_area_renov`: Superficie totale du terrain après rénovation.
- `Number of schools nearby`: Nombre d'écoles à proximité.
- `Distance from the airport`: Distance de l'aéroport.
- `Price`: Prix.

## Technologies utilisées

Langage :

- Python

Bibliothèques principales :

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- scikit-learn

## Feature Engineering

Plusieurs variables ont été créées afin d'améliorer la performance des modèles :

- `house_age` : âge de la maison
- `total_house_area` : surface totale de la maison
- `lot_house_ratio` : ratio terrain / maison
- `is_renovated` : indique si la maison a été rénovée
- `years_since_renovation` : années depuis la rénovation
- `luxury_score` : score de luxe basé sur le grade et les salles de bain

Certaines variables ont également été transformées avec une **transformation logarithmique** afin de réduire l'asymétrie des distributions.

## Modèles de Machine Learning utilisés

Plusieurs modèles de régression ont été entraînés :

- Régression Linéaire
- Random Forest Regressor
- AdaBoost Regressor
- Gradient Boosting Regressor

## Résultats

Le modèle ayant obtenu les meilleures performances est :

**Random Forest Regressor**

Performance approximative :

- R² ≈ 0.87
- MAE ≈ 0.14 (sur le log du prix)

Cela signifie que le modèle explique environ **87 % de la variance du prix des maisons**.

## Validation du modèle

Pour vérifier la robustesse des modèles, une **validation croisée (5-Fold Cross Validation)** a été utilisée.

Random Forest obtient un score moyen d'environ :

R² ≈ 0.86

## Optimisation des hyperparamètres

Une optimisation des hyperparamètres a été réalisée avec **GridSearchCV**.

Meilleurs paramètres obtenus :

- `n_estimators` = **300**
- `max_depth` = **None**
- `max_features` = **None**
- `min_samples_split` = **5**

Score R² moyen après optimisation :

- `R²` ≈ **0.864**

## Statut du projet

Projet actuellement à l'étape :

Analyse des données + Machine Learning

Prochaine étape :

Déploiement du modèle avec **Streamlit** afin de créer une application permettant de prédire le prix d'une maison à partir de ses caractéristiques.

Le déploiement sera ajouté dans une prochaine version du projet.

## Auteur

Aldrick Fotsing

Étudiant en Data Science