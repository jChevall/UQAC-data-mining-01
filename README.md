# UQAC-data-mining-01
Devoir proposé dans le cadre du cours de forage de données à l'UQAC. A pour but de détecter des intrusions avec une version améliorée de l'algorithme ID3.

# 2.1 Synthèse
Plan de la synthèse
Introduction
Contexte article
•	Sécurité info
•	DARPA
•	Intrusion
Présentation des arbres de décision
•	Objectif
•	Utilisation
•	Création
Présentation de l'approche du projet
•	Algo
•	Entropie choisi
•	Resultat attendu
Résumé de l'expérimentation
•	Mise en place
•	Résultat
Conclusion


L'article présenté porte sur la détection de tentatives d'intrusion dans un système informatique. Il présente un classifier inspiré de ID3. Celui-ci affiche, d'après l'article des performances bien supérieures aux classifiers existants sur un jeu de données. Celui-ci permet aux classifiers d'apprendre quelles requêtes sont des utilisations normales ou des attaques. 

Il est également présenté dans l'article une constante 'alpha' comprise entre 0 et 1 qui influe sur une partie de l'algorithme.

L'objectif de ce document est de retrouver les résultats obtenus dans l'article et d'étudier d'avantage l'influence de la constante 'alpha' dans les performances de l'algorithme.

Le jeu de données utilisé contient près de 5 millions d'instances et provient de la DARPA (Defense Advanced Research Projects Agency) qui est l'agence qui effectue des travaux de recherche & dévelopement à usage militaire. 


Lors de ce travail, nous utiliserons le logiciel weka pour supporter notre classifier ID3 modifié. Cela permet de réutiliser le travail déjà existant au niveau de l'interface graphique qui permettra de visualiser les données utilisées.


# transformations du fichier d'entrée

Nous avons téléchargé le fichier 'kddcup.data_10_percent_corrted' depuis l'adresse indiquée dans le sujet. Cependant, ce
fichier n'est pas au format d'entrée de Weka. Il faudra donc effectuer une transformation de celui-ci.

Nous avons donc réalisé un script python qui prend en paramètre le nom du fichier téléchargé et un nom de fichier de sortie qui aura le format .arff pour Weka. De cette façon, les transformations sont automatisées et sont reproductibles.

Ce script est disponible ici : https://github.com/librallu/UQAC-data-mining-01/blob/master/to_arff.py

Basiquement, le script contient de base les informations des noms des attributs si ils sont discrets ou continus.
Il extrait depuis le fichier d'entrée les différentes valeurs possibles des attributs, rajoute les meta informations
pour weka et applique quelques reformatages des données.


Il peut être utilisé par la commande suivante: 

  python to_arff.py input_file output_file

output_file peut maintenant être chargé dans weka.

Nous avons exécuté à titre d'example l'algorithme J48 sur ce jeu de données et obtenons le résultat présenté sur l'image https://github.com/librallu/UQAC-data-mining-01/blob/master/result_j48.png

# Journal

Dans un premier temps, nous nous sommes posés la question du format de données. Celui fourni de base n'est pas compatible avec weka (qui demande un format .arff). La première étape de notre projet à été de réaliser un script
qui permet de proposer un format arff en sortie. Une fois ceci réalisé, il est possible à partir de Weka de charger
le jeu de données et d'appliquer certains algorithmes comme C4.5 (J48 dans Weka). Celui-ci donne d'ailleurs des résultats biens meilleurs que ceux annoncés avec l'algorithme de l'article. Cela s'explique par le fait que les données fournies de base ont des attributs continus tandis que l'algorithme ID3 dont il est question dans l'article ne traite
que des valeurs discrètes. Cela nous a mis la puce à l'oreille et avons compris que les auteurs de l'article ont fait le choix de supprimer toutes les données continues.

Une deuxième étape est de modifier le script produit pour supprimer les données continues du jeu de données.
Une fois ceci accompli, il est possible de lancer l'algorithme ID3 qui donne un résultat autour de 97-98 % de
réponses correctes.

L'étape suivante est d'implémenter dans weka l'algorithme présenté dans l'article. Cet algorithme consiste à un simple
changement d'heuristique. Nous reprenons donc les sources de ID3 dans weka et modifions la fonction ComputeHeuristic.
Une fois ce changement effectué, il est possible d'exécuter dans Weka l'algorithme en question.

L'heuristique présente un paramètre alpha qu'il est possible de faire varier. Pour se faire, nous avons opté pour
une modification de l'interface de Weka pour paramétrer l'algorithme directement depuis l'interface. Pour cela, nous
modifions la docstring de la classe de ID3 modifiée et ajoutons des getters/setters pour le paramètre. De cette façon,
une nouvelle option s'affiche pour paramétrer l'algorithme et nous pouvons maintenant faire varier ce paramètre.

# TODO

- rédiger l'abstract
- reprendre le format d'entrée pour qu'il soit compatible avec celui-de Weka <- fait
- importer un module perso dans weka <- fait. Il suffit de recompiler les sources avec le fichier .java dedans
- implémenter l'entropie <- fait. Testée sur weather-nominal. On est moins bons qu'avec l'entropie de Shannon.
  Testée aussi sur le jeu de données transformé. Il s'avère que l'on a exactement le même résultat qu'avec l'entropie
  de Shannon. C'est un peu étrange
- ajouter le changement du alpha dans les paramètres de l'algorithme pour tester directement avec weka le changement du
  alpha. <- fait
- ajouter journal explicatif sur comment ajouter des paramètres à un algorithme dans weka

# Bibliographie

- https://weka.wikispaces.com/Writing+your+own+Classifier+%28post+3.5.2%29
  création d'un classifier avec Weka
- http://repository.cmu.edu/cgi/viewcontent.cgi?article=1161&context=math
  article portant sur l'entropie de Havrda et Charvat
- http://kdd.ics.uci.edu/databases/kddcup99/
  jeux de données utilisés
