---
layout: post
title:  "Drupal camp Montréal - features entityMetadataWrapper tests"
date:   2014-09-31 22:40:33
categories: Drupal conference
---

Voici la suite de mon résumé du drupalcamp montréal 2014. 

Mon billet précédent les présentation sur  [Docker/sitediff, twig et et drupal to drupal migration](/tofo)

## tl;dr
```
- Modéliser ses features par use case vs par type de configuration
- Une vision différente des tests automatisés
- J'ai hâte que drupal 8 sorte pour utiliser twig
```


Gérer la configuration de son site avec Features
--------

![features](/images/drupalcamp/features.png)

C'est un outils pratique pour gérer la configurations
types de contenu, variables, profil wysiwyg... tout ce que drupal 7 met dans la 
database feature peut l'exporter dans du code.  Mais avec certains composante il 
as comportement étrange, par exemple certain changement de configuration sont 
importé automatiquement sans passer par la commande revert et d'autres ne sont
tout simplement pas pris en compte comme lorsqu'on supprime un champ dans un type
de contenu.

Bref c'est un outil imparfait mais J'avais hâte d'avoir le point de vue de 
Pierre Buyle de Phéromone.

J'ai souvent la même discussion avec d'autres developpeur sur features... comment on
sépare les features, une seul features pour tout le site c'est définitivement 
ingérable, une features par 'use case' ça peut être complexe et générer des
conflits et souvent on finis par exporter une features par type de configuration, content_type, configuration_wysiwyg, configuration_metadata etc...

Pierre Buyle de phéromone nous as présenté une vision intéressante. Il modélise 
ses features par 'use case', et il prend soins de bien déclarer ses dépendances.
Lorsqu'un élément est réutilisé par plusieur features, comme par exemple un field
qui se retrouve sur plusieur type de contenu il crée une features abstraite dont 
dépendent les autres features un peu comme on fait en développement orienté objet.

Finalement il ajoute une features d'intégration qui dépend de tout les features 
du site.

Ils nous as aussi donné une liste de configuration qu'il évite d'exporter avec
features, les roles et permissions, les langues, terme de taxonomie, le contenu

Je n'ai pas pu trouver les slides de la présentation mais il as mentoinné qu'un
billet de blogue expliquant sa technique étais en préparation.


Twig et drupal 8
----------------

![twig](/images/drupalcamp/twig.png)

J'ai beaucoup aimé travailler avec twig sur des projets silex, et je doit avouer
que je déteste vraiment comment fonctionne l'outil de templating de drupal 7.
J'étais donc curieux de voir la conférence de Suzanne Dergacheva aussi de 
Evolvingweb et de voir comment twig avais été intégré à drupal 8.

La bonne nouvelle c'est qu'il n'y as pas de surprise, twig as été intégré 
à drupal tel quel. Il y as simplement quelques fonction qui ont été intégré.

On peut appeler la fonction t ``` { { variable | t} }``` et ils ont ajouté 
une fonction pour cacher des éléments dans une node `{ { content | without links} }`
et ils ont ajouté le block `{ {trans} } text à traduire { {endtrans} }` pour 
les traductions.

La conférencière nous as conseiller de voir la présentation de Fabien Potentier
le créateur de twig au Drupalcon. (voir le lecteur en bas de page.)

Les sessions que j'ai manqué
---------------------------
Brad Muncs et Matthieu Gadrat de Symétris ont fait une présentation sur la 
personnalisation de l'interface administrateur, leur slides sont remplis d'exemple
de code et d'idées intéressantes. Des tableau de bord et menus sur mesure, des 
exemples d'action link, de tabs etc

[Slideshare](http://fr.slideshare.net/Symetris/ppt-drupal-campmtl2014backendv01)

Albert Albala de CGI as présenté la mise à jours de son workflow de déploiement automatisé
par script d'update sans clonde de db pour Drupal 8. Sa démarche est expliqué en 
détail sur ce blog post :

[Dcycle project ](http://dcycleproject.org/blog/68/approach-code-driven-development-drupal-8)



<iframe width="640" height="480" src="//www.youtube.com/embed/18sxjsLTesE?rel=0" frameborder="0" allowfullscreen></iframe>
