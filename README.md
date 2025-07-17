Contexte : 
L’entreprise « Place de Marché » veut classifier automatiquement les articles mis en vente sur sa plateforme. 
Pourquoi faire ? Pour améliorer l’expérience utilisateur, éviter les erreurs de saisie et améliorer les traitements des données.
L’entreprise a à sa disposition 2 variables, la description et les images saisie par le client.

Ce projet est découpé en trois parties :
1.	Notebook de faisabilité pour savoir s’il est pertinent d’investir dans ce projet, où j’étudie quelle variable et quelle technique d’extraction est la plus pertinente,
2.	Notebook de classification, j’établis une stratégie d’entraînement du modèle et j’essaye d’obtenir les meilleures performances,
3.	Un court script Python d’extraction des données d’une API pour augmenter les données. 

Faisabilité 
Test de 5 méthodes de vectorisation des textes : 
•	Bag of Words
•	Tf-Idf
•	Word2Vec
•	Use
•	Bert
Test de 2 méthodes de vectorisation des images : 
•	SIFT
•	VGG 16
Chacun des vecteurs obtenus est réduit par T-SNE en 2 dimensions. On réalise une classification k-means puis on compare la classification au réel en quantifiant avec le score d’ARI.
Les deux meilleurs scores sont obtenus avec Tf-idf et VGG 16, respectivement 0.39 et 0.45. Pour la suite du projet je travaillerai avec VGG 16


Entraînement du modèle
Objectifs : 
•	Optimisation de l’Accuracy et du temps d’entraînement 
•	Identifier la meilleure fonction de perte via une cross validation
o	MAE
o	MSE
o	Categorical crossentropy
o	Poisson
•	Amélioration des données pour réduire le sur-apprentissage et identifier le modèle final.
