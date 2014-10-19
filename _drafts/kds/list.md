
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


-->
