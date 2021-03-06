---
layout: post
title:  "Keep Drupal Simple, project_layout"
date:   2014-10-28 00:00:00
categories: 
---

Suite de mes billets sur mes habitudes de dveloppement drupal, pour l'introduction 
[Keep Drupal Simple](http://denislaliberte.github.io/posts/keep-drupal-simple/)

L'exemple de code se trouve sur ce gist [project_layout.module](https://gist.github.com/denislaliberte/75252ac4882c1bbbb0aa)

Pour chaque projet j'ai un module qui s'occupe spécifiquement du layout, les menus,
header, footer, bref de tout ce qui est commun à toutes les pages du site.

## project_layout

Le template page.tpl.php contiens le layout global de drupal, le header, le footer, 
les colonnes et menus. Ce qui est spécifique aux pages est contenu dans des régions
affiché dans ce layout.

Une approche fréquente dans le développement drupal c'est de mettre le plus de 
choses possible du layout dans des blocks et de les afficher dans les régions... 
le page.tpl ne contiens que 
peu de markup. J'ai une approche différente. Le contenu spécifique à une page est 
affiché dans la région content et on utilise le hook_preprocess_page pour préparer 
un array de string à afficher dans le template.

```php
print $project_layout_data['banner'];
```

Étant donné que le fichier page.tpl finis par être gigantesque on déclare des theme
custom avec le hook_theme pour le header le footer et pour chacuns des menus. Dans
le hook_preprocess_page on vas utiliser la fonction theme() pour appeler ces templates
avec les variables spécifique dont il as de besoin.

``` php
$project_layout_data['header'] = theme('header', $header_variables);
```

## Menus

Dans certain cas on as besoin d'un markup vraiment préci pour le menu, la solution 
qu'on trouve la plus simple c'est d'utiliser la fonction `menu_tree_page_data()`
pour récupérer l'array de data du menu.

Les éléments de menu continnent le machine name de l'élément (ex node/14) et on 
peut utiliser la fonction `url()` pour obtenir l'alias d'url à utiliser dans le
menu (ex `example.com/foo/bar/biz`)


Pour ajouter des images ou des classes aux items de menu on utilise le module 
menu_attibutes et dans le cas des images on utilise la fonction file_create_url()
pour obtenir l'url de l'image à partir de l'id du fichier.

Finalement pour le sélecteur de langue on peut aussi obtenir les data avec ces 
deux fonction :

``` php
function _get_language_switcher(){
$path = drupal_is_front_page() ? '<front>' : $_GET['q'];

 $switcher = language_negotiation_get_switch_links(
'language_url', 
$path
);
return $switcher->links;
}
```



