---
layout: post
title:  "Drupal camp Montréal - Docker, sitediff, d2d migration, Entity Api"
date:   2014-09-29 22:40:33
categories: Drupal conference
---

Voici un résumé de quelques conférences que j'ai vu au drupal camp montréal 2014.

![drupalcamp montréal logo](/images/drupalcamp/logo.png)


tl;dr
-----
```
- Sitediff, un outil intéressant pour faire des diff de html entre deux site.
- Docker est plus rapide et simple que vagrant, mais ça prend une VM linux.
- Entity metadata wrapper c'est un incontournable et ça se résume en deux minutes.
- Des exemples de drupal migrate d6 to d7.
```

<br/>
Test-Driven Drupal Using Docker
--------------------------------

![Docker logo](/images/drupalcamp/docker.png)

Alex Dergachev de Evolvingweb nous as présenté rapidement comment utiliser 
Doker et quelques aventages versus vagrant.

Docker est un conteur d'application, plus léger et plus rapide qu'une Machine 
virtuelle comme ce que vagrant utilise. C'est aussi plus intuitif à configurer
que vagrant puisqu'il utilise un langage proche du bash au lieu de chef ou puppet, 
donc pas de nouveau dsl à apprendre. Le désaventage de Docker c'est qu'il ne roule 
que sur linux donc si on développe sur OSX ou Windows il faut avoir une machine 
virtuelle linux en plus de Docker.

Il nous as aussi présenté un projet de migration complexe d'un site drupal 6 à 7 
pour l'université McGill ou ils ont développé un outils qui permet de faire un diff 
entre deux pages html. Donc on peut comparer l'ancienne version
avec la nouvelle de façon automatisé.

Quelques captures d'écran de sitediff :

![sitediff output 1 ](/images/drupalcamp/sitediff-output.png)

![sitediff output 2 ](/images/drupalcamp/sitediff-output-1.png)

[Repo Github de Sitediff](https://github.com/dergachev/sitediff)

On as aussi appris qu'ils utilisent phpunit pour tester le code des modules avec
des mock pour les appels à l'api de drupal et pour un autre projet ils ont
étendu migrate pour migrer un site de documentation en markdown vers drupal.

[slides de la présentation](http://dergachev.github.io/presentations/nyccamp-2014-docker/build/out.html)

[Une captation de la même conférence à NYC camp](https://www.youtube.com/watch?v=T3WcL6vyOG0)

Drupal to drupal data migration
-------------------------------

Matt Corks de Koumbit as fait une présentation sur migrate un framework orienté 
objet qui permet de scripter l'importation de donnés dans drupal. Son architecture 
permet de configurer rapidement les sources externes (csv, sql, autres cms, autre 
instance ou version de drupal etc), la destination dans drupal (node, terme, user...)
et toutes modifications qu'on as besoin de faire entre temps par des callback. Et 
son outils en ligne de commandes permet de faire les imports, tester et de faire 
des rool back.

On as pus voir quelques exemples concrets de migration drupal 6 à drupal 7, files 
term, location, multgroup field collection, taxonomy term et ces exemples sont 
disponible sur ce lien : 
[migrate_stuff](http://mvc.koumbit.org/presentations/2014-drupalcampmtl/migrate_stuff.tar.gz)

[slides](http://mvc.koumbit.org/presentations/2014-drupalcampmtl/)

Why Aren't You Using Entity Metadata Wrappers Yet?
----------------------
Au moment de sortir drupal 7 l'api des 'entity' n'étais pas complètes l'équipe as
donc choisit de faire un module contribué qui offre un wrapper aux entité. C'est 
vraiment un incontournable lorsqu'on doit aller chercher les valeurs d'une 'node' 
programmatiquement. 

François Xavier Lemieux de Coldfront Labs nous as donné une introduction sommaire 
à l'api avec exemples de getter et setter.

Voici un exemple inspiré de la [documentation officielle](https://www.drupal.org/documentation/entity-metadata-wrappers) 
qui résume bien la démonstration

```php
<?php
// sans entityMetadataWrapper
  $value = $node->field_number[LANGUAGE_NONE][0]['value'] 

// ...avec entity metadata wrapper (getter)
  $wrapper = entity_metadata_wrapper('node', $node);
  $value = $node_wrapper->field_number->value(); 
  
// exemple de setter
  $node_wrapper->field_number->set(1); 

//Pour avoir la liste des fields et autres propriétés d'une node
  dpm($wrapper->getPropertyInfo());
```


