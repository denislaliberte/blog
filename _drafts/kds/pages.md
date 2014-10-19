
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

