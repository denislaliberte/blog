##drupal

### drupal productivity 
- dot files : dvg explore variables 
- utiliser les script depuir drush 
- Explorer les api depuis drush
- recherche google ciblié
- gd shorcut pour recherche google efficace  drupal 7 site:drupal.stackexchange.com OR  site:drupal.org

### kds
- entifiy field query plus productif que views 


### drupal 8 now
- drupal 8 now : tests and autoload 
- drupal 8 now par larowlan drupal core contributor (http://www.previousnext.com.au/blog/author/larowlan)
- prototypage rapide, toute, partial et feature toogle

- gestion des droits et profils dans drupal, api vs features
-trouver comment créer des role et ajouter des permission par l'api au 
lieu de features

https://api.drupal.org/api/drupal/modules!user!user.module/function/user_role_change_permissions/7
http://drupal.stackexchange.com/questions/50435/how-do-i-find-the-role-id-from-role-name

- utiliser le watch dog





##drupal permission
C'est trop facile de gérer les permission en code pour s'emêler avec features

`$drush scr test.php`
```php
$permissions = module_invoke_all('permission');
var_dump($permissions);
```

```php
function _add_permission_to_role($name,$permission) {
  $role = user_role_load_by_name($name);
  if($role) {
    user_role_change_permissions($role->rid,$permission);
  }else {
    watchdog(
      'stingray_permission',
      'Can\'t add permission to the role %role, role dont exist',
      ['%role'=>$name],
      WATCHDOG_WARNING
    );
  }
}
```

## drupal deploy
un seul script de déploiement c'Est un peu dure à maintenir et je ne pense pas 
que ce soit une bonne pratique, chaque 'usecase'/ domaine devrais avoir un module
une features au besoin et un script d'importation

avec module utils et module integration


## drupal testbench
2e instance de drupal configuré rapidement pour faire des tests
réinstallation from scratch
test de modules





