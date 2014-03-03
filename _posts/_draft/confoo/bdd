---
layout: post
title:  "Confoo BDD"
date:   2014-03-01 17:19:33
categories: conferences bdd
---
[slides](http://qafoo.com/talks/14_02_confoo_behave_behavior_driven_development.pdf)

Résumé de la conférences sur le Behaviours Driven Developpement au dernier Confoo.

Au dernier confoo j'ai été voir la conférences de Thobias Schlitt sur le Behavior 
Driven Developpent. Depuis quelques mois je m'intéresse à cette méthodologie et 
à ces librairies Cucumber pour le ruby et Behat pour le php. Dans ce billet je 
fait un mélange de résumé des notes que j'ai pris lors de laconférence avec mes 
notes de recherches.

## Résumé ##
Le Behavour driven developpement c'est le test driven développemnt avec un focus 
sur les fonctionnalités du site et sur la "business value" que ces fonctionnalités
créé pour le client. On écris des tests qui vérifie la foncitonnalité demandés par 
le client avant d'implémenter cette foncitonnalité et après on travaille à faire 
passer ce tests et uniquement à faire passer ce tests... et la grosse différence 
avec le tdd c'est qu'on écrit ces tests dans le language du client.

Les outils du BDD sont des outils de communication. Ces librairies aident à créer
des tests dans un languages commun entre tout les intervenants du projets qu'ils
aient des compétences techniques ou non. 

On écrit des scénario d'utilisation qui décrivent les fonctionnalités dans un 
language formel qui as le mérite d'être explicite. Puis les développeurs vont 
implémenter des tests qui valident que chacune des étapes du scénarios s'exécute
correctement. 

Donc on n'essaie plus de deviner quels sont les conditions d'acceptation d'une 
story avec une liste de bullet point, mais on valide vraiment ce qu'il est attendu
par l'utilisateur


## spécification exécutable ##
Un autres avantage de cette méthodologie c'est que ces spécification ne sont 
jamais dépassé. À chaque fois qu'on modifie le système on peut rouler l'ensemble
des tests et si on modifie le comportement d'une fonctionnalités donc que la 
documentation associées n'est plus à jours le tests vas planter et on vas devoir 
mettre à jours la documentation pour que le tests passe de nouveau.

## intégration continue ##
Évidement les développeurs peuvent ignorer les tests écrit, à moins qu'on 
intègre ces test à notre processus d'intégration continue. Par exemple le serveur
Jenkins peut rouler les tests et rejetter les commits qui brisent les tests.

donc même si un site est en ligne depuis des mois, on vas toujours avoir
des spécification claire de ce qu'il est supposé faire

## tests de non régression ##
Un autres avantage c'est qu'on as des tests de non régression. Chaque nouvelles 
foncitonnalités peut brisé n'importe quelle autres fonctionnalité. Théoriquement 
il faudrait qu'on testes toutes les fonctionnalité du site à chaque itération 
après quelques itérations le temps de tests commence à devenir vraiment grand et 
si on ne tests pas on as de gros risque pour que les bugs soient découvert par le
client ou en production. Les tests automatisé deviennent donc vraiment intéressants


## truc ##
Les product owner ou client sont souvent intimidé par un language formel au début
on peut leur laisser écrire des bullets points, une liste de  "vérifier que" 
puis ensuite traduire en Grekhin et leur faire valider après ce qui nous permet 
d'attraper une erreur d'interprétation et je parie qu'après quelques sprints ils 
vont commencer à écrire leurs propres scénarios.

## gerkhin ##
Le language formel utilisé pour décrire les scénario de test est le gerkhin:
given, when, then [and / but]
Qui est aussi disponiblle en français.


## vraid BDD ##
À la base le BDD est inspirés du "Domain Driven Design" et tout les étapes des tests
doivent parler directement aux "domains object". C'est une réalité qui est un peu 
loin de projets web de type content management system. 

Je ne dit pas que faire du vrais BDD et du DDD n'est pas une bonne idée mais 
dans le context que je voie tout les jours, un BDD moins puristes serais plus 
réalistes au début. 

## mink ##
Mink est un drivers qui offre une api pour commander des browsers de tests que ce 
soit des browser dit "headless" qui font des requetes get et qui tests le html ou 
des broser comme Selenium qui drive de vrais browsers.

Mink offre une api qui offre une abstraction du http et du html. On peut demander 
une page, remplir un formulaire, l'envoyer et tests le résultats retourné en quelques
lignes de tests.


## librairies ##
Cucumber, librairies original du bdd écrie en Ruby
Behat, port de cucumber en php 

