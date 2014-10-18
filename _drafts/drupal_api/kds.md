# Keep Drupal Simple

J'ai une nouvelle obsession depuis le début de l'année, développer tout ce que je
peux en code et éviter le plus possible la configuration par l'interface graphique
et mes projets sont de plus en plus stable, maléable et simple à comprendre. À 
chaque projet je trouve de nouvelle fonction que je peux utiliser pour éviter 
l'interface graphique.

Il y as deux semaines j'ai découver le billet [Static Prototyping and Keeping 
Drupal Simple (KDS)](bit.ly/k-d-s) de Frederic Mitchell de Phase 3. L'idée de KDS 
c'est que les module contribuée comme views ou pannels sont rapide à configurer
au départ mais qu'ils viennent avec leur propres assomptions et une complexité
accidentelle. Il propose [...]

## sources 

Je me suis inspiré d'une présentation que Mitchell as donné plus tôt cette année 
[30 DRUPAL 8 API FUNCTIONS YOU SHOULD ALREADY KNOW](https://bit.ly/d8-api) pour 
présenter à l'équipe technique de mon agence mes habitudes de développement. 


## Prérequis

Pour la suite de ce billet je présume une connaissance des concept de base des 
techniques de base de drupal comme l'override de template et l'utilisation
de hook.

[liens]

## project le site
J'ai présenté un exemple de site fictif nommé 'project' et trois module exemple 
qui regroupe des fonctionnalité commune à tout les projet de site web [...]

project_Layout

project_pages

project_blog


## project_layout

page.tpl.php

hook_preprocess_page

```php
print $project_layout_data['banner'];
```

Partials... header, footer, menu

hook_theme

``` php
$header = theme('header', $variables);
```

Menu custom

menu_tree_page_data()

url()

Menu avec images et classes... 
 
menu_attributes

```console
$ drush dl menu_attributes
```

file_create_url($uri)

Language switcher

language_negotiation_get_switch_links()

drupal_is_front_page()

``` php
function getLanguageSwitcher(){
$path = drupal_is_front_page() ? '<front>' : $_GET['q'];

 $switcher = language_negotiation_get_switch_links(
'language_url', 
$path
);
return $switcher >links;
}
```



## project_pages

Module pour la gestion des pages de contenu du site

node page.tpl.php

```php
function project_pages_preprocess_node( $variables ) {

if($variables['type'] == 'pages') {
$variables['project_pages_data'] = ['test'];

}
}
```

Field Values

```php
$ drush dl entity
```

entity_metadata_wrapper()

```php
$value = $node >field_number[LANGUAGE_NONE][0]['value'];
```
 
```php
$wrapper = entity_metadata_wrapper('node', $node);
```
 
```php
$value = $wrapper >field_number >value(); 
```

```console
$ drush dl link 
$ drush dl linkit
```
 
```console
$drush dl field_collection
```

```console
$drush dl date ; 
```
 
et [briannesbitt/Carbon](https://github.com/briannesbitt/Carbon)




## project_blog
Exemple de module qui gère une liste de contenu... 
 
ça aurrais aussi pus être communiqué, offre d'emploie,
manuel d'utilisation, commerce, produits etc

node blog.tpl.php

hook_preprocess_node()

hook_menu
```php
function project_blog_menu() {
return [
'/blog/list'=> [
'page callback' =>'project_blog_callback'
]
];
}
```

project.com/blog/list

```php
function project_blog_callback() {
return "hello world"
}
```

project_blog_i18n_translate_path

new EntityFieldQuery()

node_load_multiple()

theme('pager')

Une liste sur une page wysiwyg ?

project_blog_block_info 

project_blog_block_view

menu_get_object

Exporter la configuration 

``` console
$ drush dl features
```
dependencies[] = project_blog_nodetype

scrip de mise à jours
project_blog.install

```php
project_blog_install_update_7001() {
module_enable('project_blog_nodetype');
```

## project_integration 

Gestion des dépendances

Script d'installation


