---
layout: post
title:  "Confoo cleancode"
date:   2014-03-02 17:19:33
categories: Conferences cleancode
---

Au dernier Confoo j'ai vu la conférence de Adam Culp, une conférence sur le 
cleancode en php, pourquoi c'est important et comment le faire.

J'ai trouvé une autre captation
[ video ](http://www.youtube.com/watch?v=Vs-9a1jewlA)
de la même conférence et les
[ slides ](http://fr.slideshare.net/adamculp/clean-application-development)

Dans sa conférence Culp présente deux livres, Refactoring de Marting fowler et 
Cleancode de Robert Martin. 

## cleane code ##

L'idée de base c'est que d'écrire du code lisible est vraiment important.
Un développeur passe la majorité 80% son temps à lire du code. Il serais donc 
logique de prendre le temps d'optimiser notre code pour que sa lecture soit rapide

La règle de base de Martin est de toujours laisser le code dans un meilleur état
qu'ons l'as trouvé. 

#### conséquences ###
Écrire du code sale en php est facile, mais ça as des conséquences réelle sur l'entrprise
Chaque fonctionnalité est plus longues à ajouter et coute plus cher.
C'est tentant pour un employé de quitter son emploie.
Il y as plus de risque de bug.

### professionnalisme ###
En tant que programmeur il faut agir comme des professionnel. C'est la 
responsabilité du gestionnaire de projet de défendre le budget et l'échéancier
mais c'est celle du programmeur de défendre le code. Il faut apprendre à dire non
à la pression pour produire du meilleur code. Évidement il faut aussi apprendre 
à communiquer nos raisons et à choisir nos batailles.

lorsqu-on nous demande d-aller plus rapidement et que ça nous empeche de répondre
aux bonnes pratique

le "je vais revenir plus tard pour le fixer" n-existe pas on ne reviens jamais

dette technique, le résultat de "je vais revenir le fixer plus tard"
on peut voir le développement comme une carte de crédit, si tu ne paye pas 
ta dette continue à grossir indéfiniment jusqu-à la faillite

... c-est dure de garder des employés quand tu as une grosse dette technique
... problème avec les clients, chaque feature est de plus en plus cher


### code smell ###
Les codesmell sont des indicateurs que le code n'est pas "clean", ils ne 
constituent pas le problèmes principal mais démontrent que le programmeur
ne respecte pas les bonne pratique. Si tu ne fait pas attentions à la 
consistance de ton code il y as des chance que tu ne t-occupe pas de découpler 
tes compostante etc

Quelques indicateurs : 
- L'absance de convention de nom
- Le non respect d'un standards de code
- De longues fonciton
- L'utilisation de variables globals
- L'utilisation exessive de commentaires

### commentaires ###
clean code dont need any comments
peut servire à formater un fichier de code mais ne doit jamais servir
à expliquer ce que le code fait, si tu ressent le besoin d-écrire un commentaire
c-est que tu as de besoin de faire du refactoring

le code doit être expressis et expliquer lui même ce qu-il fait par les noms de 
variables et les noms de fonciton...

le bon code nas pas besoin daucuns commentaires



### code sniffer###
possible de le faire en live avec un ide ou en ligne de commande


### cding standards ####
psr est entrain de faire sa place dans le php... tout les frameworks sont
entrain de migrer vers le psr

l-important c-est davoir une convention, on peut utiliser ceux de lindutrie
limportant cest juste den avoir un



### funciton ###
quand on en lis une il faudrais que ce soit évident


reconnaitre du code mauvais est facile, ça ne veux pas dire que cest facie den écrire du bon
cest un art à apprendre




##  refactoring ##
martin fowler
 as écris une version php des exemples de refactoring 

### désavantages du rewrite ###
courses aux nouvelles features 

## code reviews ##
important d'avoir une 2e paire d'yeux sur le code

## test ##
introduction sur le tdd

si on le fait en premier le process est plus facile car on attrape des bugs
au fur et à la mesure pas à la fin


