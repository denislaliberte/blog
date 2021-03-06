---
layout: post
title:  "Keep Drupal Simple, l'introduction"
date:   2014-10-18 17:19:33
categories: 
---

J'ai une nouvelle approche au développement drupal depuis le début de l'année
j'essaie de développer tout ce que je peux en code et d'éviter le 
plus possible la configuration par l'interface graphique et mes projets sont de 
plus en plus stable, flexible et simple à comprendre. À chaque projet je trouve 
de nouvelle fonction que je peux utiliser pour éviter l'interface graphique.

Maintenant que j'en suis au 3e projet avec cette façon de travailler je commence 
à trouver des patterns récurent entre mes projets et j'ai l'impression qu'il est
temps que je commence à partager quelques idées, j'ai donc préparer une série 
de billet de blog et quelques présentation sur ce sujet.

## Pourquoi "Keep Drupal Simple" ?

Il y as deux semaines j'ai découver le billet [Static Prototyping and Keeping 
Drupal Simple (KDS)](http://bit.ly/k-d-s) de Frederic Mitchell de Phase 3 (c'est
le programmeur qui as leadé le projet de refonte du site du département de l'énergie 
fédéral Américains). L'idée de KDS c'est que les module contribuée comme views ou 
pannels sont rapide à configurer au départ mais qu'ils viennent avec leur propres
assomptions, du markup étrange, une complexité accidentelle et une dette technique.

C'est la première fois que je trouve un développeur de la communauté qui fait un
plaidoyer explicite pour le code custom, j'ai donc choisit de voler son buzz word
pour en faire le titre de ma première présentation.

Pour cette présentation j'ai choisit de présenter trois type de module custom avec
leur combinaison de hook, fonction, template et module contribué.

## project le site
J'ai présenté un exemple de site fictif nommé 'project' et trois exemple de modules,
trois billets suiveront avec les détails de ces modules.

- project_Layout, qui contiens le header, footer et les menus.

- project_pages, qui s'occupe des variables et des field d'une page wysiwyg.

- project_blog, qui est un exemple de liste de blog post sans utiliser views.



## Slides
Le lien pour les slides de ma présentation sur [Keep Drupal Simple ](/slides/kds)

---
## 30 DRUPAL 8 API FUNCTIONS YOU SHOULD ALREADY KNOW de Frederick Mitchell

Je me suis aussi inspiré d'une présentation que Mitchell as donné plus tôt cette 
année 30 DRUPAL 8 API FUNCTIONS YOU SHOULD ALREADY KNOW ou il présente chaque 
fonction et la met en contexte avec son équivalent dans drupal 7.

<iframe width="640" height="480" src="//www.youtube.com/embed/NWWf3h5JoMM?rel=0" frameborder="0" allowfullscreen></iframe>



