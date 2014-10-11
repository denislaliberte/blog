drupal api
=========

## code over configuration
 API Over Everything : The reason is because 3rd-party modules have assumptions that can lead to technical debt. Many times, budgets are blown because of the work you have to do to undo a default assumption.

http://www.phase2technology.com/blog/static-prototyping-and-keeping-drupal-simple-kds/

// pragprog 
- Don't use wizard code you don't understand p198
- Don't programme by coincidence 172

// martin fowler

simple vs easy

Programmer demande un effort initial, il faut apprendre les apis, il peut être
tentant d'utiliser l'interface

Impossible de faire du tdd avec l'interface graphique

réutilisation de code, à l'intérieur d'un projet, entre les projets

Ford, accelerators p18
"Graphical operating systems fovor convenience (and eye candy) over raw efficiency"




## introduction
Dans ce billet je vais lister les hook et les fonction que j'utilise habituellement
dans mes projets.

contrainte graphique 

## concept de base 
### hook

### templates 

La technique est assez simple soit on override les fichier template et on utilise
des hook_preprocess pour obtenir et traiter les variables ou on register un block 
ou une route pour afficher du html custom

##

process habituel, presque routinier, 

- analyse du template
- configuration du backend (menu, content type )
- override templates, block ou page
- query the api to get variables
- process and query to more variable
- null check format variable array
- pass to the templates



## page

Le template page.tpl.php est utilisé pour le layout général du site, le header 
et le footer qui apparisse surtoutes les pages du site.

On peut utiliser le hook_preprocess_page pour préparer les variables pour ce 
template.

### menus
Je n'ai pas vu de site ou le menu par défaut de drupal convenais, généralement 
le markup et les classe fournis ne conviennent pas au desing et à l'intéraction
voulue.

On peut utiliser la fonction menu_tree_page_data pour récupérer un array contenant
les données du menu et les formater en fonction des classe custom dont on as de 
besoin.

- fonction pour les liens

### Attibuts du menu
Le module menu_attributes fournis de nouveaux champs dans l'admin pour ajouter 
des images ou des classe aux items de menus 

On peut utiliser la fonciton file_create_url pour réfupérer les url des images 
ajouté par le module menu attibute

### languages switcher
En quelques lignes de code on peut avoir les donnés du language swicher.

- language_negotiation_get_switch_links 
- drupal_is_front_page
- l'objet global language permet de récupérer le langcode de la langue courant

- code sample

### variables
Les variables de drupal sont des 

- variable_set
- variables module pour l'admin
- realm var

### templates 
Je ne pense pas que ce soit une bonne idée de mettre

On peut déclarer nos propres templates avec le hook_theme et ensuite on peut
utiliser la fonction theme() pour récupérer les fonctions 

### breadcrumb
la fonction thème avec 

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

## theme

## menu 
- callback
- i18n_translate_path

- EntityFieldQuery
- node_load_multiple
- pagination

- drupal_render
- node_view
- node_view_multiple

## block 
- block_info 
- block_view
- menu_get_object
  

- taxonomy_get_tree
- i18n_taxonomy_localize_terms


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

Kds se sert de features que pour exporter, puis fait l'import dans un hook_update

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



## Conventions proposé
  1 responsabilité par modules
  templates custom minimal dans les modules
  overrides des templates dans le thème
  1 module (deploy ou integration ) responsable de construire le site
  favoriser les apis vs la configuration
  hook_menu, i18n, hook_block
  La logique se retrouve toutes au niveau des modules, riens ou presque dans les 
  templates
  array de data dans les templates, entityMetadataWrapper
  one line installer
  favoriser les entityfieldquery vs les views
  processing de menu
  fichier de moins de 100 lignes de codes
    - séparer les hook dans des includes
    - abstraction, classe library
