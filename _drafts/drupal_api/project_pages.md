---
layout: post
title:  "project pages Drupal api [titre de travail]"
date:   2014-10-13 12:00:00
categories: Drupal 
---

## Pages de contenu 


### node

Chaque field des nodes as son propre template donc si on doit controler précisément
le html des node on doit overrider des dizaines de template et encore...

En déclarant un hook_preprocess_node on peut récupérer les valeurs de la node
et préparer un array de variable prêt à être afficher dans le templates
node.tpl.php qu'on peut overrider par type de contenu avec le fichier nommé
node--type.tpl.php




- EntityMetadataWrapper
null check

https://api.drupal.org/api/drupal/includes%21entity.inc/class/EntityFieldQuery/7


