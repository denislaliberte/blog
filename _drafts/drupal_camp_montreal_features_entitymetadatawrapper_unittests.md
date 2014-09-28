---
layout: post
title:  "Drupal camp Montréal - Docker, Twig, d2d migration"
date:   2014-09-23 22:40:33
categories: Drupal conference
---

- Modéliser ses features par use case vs par type de configuration
- Faire un prototype "front end" ça permet de développer plus rapidement
- Entity meta data wrapper c'est un incontournable
- L'interface administrateur dans un cms c'est important

Gérer la configuration de son site avec Features
--------
Je ne peux pas me passe de features... mais je le déteste...

Features c'est indispensable pour exporter la configuration de drupal 7. Je sait
que certains arrivent à tout configurer dans le code sans utiliser features et 
j'ai étudié la possibilité mais pour l'instant la façon la plus productive pour
moi de travailler avec drupal 7 c'est features.

J'avais vraiment hâte d'avoir le point de vue de Pierre Buyle sur l'utilisation 
de features.

J'ai souvent la même discussion avec d'autres dev sur features... comment on
sépare les features, une seul features pour tout le site c'est définitivement 
ingérable, une features par use case ça peut être complexe et emporter des 
conflits et souvent on finis par exporter une features par type de configuration
- content_type, configuration_wysiwyg, configuration_metadata etc...

Pierre Buyle de phéromone nous as présenté une vision intéressante. Il modélise 
ses features par use case, map ses dépendances créé des features intermédiaire pour
les configurations qui sont utilisé par plusieur features et ajoute une 
features d'intégration qui dépend de tout les features du site.

Je n'ai pas pu trouver les slides de la présentation mais il as dit qu'un
billet de blogue expliquant sa technique étais en préparation.




Why Aren't You Using Entity Metadata Wrappers Yet?
----------------------
Au moment de sortir drupal 7 l'api des 'entity' n'étais pas complètes l'équipe as
donc choisit de faire un module contribué qui offre un wrapper aux entité.

C'est vraiment un incontournable lorsqu'on doit aller chercher les valeurs d'une
node programmatiquement, je ne peux vraiment pas m'en passer. 

On as eu droit à une introduction sommaire à l'api avec exmeple de getter et setter
je doit avouer que pour une séance indentifié comme avancé je m'attendais à en 
apprendre un peu plus sur les opportunités de l'api.

Des tests modernes pour Drupal
------------------------------

Étant donné le titre de présentation je m'attendais à apprendre quelques trucs
intéressant à intégrer à ma stratégie de tests pour drupal 7 [liens] mais le 
conférencier avais une philosophie de tests assez loin de la mienne.

Il utilise phpunit pour automatiser ses tests et il bootstrap drupal à chaque tests.

Étant donné que ses exemples ne testais que des opération mathématique simple (1+1)
on n'as pas su quel étais sa stratégie pour les données. 

L'autre point original c'est qu'il utilise selenium créer des tests d'interface
(ce qu'il appelle des tests d'intégration) 

et il appelle ses tests unitaire depuis les script généré par sélénium.

Finalement il utilise behat pour créer des "acceptance tests" mais au lieu de 
l'utiliser comme un outil de collaboration et de communication avec le client 
il as plutôt suggérer que ce soit un gestionnaire de projet membre de l'équipe
de production qui s'en charge...


Le conférencier as présenté une technique ou il bootstrap drupal dans 
avant de rouler ses tests unitaires 

http://fr.slideshare.net/hellosct1/des-testsmodernespourdrupal

