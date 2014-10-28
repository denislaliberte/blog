---
layout: post
title:  "Keep Drupal Simple, project_layout"
date:   2014-10-28 00:00:00
categories: 
---

~introduction, retour et lien sur kds

## project_layout

Le template page.tpl.php contiens le layout global de drupal, le header, le footer, 
les colonnes et menus. Ce qui est spécifique aux pages est contenu dans des régions
affiché dans ce layout.

~exemple régions

Une approche commune à drupal c'est de mettre le plus de choses possible du layout
dans des blocks et de les afficher dans les régions... le page.tpl ne contiens que 
peu de markup.

J'ai une approche différente. Le contenu spécifique à une page est affiché dans 
la région content et on utilise le hook_preprocess_page pour préparer un array de
string à afficher dans le template.

```php
print $project_layout_data['banner'];
```

Étant donné que le fichier page.tpl finis par être gigantesque on déclare des theme
custom avec le hook_theme pour le header le footer et pour chacuns des menus. Dans
le hook_preprocess_page on vas utiliser la fonction theme() pour appeler ces templates
avec les variables spécifique dont il as de besoin.

``` php
$project_layout_data['header'] = theme('header', $variables);
```

## Menus



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



