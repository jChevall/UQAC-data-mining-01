# UQAC-data-mining-01
Devoir proposé dans le cadre du cours de forage de données à l'UQAC. A pour but de détecter des intrusions avec une version améliorée de l'algorithme ID3.

# 2.1 Synthèse

L'article présenté porte sur la détection de tentatives d'intrusion dans un système informatique. Il présente un classifier inspiré de ID3. Celui-ci affiche, d'après l'article des performances bien supérieures aux classifiers existants sur un jeu de données. Celui-ci permet aux classifiers d'apprendre quelles requêtes sont des utilisations normales ou des attaques. 

Il est également présenté dans l'article une constante 'alpha' comprise entre 0 et 1 qui influe sur une partie de l'algorithme.

L'objectif de ce document est de retrouver les résultats obtenus dans l'article et d'étudier d'avantage l'influence de la constante 'alpha' dans les performances de l'algorithme.

Le jeu de données utilisé contient près de 5 millions d'instances et provient de la DARPA (Defense Advanced Research Projects Agency) qui est l'agence qui effectue des travaux de recherche & dévelopement à usage militaire. 


Lors de ce travail, nous utiliserons le logiciel weka pour supporter notre classifier ID3 modifié. Cela permet de réutiliser le travail déjà existant au niveau de l'interface graphique qui permettra de visualiser les données utilisées.


# transformations du fichier d'entrée

Nous avons téléchargé le fichier 'kddcup.data_10_percent_corrted' depuis l'adresse indiquée dans le sujet. Cependant, ce
fichier n'est pas au format d'entrée de Weka. Il faudra donc effectuer une transformation de celui-ci.

Une première chose à faire est d'enlever les points en fin de ligne.
Cela peut être effectué par la commande : sed 's/\.$//g' kddcup.data_10_percent_corrted > kddcup.txt
Nous avons maintenant le fichier kddcup.txt qui se rapproche du format souhaité.


# TODO

- rédiger l'abstract
- reprendre le format d'entrée pour qu'il soit compatible avec celui-de Weka
- importer un module perso dans weka
- implémenter l'entropie

# Bibliographie

- https://weka.wikispaces.com/Writing+your+own+Classifier+%28post+3.5.2%29
  création d'un classifier avec Weka
- http://repository.cmu.edu/cgi/viewcontent.cgi?article=1161&context=math
  article portant sur l'entropie de Havrda et Charvat 
