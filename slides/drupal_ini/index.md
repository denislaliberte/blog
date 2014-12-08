class: center, middle
# Initiation a Drupal
---
## slides

denislaliberte.github.com/slides/drupal_ini

???
Les slides de la présentation sont disponible à cet url

__todo__ ajouter bitly pour slides et la version texte

---
name: agenda
## Agenda
- Drush
- Module


???

__todo__ ajuster l'agenda

---
name: drush
## Drush

--

### Drupal shell

???
Drush c'est le drupal shell, c'est l'outil en ligne de commande de drupal.

--

[Documentation | drush.org](http://www.drush.org/en/master/)

---
template: drush

### Project manager

???
Drush contiens un projet manager, qui peut télécharger et mettre à jours le core
de drupal, les thèmes et les modules.

--

```shell
$ cd ~/Sites
$ drush pm-download
Project drupal (7.34) downloaded to /Users/dl/Sites/drupal-7.34
```

---
template:drush

### Installation

???
Drush permet d'installer drupal, créer la base de données et les fichier de 
configuration.

--

```console
$ cd /Users/dl/Sites/drupal-7.34
$ drush site-install standard \
    --db-url=mysql://root:@127.0.0.1/drupaldatabase \
    --account-name=admin \
    --account-pass=asdf \
    --site-name=drupalini
```

---
template:drush

### Mise à jours

???
On peut faire les mises à jour du code et de la base de données par drush.

--

```console
$ drush upc
No code updates available.

$drush updb
No database updates required
```

---
template:drush

### Variables

???
Drush permet d'inspecter et de modifier les variables de drupal
--
```console
$ drush variable-get name
site_name: 'drupalini'

$ drush variable-set site_name new-name
site_name was set to "new-name".
```

---
template: drush
### script

???
On peut utiliser drush pour executer des script php ce qui est pratique pour 
explorer l'api.

--

```console
$ echo "<?php var_dump(menu_tree_page_data('main-menu'));" > test.php
$ drush php-script test.php
 array(1) {
   '50000 Home 218' =>
   
   [...]
```

---
template: drush

### Gestion des modules

???
On peut aussi gérer les modules, téléchargements, installations et update

Avec la commande suivante on télécharge le projet example de drupal. Ce sont des
exemple de module pour apprendre à travailler avec les api backend de drupal.

--

```shell
$ drush pm-download example
Project examples (7.x-1.x-dev) downloaded to sites/all/modules/examples.
```

[Examples for Developers | drupal.org](https://www.drupal.org/project/examples)

---
##hook_menu
---
## hook_theme
---
## hook_preprocess_
---
template: agenda

---
name: block
## block_example

--

???
Nous allons étudier le module 'block_example' qui démontre comment créer un block custom.

Au minimum un module contiens un fichier de configuration block_example.info et 
un fichier avec le code block_example.module.

Le fichier block_example.install contiens le script d'installation et le block_example.test
contiens les tests d'intégration drupal avec Simple Test.
--

```console
$ cd sites/all/modules/examples/block_example
$ ls
block_example.info
block_example.install
block_example.module
block_example.test
```

---
template: block

### block_example.info
???
Le fichier info contiens l'information du module qui seront affiché dans 
l'interface d'administration ou dans la commande `drush pm-info`.
--

```
name = Block Example
description = An example outlining how a module can define blocks.
package = Example modules
core = 7.x
```

---
template: block

### HOOK_block_info

???
Dans le fichier .module on définie des hook pour que drupal puisse appeler notre 
code. Les hook sont des fonction qui débute avec le nom du module.

Par exemple pour implémenter hook_block_info on définie une fonction avec le nom
block_example_block_info().
--

```php
<?php
  function block_example_block_info() {
```

???

Le hook block_info on retourne les informations de notre block à drupal.
---
template: block

```php
  $blocks['example_uppercase'] = array(
    'info' => t('Example: uppercase this please'),
    'status' => TRUE,
    'region' => 'sidebar_first',
  );
  return $blocks;
 }
```

???
Les valeurs possible de l'array de block est documenté sur le site de drupal.org

---
template: block

[hook_block_info | drupal.org](https://api.drupal.org/api/drupal/modules%21block%21block.api.php/function/hook_block_info/7)

[hooks | drupal.org](https://api.drupal.org/api/drupal/includes%21module.inc/group/hooks/7)

???
Lorsque drupal as les information du block, on peut l'assigner à une région dans 
l'interface administrateur.
---
template: block

example.local/admin/structure/block

![](images/block.png)

---
template: block

### hook_block_view

???
Le hook block view est appelé par drupal avant d'afficher les block et le machine
name du block est passé en argument.
--

```php
function block_example_block_view($delta = '') {
  switch ($delta) {
    case 'example_configurable_text':
```

???
On as simplement à ajouter la string qu'on veux afficher comme valeur à 
la clé 'content' pour qu'elle s'affiche dans le block.
---
template: block
### example_empty

```php
    case 'example_empty':
      $block['subject'] = t('Title of second block');
      $block['content'] = block_example_contents($delta);
    break;
```
---
name: Region

###

---
name: theme


---
## Système de région
    créer une nouvelle région
   Associer un block à une région
---
## Système d'ouverride de template dans drupal



---
## Système de variables
   déclaration métadata
   formulaire
   fonctions
---
## Api de contenu
   EntityFieldQuery
   Entity api
---
## Création d'un type de content
---
## Utilisation du module field collection
---
## Gestion des menus
---


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
