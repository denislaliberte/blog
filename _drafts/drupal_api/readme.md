---
layout: post
title:  "Drupal api [titre de travail]"
date:   2014-10-13 12:00:00
categories: Drupal 
---


1. Code vs configuration
  - UI driven design 
  - approche itérative
2. Combinaison hook / api funciton
  - layout
  - pages
  - listes de contenu
  - block
3. Habitude / convention
  - Module avec une seule responsabilité
  - Namespace
  - features et dépendances

## 1 Code vs configuration 
voir drupal_api/conde_configuration.md


## 2  Combinaison
Il y as certaines combinaison de hook et fonction qui reviennent continuellement

J'évite le mot pattern car il est un peu sur-utilisé en développement et ce que 
j'expose ici est plus près d'une habitude que d'un design pattern au sens formel.

### process 
Avec le développeur frontend on étudie les maquettes grahpique et on décide ensemble
des variables et des templates dont on auras besoin pour rendre la maquette et
les différentes déclinaison.

Ensuite dépendant du cas soit je vais créer des page ou block custom ou je vais
overrider des templates. Puis je vais utiliser les api pour récupérer les datas 
et les formater en array.
pour réviser les concept d'overrides de template et de hook [docuemtation]() 


process habituel, presque routinier, 

- analyse du template
- configuration du backend (menu, content type )
- override templates, block ou page
- query the api to get variables
- process and query to more variable
- null check format variable array
- pass to the templates

## project_layout.module

## listes de contenu



## modules

separation of concern 
single class responsability

Module avec le moins de responsabilité possible, une seule choses

Défits 
- réutilisation de code
- module librairy
- intégration


## Module d'intégration

dependency

## script d'installation
dcycle
hook_install
hook_update_n
theme_enable
module_enable
module_disable
variable_set
$languages = language_list();
variable_set('language_default', $languages[$lang_code]);

compliqué à s'y retrouver si on n'as qu'un script pour tout le projet


## features

utiliser le moins possible

dés que je peux scripter quelque choses je le fait, variables, droits

## convention de nom
nom de module projet_
variable module_data
module_callback
preprocess node page html
    - ajoute une variable project_module_data qui contiens tout les
    donnés du module

## structure de fichier

/sites/all
  /modules
    /contrib
    /patch
    /project
  /theme
    /project_name
    /templates

## project module
/sites/all/modules/project
      project.module
      /project_integration
        project_integration.install
      /features
        /project_features
      /projetc_blog
        project_blog.module
        /themes


## develmodule
Configuration différente pour les instance de développement
Module à ne pas enabler en production

## contrib module
- date field
- link field et linkit
- pathauto, pathologic


autres
drupa_get_path
module_load_include



## convention
  - 1 responsabilité par modules
  - overrides des templates dans le thème
  - 1 module (deploy ou integration ) responsable de construire le site
  - favoriser les apis vs la configuration
  - hook_menu, i18n, hook_block
  - La logique se retrouve toutes au niveau des modules, riens ou presque dans les 
  - templates
  - array de data dans les templates, entityMetadataWrapper
  - one line installer
  - favoriser les entityfieldquery vs les views
  - processing de menu
  - fichier de moins de 100 lignes de codes
    - séparer les hook dans des includes
    - abstraction, classe library

## citation et ressources 
 API Over Everything : The reason is because 3rd-party modules have assumptions that can lead to technical debt. Many times, budgets are blown because of the work you have to do to undo a default assumption.

http://www.phase2technology.com/blog/static-prototyping-and-keeping-drupal-simple-kds/

// pragprog 
- Don't use wizard code you don't understand p198
- Don't programme by coincidence 172

// martin fowler

rich hickey simple vs easy

Ford, accelerators p18
"Graphical operating systems fovor convenience (and eye candy) over raw efficiency"

// ressources pour apprendre l'api


Driver par l'interface graphique
Outils et modules
- focus 
- one responsability
Namespace et structure
Api function et hook
the drupal ways
- embivalent
- 
