
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



