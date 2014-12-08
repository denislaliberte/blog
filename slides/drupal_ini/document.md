# Initiation a Drupal
## slides

denislaliberte.github.com/slides/drupal_ini

Les slides de la présentation sont disponible à cet url

__todo__ ajouter bitly pour slides et la version texte

## Agenda
- Drush
- Module



__todo__ ajuster l'agenda

## Drush


### Drupal shell

Réfère à drupal shell, c'est l'outil en ligne de commande de drupal.




### Project manager

Drush contiens un projet manager, qui peut télécharger et mettre à jours le core
de drupal, les thèmes et les modules.


```shell
$ cd ~/Sites
$ drush pm-download
Project drupal (7.34) downloaded to /Users/dl/Sites/drupal-7.34
```


### Installation

Drush permet d'installer drupal, créer la base de données et les fichier de 
configuration.


```console
$ cd /Users/dl/Sites/drupal-7.34
$ drush site-install standard \
```


### Mise à jours

On peut faire les update du code et de la base de données par drush.


```console
$ drush upc
No code updates available.

$drush updb
No database updates required
```


### Variables

Drush permet d'inspecter et de modifier les variables de drupal
```console
$ drush variable-get name

$ drush variable-set site_name new-name
site_name was set to "new-name".
```

### script

On peut utiliser drush pour executer des script php ce qui est pratique pour 
explorer l'api.


```console
$ echo "<?php var_dump(menu_tree_page_data('main-menu'));" > test.php
$ drush php-script test.php
 array(1) {
   '50000 Home 218' =>
   
   [...]
```


### Gestion des modules

On peut aussi gérer les modules, téléchargement, installation et update

Dans cet exemple on télécharge les modules d'exemple de drupal.


```console
$ drush pm-download example
Project examples (7.x-1.x-dev) downloaded to sites/all/modules/examples.
```



## Création d'un module


### block_example

Nous allons étudier le module 'block_example' qui démontre comment créer un block custom.

Au minimum un module contiens un fichier de configuration block_example.info et 
un module avec le code block_example.module.

Le fichier block_example.install contiens le script d'installation et le block_example.test
contiens les tests d'intégration drupal avec simple test.

```console
$ cd sites/all/modules/examples/block_example
$ ls
block_example.info
block_example.install
block_example.module
block_example.test
```


### block_example.info
Le fichier info contiens l'information du module 

```
name = Block Example
description = An example outlining how a module can define blocks.
package = Example modules
core = 7.x
```


### hook_block_info

Dans le fichier .module on définie des hook pour que drupal puisse appeler notre 
code. Les hook sont des fonction qui débute avec le nom du module.

Dans cette exemple on défini le hook pour fournir les informations de notre block
À drupal, on peut voir la structure attendu sur la page de la documentation.

```php
<?php
  function block_example_block_info() {
# ....
  $blocks['example_uppercase'] = array(
    'status' => TRUE,
    'region' => 'sidebar_first',
  );
  return $blocks;
 }
```



### hook_block_view





## hook_preprocess_
## hook_theme
## hook_block
##hook_menu
## Système d'ouverride de template dans drupal







## Système de région
    créer une nouvelle région
   Associer un block à une région
## Système de variables
   déclaration métadata
   formulaire
   fonctions
## Api de contenu
   EntityFieldQuery
   Entity api
## Création d'un type de content
## Utilisation du module field collection
## Gestion des menus


Modication de la portion backend
## Gestions des librairies et autoloader (composer)
## Exemples de code et test automatisé (phpspec)
## Traitement des variables des éléments de conteu
    Drupal adapter
   Arrays functions
    Fields functions
   Menu


Utilisation de git et release cycle
## Fonction des différentes branches
## Fonction des différents Environnements
## Déploiement du code et mise à jours de la configuration

Gestion de la configurations et mise à jours automatisé

## Configuration drupal par script automatisés
     fichier.install
    hook_update_n
 ## gestion des variables et des modules
 ## gestion des roles et permissions
 ## Export de la configuration par features
 ## Module d'intégration
