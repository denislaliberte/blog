confoo cleancode
===============
conférence sur le clean code en php, pourquoi c-cest important et comment le faire

La conférence est centré au tour de 4 livre, dont principalement Cleancode de 
Robert Martin, un livre qui as eu beaucoup d-impacte sur ma vision du développement

## cleane code ##
Règle toujours laisser le code dans un meilleur état que tu l-as trouvé

writing dirty code is easy in php
if you having really bad code how easy is it to keep good programmer


clean code dont need any comments


il faut apprendre à dire non à la pression
il faut être professionnel et apprendre à dire non
lorsqu-on nous demande d-aller plus rapidement et que ça nous empeche de répondre
aux bonnes pratique

on ne peux pas dire tout le temps non, il faut apprendre à choisir nos batailles
et apprendre à expliquer nos motivations

notre job est de défendre le code, la job dun pm est de défendre les times line
la notre est de défendre le code 




le "je vais revenir plus tard pour le fixer" n-existe pas on ne reviens jamais

quel est le résultat du dirty code

chaque features est plus longues à ajouter, 

dette technique, le résultat de "je vais revenir le fixer plus tard"
on peut voir le développement comme une carte de crédit, si tu ne paye pas 
ta dette continue à grossir indéfiniment jusqu-à la faillite

... c-est dure de garder des employés quand tu as une grosse dette technique
... problème avec les clients, chaque feature est de plus en plus cher


### code smell ###
c-est des indicateurs que du code n-est pas cleane
généralement c-est que le programmeur ne suis pas les bonnes pratique
si tu ne fait pas attentions à la consistance de ton code il y as 
des chance que tu ne t-occupe pas de découpler tes compostante etc

indicateur : 
-inconsistance dans le naming convention
-inconsistant codign standard
-de longues fonciton...
-globals
-commentaires : il ne sert pas à palier à du mauvais code

liens avec le concept de la fenetre brisé de pragmatic programmeur


### commentaires ###
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

on passe 80% de notre temps à lire du code... il faut donc optimiser le temps
de lecture du code et non celui de lecture


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


