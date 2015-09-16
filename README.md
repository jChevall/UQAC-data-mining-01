# UQAC-data-mining-01
Devoir proposé dans le cadre du cours de forage de données à l'UQAC. A pour but de détecter des intrusions avec une version améliorée de l'algorithme ID3.

# 2.1 Synthèse

L'article présenté porte sur la détection de tentatives d'intrusion dans un système informatique. Il présente un classifier inspiré de ID3. Celui-ci affiche, d'après l'article des performances bien supérieures aux classifiers existants sur un jeu de données. Celui-ci permet aux classifiers d'apprendre quelles requêtes sont des utilisations normales ou des attaques. 

Il est également présenté dans l'article une constante 'alpha' comprise entre 0 et 1 qui influe sur une partie de l'algorithme.

L'objectif de ce document est de retrouver les résultats obtenus dans l'article et d'étudier d'avantage l'influence de la constante 'alpha' dans les performances de l'algorithme.

Le jeu de données utilisé contient près de 5 millions d'instances et provient de la DARPA (Defense Advanced Research Projects Agency) qui est l'agence qui effectue des travaux de recherche & dévelopement à usage militaire. 

# Bibliographie

- https://weka.wikispaces.com/Writing+your+own+Classifier+%28post+3.5.2%29
  création d'un classifier avec Weka
