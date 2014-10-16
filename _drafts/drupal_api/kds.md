# Keep Drupal Simple

---
## Keep Drupal Simple

Présentation sur mes habitudes de développement Drupal, les hook, modules et fonctions.

---
##sources
30 DRUPAL 8 API FUNCTIONS YOU SHOULD ALREADY KNOW

-Fredric Mitchell, Phase 2

[bit.ly/d8-api](https://bit.ly/d8-api)

---
##sources
Static Prototyping and Keeping Drupal Simple (KDS)

-Fredric Mitchell, Phase 2

[bit.ly/k-d-s](https://bitly.com/)

---
## Concept de base

fichiers `.tpl.php`

--

Override de hook...
--
 exemple hook_init

```php

function project_init() {
  print "hello world";
}
```

---
class: center
name: agenda
## Exemple project

project_Layout

project_pages

project_blog

---

# project_Layout

---

## project_layout

page.tpl.php

--

hook_preprocess_page

--

```php
print $project_layout_data['banner'];
```

---
## project_layout

Partials...

--
header, footer, menu

--

hook_theme

--

``` php
$header = theme('header', $variables);
```

---
## project_layout
Menu custom

--

menu_tree_page_data()

--

url()

---
## project_layout

Menu avec images et classes... 
--
menu_attributes

```console
$ drush dl menu_attributes
```

--

file_create_url($uri)

---
## project_layout
Language switcher

--

language_negotiation_get_switch_links()

--

drupal_is_front_page()

---
## project_layout

``` php
function getLanguageSwitcher(){
  $path = drupal_is_front_page() ? '<front>' : $_GET['q'];
    
 $switcher = language_negotiation_get_switch_links(
    'language_url', 
    $path
  );
  return $switcher->links;
}
```

---
template: agenda
---
# project_pages

---
## project_pages

Module pour la gestion des pages de contenu du site

--

node--page.tpl.php

---
## project_pages

```php
function project_pages_preprocess_node( $variables ) {

  if($variables['type'] == 'pages') {
    $variables['project_pages_data'] = ['test'];
  
    }
}
```

---
##project_pages 
Field Values

--

```php
$ drush dl entity
```

--

entity_metadata_wrapper()

---

##project_pages

```php
  $value = $node->field_number[LANGUAGE_NONE][0]['value'];
```
--
```php
  $wrapper = entity_metadata_wrapper('node', $node);
```
--
```php
  $value = $wrapper->field_number->value(); 
```

---
## project_pages

```console
$ drush dl link 
$ drush dl linkit
```
--
```console
$drush dl field_collection
```

---
## project_pages

```console
$drush dl date ; 
```
--
et [briannesbitt/Carbon](https://github.com/briannesbitt/Carbon)

---
template: agenda
---
# project_blog

---
## project_blog
Exemple de module qui gère une liste de contenu... 
--
ça aurrais aussi pus être communiqué, offre d'emploie,
manuel d'utilisation, commerce, produits etc

---
## project_blog
node--blog.tpl.php

hook_preprocess_node()

...

---
## project_blog
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
---
## project_blog

project.com/blog/list

```php
function project_blog_callback() {
  return "hello world"
}
```
--

project_blog_i18n_translate_path

---
## project_blog


new EntityFieldQuery()

--

node_load_multiple()

--

theme('pager')

---
## project_blog

Une liste sur une page wysiwyg ?

--

project_blog_block_info 

--

project_blog_block_view

--

menu_get_object

---
## project_blog

Exporter la configuration 

--

``` console
$ drush dl features
```

--

dependencies[] = project_blog_nodetype

---
## project_blog

scrip de mise à jours

--

project_blog.install

--
```php
project_blog_install_update_7001() {
module_enable('project_blog_nodetype');
```

---
## project_integration 

--

Gestion des dépendances

--

Script d'installation

---
template: kds


