---
layout: post
title:  "Drupal camp Montréal - features, twig, interface administrateur, Dcycle d8"
date:   2014-10-01 23:10:00
categories: Drupal conference
---

Voici la suite de mon résumé du drupalcamp montréal 2014. 

Mon billet précédent les présentation sur  [Docker/sitediff, drupal to drupal migration, Entity api](/drupal/conference/2014/09/29/Drupal_camp_montreal_Docker_sitediff_d2d_migration_Entity_Api.html)

## tl;dr
```
- Modéliser ses features par use case vs par type de configuration.
- Des outils et techniques pour configurer l'interface administrateur.
- J'ai hâte que drupal 8 soit stable pour utiliser twig.
- Une technique de gestion de configuration dans Drupal 8.
```


Gérer la configuration de son site avec Features
--------

![features](/images/drupalcamp/features.png)

La question revient régulièrement, comment on séparer les features, une seul 
features pour tout le site c'est dificile à gérer, une features par 
'use case' ça peut être complexe et générer des conflits et souvent on finis par
exporter une features par type de configuration ex. content\_type, 
configuration\_wysiwyg, configuration\_metadata etc...

Pierre Buyle de phéromone nous as présenté une vision intéressante. Il modélise
ses features par 'use case', et il prend soins de déclarer les dépendances
entre les features. Lorsqu'un élément est réutilisé par plusieur features, comme
par exemple un field qui se retrouve sur plusieur types de contenu il crée une 
feature abstraite dont dépendend les autres features un peu comme on fait en 
développement orienté objet. Finalement il ajoute une features d'intégration qui
dépend de tout les features du site.

Ils nous as aussi donné une liste de configuration qu'il évite d'exporter avec
features, les roles et permissions, les langues, terme de taxonomie, le contenu.

Twig et drupal 8
----------------

![twig](/images/drupalcamp/twig.png)

J'étais curieux de voir la conférence de Suzanne Dergacheva aussi de Evolvingweb 
et de voir comment twig avais été intégré à drupal 8.

La bonne nouvelle c'est qu'il n'y as pas de surprise, twig as été intégré 
à drupal tel quel. Il y as simplement quelques fonction qui ont été intégré.

On peut appeler la fonction t `{{ "{{ variable | t" }} }}` et ils ont ajouté 
une fonction pour cacher des éléments dans une node `{{ "{{ content | without links" }} }}`
et ils ont ajouté le block `{{ "{{trans"}}}}text à traduire {{ "{{endtrans"}}}}` pour 
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
par script d'update sans clone de db pour Drupal 8. Sa démarche est expliqué en 
détail sur ce blog post :
[Dcycle project ](http://dcycleproject.org/blog/68/approach-code-driven-development-drupal-8)



<iframe width="640" height="480" src="//www.youtube.com/embed/18sxjsLTesE?rel=0" frameborder="0" allowfullscreen></iframe>
